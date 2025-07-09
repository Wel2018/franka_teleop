import sys
import threading
import numpy as np
from rich import print
from toolbox.core.time_op import get_time_str
from toolbox.robot.franka_arm_client import FrankaArmClient
from toolbox.qt import qtbase
from .ui.ui_form import Ui_DemoWindow
from toolbox.robot.robot_collect import FrankaCollector
from .setting import SettingWindow
from . import AppConfig, logger, VERBOSE, THREAD_DEBUG, APPCFG


class SharedData:
    """共享数据"""
    incr = {
        "x": .0,
        "y": .0, 
        "z": .0,
        "R": .0,
        "P": .0,
        "Y": .0,
        "gripper": 0, # 0 表示没有动作，1 表示打开夹爪，-1 表示关闭夹爪
    }
    incr_bak = {}


class WorkMode:
    """遥操作工作模式"""
    keyboard = 0
    spacemouse = 1
    iphone = 2
    io = 3


class MainWindow(qtbase.IMainWindow):
    """应用具体实现"""
    # 定时器和线程名称
    TH_COLLECT = "collect"
    TH_SYNC = "sync"
    TH_CAM = "cam3d"
    TH_CTL_MODE = "teleop_ctl_mode"
    TIMER_ROBOT_STATE = "robot_state"

    is_quit_confirm = 0  # 程序退出确认
    is_keyboard_ctrl = 1  # 键盘控制开关
    is_collect_data = 0  # 数据集收集开关
    is_gripper_open = 1  # 当前夹爪状态
    is_debug = 0
    is_going_to_init_pos = 0
    VERBOSE = VERBOSE

    def __init__(self, parent = None):
        ui = self.ui = Ui_DemoWindow()
        super().__init__(ui, parent)

        # 初始化
        self.init(
            confcache_name="franka_teleop",
            apptitle=AppConfig.title,
            ui_logger=ui.txt_log,
            logger=logger,
            fontsize=AppConfig.fontsize,
        )

        # 子页面
        self.setting_wd = SettingWindow(self)
        self.kb_mapp = self.setting_wd.keyboard_mapp

        # 绑定点击事件
        self.bind_clicked(ui.btn_setting, lambda: self.setting_wd.showNormal())
        self.bind_clicked(ui.btn_clear, self.clean_log)
        self.bind_clicked(ui.btn_gripper, self.set_gripper)
        self.bind_clicked(ui.btn_open_dir, lambda: self.open_dir(self.ui.dataset_dir.text()))
        self.bind_clicked(ui.btn_play, self.play)

        # 工具栏
        # self.set_icon(ui.act_setting, "data/assets/setting.svg")
        self.bind_action(ui.act_setting, lambda: self.setting_wd.showNormal())

        # 添加按钮图标
        # self.set_app_icon("data/assets/franky.svg")
        # qtbase.QGuiOperate.label_set(ui.msg, "styled", "0")

        # 设置勾选状态
        self.set_check(ui.is_keyboard_ctrl, self.is_keyboard_ctrl)
        self.set_check(ui.is_collect_data, self.is_collect_data)
        self.set_check(ui.rb_keyboard, 1)
        
        # 勾选框glob
        self.bind_checked(ui.is_keyboard_ctrl, self.keyboard_ctl)
        self.bind_checked(ui.is_collect_data, self.collect_data)
        
        # 监听工作模式选择
        for rb in [ui.rb_keyboard, ui.rb_spacemouse, ui.rb_iphone, ui.rb_io]:
            rb.clicked.connect(self.ctl_mode_changed)
        # 默认工作模式
        self.set_enable(ui.rb_iphone, 0)
        self.set_enable(ui.rb_io, 0)
        self.mode = WorkMode.keyboard
        
        # 遥操作控制步长改变
        # 线速度、角速度
        self.pos_vel = ui.step_posi_vel.value()
        self.rot_vel = ui.step_angle_vel.value()
        self.max_duration = 1000*60
        
        # 在 lambda 表达式中不能使用赋值语句（=）。
        self.bind_val_changed(
            ui.step_posi_vel, 
            lambda val: \
                setattr(self, 'pos_vel', round(val,3))
        )
        
        self.bind_val_changed(
            ui.step_angle_vel, 
            lambda val: \
                setattr(self, 'rot_vel', round(val,3))
        )

        # 摄像头
        zero_img = np.zeros((480, 640, 3), dtype=np.uint8)
        self.zero_img = qtbase.QPixmap(qtbase.cv2qt(zero_img))
        self.reset_viz()

        #self.tcost = Timecost(0, 1)
        self.pressed_keys = set()
        
        # 摄像头 --------------------
        self.camtype = APPCFG['camtype']
        from toolbox.cam3d import load_cam3d
        self.cam = load_cam3d(
            self.camtype, 
            camtypes_for_S_mode=APPCFG['camtypes_for_S_mode'],
            is_start_and_warmup=1
        )
        self.robot_cam_th = qtbase.CameraTask(
            qtbase.Camera3DWrapper(self.cam))
        self.robot_cam_th.bind(on_data=self.get_obs)
        self.add_th(self.TH_CAM, self.robot_cam_th, 1)
        
        # 机械臂控制 --------------------
        self.arm = FrankaArmClient()
        self.arm.gozero()
        
        self.add_log("程序初始化完成")
        
        # 检查服务器是否能够正常连接
        self.add_timer(self.TIMER_ROBOT_STATE, 100, self.refresh_state, 1)
    
    def get_ctl_mode(self):
        ui = self.ui
        if ui.rb_keyboard.isChecked():
            return WorkMode.keyboard
        elif ui.rb_spacemouse.isChecked():
            return WorkMode.spacemouse
        elif ui.rb_iphone.isChecked():
            return WorkMode.iphone
        elif ui.rb_io.isChecked():
            return WorkMode.io
        else:
            raise ValueError("未知控制模式")

    def ctl_mode_changed(self):
        """启动空间鼠标控制"""
        ui = self.ui
        self.is_collect_data = 0
        mode = self.get_ctl_mode()
        if mode == self.mode:
            self.add_log("请点击不同工作模式")
            return
        
        # 停止之前的任务线程
        self.stop_th(self.TH_CTL_MODE)
        
        if mode == WorkMode.keyboard:
            self.add_log("键盘控制")
            
        elif mode == WorkMode.spacemouse:
            self.add_log("SpaceMouse 控制")
            from .bgtask.spacemouse import SpaceMouseListener
            self.spacemouse_th = SpaceMouseListener()
            self.spacemouse_th.bind(on_data=self.spacemouse_cb, on_msg=self.add_log)
            self.add_th(self.TH_CTL_MODE, self.spacemouse_th, 1)
        
        elif mode == WorkMode.iphone:
            self.add_log("iPhone 控制 [暂不支持]")
        
        elif mode == WorkMode.io:
            self.add_log("IO 控制 [暂不支持]")
        else:
            raise ValueError("未知控制模式 [暂不支持]")
        self.mode = mode

    @qtbase.Slot(dict)
    def spacemouse_cb(self, data: dict):
        # print(f"{get_time_str(2)} data={data}")
        # self.cmd2incr(data, data)
        # 所有按键的数据都已同步
        incr = SharedData.incr
        
        # 将 spacemouse 数据格式转为 incr 字典
        _incr = {}
        for k in ['x','y','z']:
            _incr[k] = data[k] if data[k] else 0
        for k in ['R','P','Y']:
            _incr[k] = data[k] if data[k] else 0
        
        # 判断是否和之前的数值相同
        is_same = 1
        for k in ['x','y','z','R','P','Y']:
            if incr[k] != _incr[k]:
                is_same = 0
                break
        
        if is_same:
            return
        
        _incr.update({
            "duration": self.max_duration,
            "is_async": 1,
        })
        # print(f"{get_time_str(2)} {_incr}")
        self.arm.cartesian_velocity_control(_incr)
        SharedData.incr.update(_incr)
        

    def play(self):
        """执行任务理解逻辑"""
        self.add_log("回到默认位置")
        self.arm.goto_init_pos()

    def kb_collect(self):
        # 开始收集
        if self.is_collect_data == 0:
            self.is_collect_data = 1
            self.set_op_cmd("collect")
            self.add_log("开启数据采集模式")
            self.robot_collect = FrankaCollector(self.cam, self.arm, use_kb_incr=1, incr=SharedData.incr)
            self.robot_collect.bind(on_msg=self.add_log)
            self.add_th(self.TH_COLLECT, self.robot_collect, 1)
        else:
            self.is_collect_data = 0
            self.set_op_cmd("")
            self.add_log("关闭数据采集模式")
            self.stop_th(self.TH_COLLECT)

    def cam_search(self):
        self.cam_s = qtbase.CameraSearcher()
        self.cam_s.show()

    def set_gripper(self):
        """夹爪控制"""
        self.is_gripper_open = not self.is_gripper_open
        if self.is_gripper_open:
            self.add_log("打开夹爪")
            self.arm.gripper_open()
        else:
            self.add_log("关闭夹爪")
            self.arm.gripper_close()
            

    def reset_viz(self):
        self.pix_left = self.zero_img
        self.pix_right = self.zero_img

    
    def refresh_state(self):
        res = {}
        try:
            ee = self.arm.ee()
            j = self.arm.joints()
            gripper = self.arm.gripper()
            timestamp = get_time_str(4)
            
            ee = [f"{round(el, 2):.2f}" for el in ee] # type: ignore
            j = [f"{round(el, 2):.2f}" for el in j] # type: ignore
            self.ui.msg.setText((
                f"时间={timestamp} 位姿={ee} 夹爪={gripper} \n 关节={j}")
            )

            self.set_timer(self.TIMER_ROBOT_STATE, 100)
        except Exception as e:
            logger.error(f"e={e} get_data res={res}")
            self.ui.msg.setText(f"error={e} at {get_time_str(4)}")
            self.set_timer(self.TIMER_ROBOT_STATE, 3000)

    def keyboard_ctl(self, state):
        #state: 0 未勾选, 1 半勾选, 2 勾选
        if state == 2:
            self.is_keyboard_ctrl = 1
            self.add_log("开启遥操作模式")
        else:
            self.is_keyboard_ctrl = 0
            self.add_log("关闭遥操作模式")
        
    def collect_data(self, state):
        self.kb_collect()
        

    def cmd2incr(self, data: dict, cmd: str):
        """根据命令执行动作 
        `cmd := "+x", "-x`
        """
        step = self.pos_vel

        for op in ['R','P','Y']:
            if op in cmd:
                step = self.rot_vel
                break
        
        # xyz
        if cmd == "+x": 
            data["x"] = step
        elif cmd == "-x":
            data["x"] = -step
        elif cmd == "+y":
            data["y"] = step
        elif cmd == "-y":
            data["y"] = -step
        elif cmd == "+z":
            data["z"] = step
        elif cmd == "-z":
            data["z"] = -step
        
        # RPY
        elif cmd == "+R":
            data["R"] = step
        elif cmd == "-R":
            data["R"] = -step
        elif cmd == "+P":
            data["P"] = step
        elif cmd == "-P":
            data["P"] = -step
        elif cmd == "+Y":
            data["Y"] = step
        elif cmd == "-Y":
            data["Y"] = -step
        
        elif cmd == "gripper":
            if self.is_gripper_open:
                data["gripper"] = 1
            else:
                data["gripper"] = -1
        
        # return data

    def get_empty_incr(self):
        incr = {
            "x": .0,
            "y": .0, 
            "z": .0,
            "R": .0,
            "P": .0,
            "Y": .0,
            "gripper": 0, # 0 表示没有动作，1 表示打开夹爪，-1 表示关闭夹爪
        }
        return incr
    
    def add_key(self, key: str):
        if key not in self.pressed_keys:
            self.pressed_keys.add(key)
            # print(f"key add {key}")
            # pressed_keys={'D', 'W'}
        self.set_ctl_cmd(str(list(self.pressed_keys)))
        
    
    def remove_key(self, key: str):
        self.pressed_keys.discard(key)
        self.set_ctl_cmd(str(list(self.pressed_keys)))
        
    
    def get_cmd(self, key: str):
        # +x, -x, ...
        if key in self.kb_mapp.inverse.keys():
            cmd = self.kb_mapp.inverse[key]
            return cmd
        return ""
        

    def keyPressEvent(self, event: qtbase.QKeyEvent):
        """按下按键：键盘打开 caps lock 模式，可以实现长按模式
        （即按住 A，只会触发一次 keyPressEvent，不会连续触发，松开也是只触发一次）
        - 键盘长按会在第一次 isAutoRepeat=False, 之后是 True
        """
        if not event.isAutoRepeat():
            key = event.text().upper()
            self.add_key(key)

            if self.VERBOSE:
                print(f"keyPressEvent {event}")
            
            incr = self.get_empty_incr()
            
            # 遍历当前按下的按键
            for key in self.pressed_keys:
                # 如果当前按下的按键已经绑定
                cmd = self.get_cmd(key)
                
                if cmd == "gripper":
                    self.set_gripper()
                    return super().keyPressEvent(event)
                
                elif cmd == "collect":
                    self.kb_collect()
                    return super().keyPressEvent(event)
                
                elif cmd == "goto_init_pos":
                    self.add_log("G：回到初始位置")
                    if not self.is_going_to_init_pos:
                        self.add_log("正在回到初始位置中...")
                        self.is_going_to_init_pos = 1
                        self.arm.goto_init_pos()
                        self.is_going_to_init_pos = 0
                        self.add_log("机械臂已归位！")
                    return super().keyPressEvent(event)
                
                elif "+" in cmd or "-" in cmd:
                    self.cmd2incr(incr, cmd)
                    SharedData.incr.update(incr)
                else:
                    print(f"未定义 {key}")
            
            # 所有按键的数据都已同步
            incr.update({
                "duration": self.max_duration,
                "is_async": 1,
            })
            
            if self.VERBOSE:
                print(f"{get_time_str(4)} keyPressEvent", incr)
            
            # patch
            # if SharedData.keyboard_incr_bak != SharedData.keyboard_incr:
                #print("-"*50)
                #print("incr_bak", SharedData.keyboard_incr_bak)
                #print("incr", SharedData.keyboard_incr)
                #self.arm.cartesian_velocity_control(data)
                # SharedData.keyboard_incr_bak.update(SharedData.keyboard_incr)
            self.arm.cartesian_velocity_control(incr)

        return super().keyPressEvent(event)
    
    
    def keyReleaseEvent(self, event):
        """松开按键"""
        if not self.is_keyboard_ctrl:
            return
        
        if not event.isAutoRepeat():
            key = event.text().upper()
            if self.VERBOSE:
                print(f"keyReleaseEvent {event}")
            self.remove_key(key)
            cmd = self.get_cmd(key)
            if cmd == "goto_init_pos":
                print("松开 G：直接返回，不需要 stop_motion")
                return
            
            incr = self.get_empty_incr()
            # 遍历当前按下的按键
            for key in self.pressed_keys:
                # 如果当前按下的按键已经绑定
                cmd = self.get_cmd(key)
                if "+" in cmd or "-" in cmd:
                    self.cmd2incr(incr, cmd)
                    SharedData.incr.update(incr)
                else:
                    print(f"未定义 {key}")
            
            # 所有按键的数据都已同步
            incr.update({
                "duration": self.max_duration,
                "is_async": 1,
            })
            SharedData.incr.update(incr)
            # if self.VERBOSE:
            #     print(f"{get_time_str(4)} keyReleaseEvent", data)
            
            if len(self.pressed_keys) == 0:
                if self.VERBOSE:
                    print(f"{get_time_str(4)} 无按键，停止运动")
                self.arm.stop_cartesian_velocity_control()
            else:
                self.arm.cartesian_velocity_control(incr)
        # return super().keyPressEvent(event)

    def set_ctl_cmd(self, cmd: str):
        self.ui.ctl_state.setText(cmd)
        # res = api.set_data("ctl", cmd)
    
    def set_op_cmd(self, cmd: str):
        self.ui.ctl_state.setText(cmd)
        # res = api.set_data("op", cmd)

    def get_obs(self, frames: dict):
        self.pix_left = qtbase.QPixmap(qtbase.cv2qt(frames['v1']))
        self.pix_right = qtbase.QPixmap(qtbase.cv2qt(frames['v2']))

    def paintEvent(self, event: qtbase.QtGui.QPaintEvent) -> None:
        """图像显示区支持自适应缩放"""
        ui = self.ui
        self._resize_and_scaled(ui.lb_left, ui.wd_left, self.pix_left)
        self._resize_and_scaled(ui.lb_right, ui.wd_right, self.pix_right)
        return super().paintEvent(event)

    def close_ready(self):
        ...
    
    
def main():
    qapp = qtbase.QApplication(sys.argv)
    # 设置全局默认字体
    qapp.setFont(qtbase.QFont("微软雅黑", 11))
    mapp = MainWindow()
    mapp.show()
    sys.exit(qapp.exec())
