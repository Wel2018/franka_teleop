"""睿尔曼模仿学习客户端"""

from toolbox.qt import qtbase
from toolbox.core.logbase import get_logger
APPCFG = qtbase.get_appcfg(__file__)


AppConfig = qtbase.QAppConfig(
    name = "Franka 遥操作数据采集程序",
    name_en = "Franka Teleop",
    date="2025-07-11",
    version = "1.2.0",
    fontsize = 14,
    slot="franka_teleop",
    appcfg=APPCFG,
)

print(f"AppConfig={AppConfig}")
logger = get_logger(AppConfig.slot)
