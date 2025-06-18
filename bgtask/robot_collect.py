from toolbox.qt import qtbase
from rich import print
from toolbox.cam3d.cam3d_base import Camera3DBase
from toolbox.robot.franka_arm_client import FrankaArmClient
from toolbox.robot.hdf5_dataset_op import DemoCreator, DemoLoader
from .. import THREAD_DEBUG, VERBOSE, APPCFG

import numpy as np
np.set_printoptions(precision=3, suppress=True)


IDLE_MS = 3
FPS = 60


#######################################################################################

class RobotCollect(qtbase.QAsyncTask):
    """数据采集并保存到本地，按照日期时间命名文件夹"""
    REC_WHEN_INCR = 0  # 当有增量时记录
    is_debug = 0

    def __init__(self, shared_data, cam: Camera3DBase, arm: FrankaArmClient, fps=FPS, conf={}):
        super().__init__(conf)
        self.is_run = 1
        self.fps: int = fps
        self.cam: Camera3DBase = cam
        self.arm: FrankaArmClient = arm
        self.incr: dict = shared_data.incr
        self.ee_bak = [0.0]*6
        self.j_bak = [0.0]*7
        
    #@benchmark(bool(1))
    def add_step_ob(self, ds: DemoCreator):
        """添加一个时间步的数据"""
        joint = self.arm.joints()
        gripper = self.arm.gripper()
        ee = self.arm.ee()

        #@benchmark(1)
        def calc_ee_err(e1: list, e2: list):
            # 函数 calc_ee_err 执行耗时: 0.025 ms
            e1 = np.array(e1) # type: ignore
            e2 = np.array(e2) # type: ignore
            return np.linalg.norm(e1 - e2) # type: ignore
           
        #if self.ee_bak == ee:
        if calc_ee_err(self.ee_bak, ee) < 0.001: # type: ignore
            if VERBOSE:
                print(f"帧 {self.frame_idx} 重复")
            self.msleep(IDLE_MS)
            return
        
        self.ee_bak = ee
        
        print(f"i={self.frame_idx} end: {ee} Gripper：{gripper}")
        # agent_pos = np.array(joints + [gripper]) # type: ignore
        self.frame_idx += 1
        
        # 图像数据
        cam = self.cam
        # if isinstance(cam, OrbbecCamera):
        if APPCFG['cam_type'] == "orbbec":
            cam_data= cam.read(is_sync=1, is_bgr=0, read_depth=1)
            #cam_data = self.cam_th.cam_data
            color = cam_data['color']
            depth = cam_data['depth']
            pointcloud = cam_data['pointcloud']
            print(f"i={self.frame_idx} color={color.shape}, depth={depth.shape}")

            # 重获取（图像读取会有 30ms 的延迟）
            joint = self.arm.joints()
            gripper = self.arm.gripper()
            ee = self.arm.ee()

            ds.add_step_ob(
                color=color.copy(), 
                depth=depth.copy(), 
                pointcloud=pointcloud.copy(),
                joint=joint, ee=ee, gripper=gripper)
        
        # elif isinstance(cam, RealsenseCameraDual):
        elif APPCFG['cam_type'] == "realsense":
            cam_data= self.cam.read(is_sync=1, is_bgr=0)
            #cam_data = self.cam_th.cam_data
            color_static = cam_data['color_static']
            color_gripper = cam_data['color_gripper']
            depth_static = cam_data['depth_static']
            depth_gripper = cam_data['depth_gripper']
            depth_static_colorized = cam_data['depth_static_colorized']
            depth_gripper_colorized = cam_data['depth_gripper_colorized']
            
            print(f"color static={color_static.shape}, gripper={color_gripper.shape}")
            print(f"depth static={depth_static.shape}, gripper={depth_gripper.shape}")

            # 重获取（图像读取会有 30ms 的延迟）
            joint = self.arm.joints()
            gripper = self.arm.gripper()
            ee = self.arm.ee()
            
            ds.add_step_ob(
                color_static=color_static, 
                color_gripper=color_gripper, 
                depth_static=depth_static, 
                depth_gripper=depth_gripper,
                depth_static_colorized=depth_static_colorized, 
                depth_gripper_colorized=depth_gripper_colorized,
                joint=joint, ee=ee, gripper=gripper)
        
        else:
            raise NotImplementedError

    
    def has_incr(self):
        for k in ['x', 'y', 'z', 'R', 'P', 'Y']:
            if self.incr[k] != 0:
                return True
        return False

    @qtbase.enable_debugpy(THREAD_DEBUG)
    def run(self):
        self.is_run = 1
        self.frame_idx = 0
        self.add_log("开始收集数据...")
        # mode = "VLA" if isinstance(self.cam, RealsenseCameraDual) else "VA"
        mode = "VLA" if APPCFG['cam_type'] == "realsense" else "VA"
        ds = DemoCreator("tmp/data", mode=mode)
        ds.create_demo()
        
        while self.is_run:
            if self.REC_WHEN_INCR and self.has_incr():
                print("-"*50)
                self.add_step_ob(ds)
                continue

            if not self.REC_WHEN_INCR:
                # 测试：开启数据录制模式就直接采集，不等待键盘输入
                self.add_step_ob(ds)
                continue

            intv = 1000 // self.fps
            self.msleep(intv)
        # end while

        ds.save_demo(use_hdf5=1)
        self.add_log(f"保存完成（时间步={ds.cur_demo_step}")

    def clean(self):
        self.ee_bak = [0.0]*6
        self.j_bak = [0.0]*7
    
    def add_log(self, msg):
        #print(msg)
        self.sig_msg.emit(msg)
