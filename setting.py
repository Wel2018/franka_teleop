import math

from toolbox.core.file_op import yaml_load, yaml_save
from . import AppConfig, logger, VERBOSE, THREAD_DEBUG, APPCFG
from .ui.ui_setting import Ui_SettingWindow
from toolbox.qt import qtbase
from toolbox.robot.unit_converter import RobotUnitConverter


pose_keys = ['x', 'y', 'z', 'R', 'P', 'Y']
joint_keys = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7']


class SettingWindow(qtbase.IMainWindow):
    """设置页"""


    def __init__(self, parent = None):
        ui = self.ui = Ui_SettingWindow()
        super().__init__(ui, parent)

        # only=['add_x', 'sub_x', ...]
        only = []
        for k in pose_keys:
            only.append(f'add_{k}')
            only.append(f'sub_{k}')
        only.append("gripper")

        self.init(
            "isaac_demo_setting",
            "设置",
            only=only
        )

        from bidict import bidict
        self.keyboard_mapp = bidict({
            # 位置
            "+x": "w",
            "-x": "s",
            "+y": "a",
            "-y": "d",
            "+z": "q",
            "-z": "z",
            # 姿态
            "+R": "u",
            "-R": "j",
            "+P": "i",
            "-P": "k",
            "+Y": "o",
            "-Y": "l",
            # 其他
            "gripper": "p",
            "collect": "B",
            "goto_init_pos": "G",
        })
        self.curr = {}
        

        self.bind_clicked(ui.btn_sync_sim, self.sync_sim)
        self.bind_clicked(ui.btn_sync_real, self.sync_real)
        self.bind_clicked(ui.btn_get_real, self.get_real)
        self.bind_clicked(ui.btn_set_default, self.set_default)
        self.bind_clicked(ui.btn_save_default, self.save_default)
        self.bind_clicked(ui.btn_apply, self.apply)
        self.bind_shotcut()


        def keyPressEvent(arg__1: qtbase.QKeyEvent, line_edit: qtbase.QLineEdit):
            event = arg__1
            # 获取修饰键和主键
            modifiers = event.modifiers().value
            key = event.key()

            # 忽略无效按键（如单独按下修饰键）
            if key in (
                qtbase.Qt.Key.Key_Control, 
                qtbase.Qt.Key.Key_Shift, 
                qtbase.Qt.Key.Key_Alt, 
                qtbase.Qt.Key.Key_Meta,
                qtbase.Qt.Key.Key_Escape):
                return

            # 组合修饰键和主键
            combined_key = int(modifiers) | int(key)
            fmt = qtbase.QKeySequence.SequenceFormat.NativeText
            shortcut = qtbase.QKeySequence(combined_key).toString(fmt)

            # 设置到输入框
            line_edit.setText(shortcut)

            # 阻止默认行为
            event.accept()
        
        # 动态绑定
        for line_edit in [
            ui.add_x, ui.sub_x,
            ui.add_y, ui.sub_y,
            ui.add_z, ui.sub_z,
            ui.add_R, ui.sub_R,
            ui.add_P, ui.sub_P,
            ui.add_Y, ui.sub_Y,
            ui.gripper,
        ]:
            def _keyPressEvent(arg__1: qtbase.QKeyEvent, line_edit=line_edit):
                return keyPressEvent(arg__1, line_edit)
            line_edit.keyPressEvent = _keyPressEvent
    

    def save_default(self):
        yaml_save(self.curr, "tmp/isaac_demo_setting_default.yaml")
        logger.info(f"保存默认状态 {self.curr}")

    def set_default(self):
        ui = self.ui
        self.curr = yaml_load("tmp/isaac_demo_setting_default.yaml")
        logger.info(f"使用默认状态 {self.curr}")
        for k in self.curr.keys(): # type: ignore
            el = getattr(ui, k, None)
            if el is not None:
                el.setValue(self.curr[k]) # type: ignore

    def bind_shotcut(self):
        ui = self.ui
        # 快捷键 --------------------
        # key=x, y, z，获取对应的 add_x，add_y 的快捷键内容保存到 mapp 中
        for key in pose_keys:
            el = getattr(ui, f"add_{key}")
            self.keyboard_mapp[f'+{key}'] = el.text() # type: ignore
            el = getattr(ui, f"sub_{key}")
            self.keyboard_mapp[f'-{key}'] = el.text() # type: ignore
        logger.info(f"绑定快捷键 {self.keyboard_mapp}")
        # 其他 -----------------------
        self.keyboard_mapp['gripper'] = ui.gripper.text() # type: ignore


    def get_real(self):
        ui = self.ui
        # curr = robot.get_curr()
        # logger.info(f"获取物理机状态 {curr}")

        # for k in curr.keys():
        #     el = getattr(ui, k, None)
        #     if el is not None:
        #         el.setValue(curr[k])
        # self.curr = curr
    

    def fetch_ui(self):
        ui = self.ui
        # 同步 ------------------
        joints = [
            ui.j1.value(),
            ui.j2.value(),
            ui.j3.value(),
            ui.j4.value(),
            ui.j5.value(),
            ui.j6.value(),
        ]
        
        pose = [
            ui.x.value(),
            ui.y.value(),
            ui.z.value(),
            ui.R.value(),
            ui.P.value(),
            ui.Y.value(),
        ]

        x,y,z = pose[:3]
        R,P,Y = pose[3],pose[4],pose[5]
        rx,ry,rz,rw = RobotUnitConverter.euler2quat([R,P,Y])
        j1, j2, j3, j4, j5, j6 = joints
        joints_degree = [math.degrees(angle) for angle in joints]

        return {
            'x': x,
            'y': y,
            'z': z,
            'R': R,
            'P': P,
            'Y': Y,
            'rx': rx,
            'ry': ry,
            'rz': rz,
            'rw': rw,
            'j1': j1,
            'j2': j2,
            'j3': j3,
            'j4': j4,
            'j5': j5,
            'j6': j6,
            'joints': joints,
            'joints_degree': joints_degree,
            'xyzRPY': [x, y, z, R, P, Y],
            # 同步
            "rm_joint": joints,
            "rm_pos": [x,y,z, rx,ry,rz,rw],
        }


    def sync_sim(self):
        """同步到虚拟环境"""
        data = self.fetch_ui()
        json={
            "op": "init",
            "rm_joint": data['rm_joint'],
            "rm_pos": data['rm_pos'],
        }
        # res = api.set_data_json(json)
        # logger.info(f"同步到虚拟环境 {json} {res}")


    def sync_real(self):
        """同步到真实环境"""
        data = self.fetch_ui()
        # res = robot.plan(data['joints_degree'], is_first=1)
        # logger.info(f"同步到真实环境 {data} {res}")

    def close_ready(self):
        self.apply()

    def apply(self):
        self.bind_shotcut()
