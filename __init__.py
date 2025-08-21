"""睿尔曼模仿学习客户端"""

from toolbox.qt import qtbase
from toolbox.core.logbase import get_logger


q_appcfg = qtbase.QAppConfig(
    name = "Franka 遥操作数据采集程序",
    name_en = "Franka Teleop",
    date="2025-08-21",
    version = "1.3.0",
    fontsize = 14,
    slot="franka_teleop",
    APPCFG_DICT=qtbase.get_appcfg(__file__),
)

print(f"q_appcfg={q_appcfg}")
logger = get_logger(q_appcfg.slot)
