import pickle
import timeit

import cv2
import numpy as np

from toolbox.robot.franka_arm_client import FrankaArmClient
from toolbox.robot.hdf5_dataset_op import DemoLoader
from .. import APPCFG


def test_load_pickle():
    # 测试加载 pickle 文件
    with open("tmp/data/demo_20250428_143547.pkl", "rb") as f:
        data = pickle.load(f)
        print(data.keys())
        print(data['color'][0].shape)
        print(data['depth'][0].shape)
        print(data['pointcloud'][0].shape)
        print(data['agent_pos'][0].shape)
        print(data['action'][0].shape)
        print(data['action'][0])


def test_get_latest_hdf5_file():
    directory = "tmp/data"
    file = DemoLoader.get_latest_file(directory)
    print(file)


def test_load_hdf5():
    filepath = DemoLoader.get_latest_file("tmp/data")
    print(f"加载文件 {filepath}")
    #filepath = "tmp/data.old/40.hdf5"
    slow_speed = 5
    fast_speed = 20
    speed = fast_speed
    demo_loader = DemoLoader()
    demo_loader.SHOW_PC = 1 # type: ignore
    demo_loader.load_hdf5(filepath, "VA")
    demo_loader.vis(fps=speed)
    bname = DemoLoader.basebaname(filepath)
    demo_loader.export_video(f"tmp/vis_{bname}.mp4", export_vis=1)


# 轨迹复现
def test_replay():
    arm = FrankaArmClient()
    arm.goto_init_pos()
    # cam: OrbbecCamera | RealsenseCamera
    
    cam_type = APPCFG['cam_type']

    if cam_type == "realsense":
        from toolbox.cam3d.cam3d_realsense import RealsenseCameraDual
        cam = rs_cam = RealsenseCameraDual()
    else:
        from toolbox.cam3d.cam3d_orbbec import OrbbecCamera # type: ignore
        cam = orbbec_cam = OrbbecCamera()

    # mode = "VA" if isinstance(cam, OrbbecCamera) else "VLA"
    mode = "VA" if cam_type == "orbbec" else "VLA"

    # files = glob.glob("tmp/data/*.hdf5")
    # filepath = files[0]
    filepath = DemoLoader.get_latest_file("tmp/data")
    print(f"加载文件 {filepath}")

    demo_loader = DemoLoader()
    demo_loader.load_hdf5(filepath, mode)
    demo_loader.SHOW_DEPTH = 0
    demo_loader.SHOW_PC = 0

    for i in range(demo_loader.steps):
        # 可视化数据集内容
        demo_loader.vis_step(i)

        # 实时可视化
        frames = cam.read(
            is_sync=1, is_bgr=1, 
            read_color=1, 
            read_depth=demo_loader.SHOW_DEPTH, 
            read_pc=demo_loader.SHOW_PC)
        
        if mode == "VLA":
            color_static = frames['color_static']
            color_gripper = frames['color_gripper']
            color = np.hstack((color_static, color_gripper))
            cv2.imshow("Realtime Camera", color)
            cv2.waitKey(1)
        else:
            color = frames['color']
            #depth = depth2color(frames['depth'])
            #cv2.imshow("Realtime Camera", np.hstack((color, depth)))
            cv2.imshow("Realtime Camera", color)
            cv2.waitKey(1)


        # 机械臂状态
        t1 = timeit.default_timer()
        print("-"*50)
        print(f"step {i}")
        joint = demo_loader.get_joint(i)
        gripper = demo_loader.get_gripper(i)
        action = demo_loader.get_action_ee(i)
        print(f"joint={joint} gripper={gripper}")
        print(f"action={action}")
        agent_pos = joint.tolist() + [float(gripper)] # type: ignore
        arm.step(agent_pos, intv=0.05)
        t = round((timeit.default_timer() - t1)*1000, 2)
        print(f"{t} ms")
        
        cv2.waitKey(1000//30)
