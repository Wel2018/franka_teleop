"""睿尔曼模仿学习客户端"""
import os
from toolbox.qt import qtbase
from toolbox.core.logbase import get_logger
from toolbox.core.file_op import yaml_load


AppConfig = qtbase.QAppConfig(
    name = "Franka 遥操作数据采集程序",
    name_en = "Franka Teleop",
    date="2025-07-02",
    version = "1.0.1",
    fontsize = 14
)
print(f"AppConfig={AppConfig}")


# 配置 -----------------------------------------------------------
logger = get_logger(prefix="", name="franka_teleop")
cur_dir = os.path.dirname(os.path.abspath(__file__))
APPCFG = yaml_load(f"{cur_dir}/appcfg.yaml")
print(f"APPCFG={APPCFG}")
THREAD_DEBUG = APPCFG['THREAD_DEBUG']
VERBOSE = APPCFG['VERBOSE']
BENCHMARK = APPCFG['BENCHMARK']
