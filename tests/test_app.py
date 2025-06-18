from toolbox.qt import qtbase
from ..setting import SettingWindow


def test_franka_teleop_setting():
    # shared.init()
    # mp.freeze_support()
    qapp = qtbase.get_qapp()
    mapp = SettingWindow()
    mapp.show()
    mapp.activateWindow()
    qapp.exec()
