# Franka 遥操作数据采集

用于 **视觉驱动的模仿学习算法** 的数据采集，主要针对 Franka 机械臂和 realsense, Orbbec 深度相机设计，后端使用 [franka_server](https://github.com/Wel2018/franka_server)。


## 功能特性

- 键盘模式支持同时多按键采集
- 支持调整机械臂移动时关节的线速度和角速度
- 支持自定义快捷键
- 支持 SpaceMouse 的自定义按键和摇杆控制
- 支持保存到 `HDF5`, `zarr` 格式
- 支持数据集后处理


## 支持设备

- 机械臂
  - Franka Research 3
  - Realman 65B
  - Jaka
- 摄像头
  - Realsense L515
  - Realsense D435
  - Realsense D405
  - Orbbec Femto Bolt

## 主界面

![ui](docs/ui.png)

## 环境配置

```sh
# 1、安装机器人工具箱
pip install ./wk_robot_toolbox-*.tar.gz

# 2、安装依赖
pip install -r requirements.txt

# 3、启动主程序
python -m franka_teleop
```

## TODO

- [ ] iPhone 陀螺仪控制
- [ ] 艾欧智能的遥操作设备控制
