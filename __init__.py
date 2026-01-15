"""睿尔曼模仿学习客户端"""

from toolbox.qt import qtbase
from .version import __version__
from .version import __update_timestamp__


q_appcfg = qtbase.QAppConfig(
    name = "Franka 遥操作数据采集程序",
    name_en = "Franka Teleop",
    date=__update_timestamp__,
    version = __version__,
    fontsize = 14,
    slot="franka_teleop",
    APPCFG_DICT=qtbase.get_appcfg(__file__),
)
