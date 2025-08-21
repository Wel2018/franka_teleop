from . import logger
from .ui.ui_setting import Ui_SettingWindow
from toolbox.qt import qtbase


class SettingWindow(qtbase.QApp):
    """设置页"""

    def pre_init(self):
        self.pose_keys = ['x', 'y', 'z', 'R', 'P', 'Y']
        self.joint_keys = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7']
        self.apptitle = "设置"
        self.slot = "franka_teleop_setting"
        self.fontsize = self.q_parent.fontsize # type: ignore
        
        # only=['add_x', 'sub_x', ...]
        only = []
        for k in self.pose_keys:
            only.append(f'add_{k}')
            only.append(f'sub_{k}')
        only.append("gripper")
        self.only = only
    
    def post_init(self):
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
        
        ui = self.ui
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

    
    def __init__(self, parent = None):
        ui = self.ui = Ui_SettingWindow()
        super().__init__(ui, parent)
        self.pre_init()
        self.init(only=self.only)
        self.post_init()

    def bind_shotcut(self):
        ui = self.ui
        # 快捷键 --------------------
        # key=x, y, z，获取对应的 add_x，add_y 的快捷键内容保存到 mapp 中
        for key in self.pose_keys:
            el = getattr(ui, f"add_{key}")
            self.keyboard_mapp[f'+{key}'] = el.text() # type: ignore
            el = getattr(ui, f"sub_{key}")
            self.keyboard_mapp[f'-{key}'] = el.text() # type: ignore
        logger.info(f"绑定快捷键 {self.keyboard_mapp}")
        # 其他 -----------------------
        self.keyboard_mapp['gripper'] = ui.gripper.text() # type: ignore

    def close_ready(self):
        self.apply()

    def apply(self):
        self.bind_shotcut()
