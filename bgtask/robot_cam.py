from toolbox.qt import qtbase
from toolbox.cam3d.cam3d_base import get_zero_img
from toolbox.cam3d.cam3d_base import Camera3DBase
from .. import THREAD_DEBUG, VERBOSE, APPCFG

zero_img = get_zero_img()
##########################################


class IRobotCamTask(qtbase.QAsyncTask):
    """适配虚拟环境和真实环境的相机接口
    """
    INTV_MS = 10 # ms

    def __init__(self, conf: dict = {}) -> None:
        super().__init__()
        self.is_run = 0
        self.intv = self.INTV_MS # ms
        self.cam_frames = {}
        self.cam_data = {}
        self.conf = conf
    
    def pull_data(self):
        raise NotImplementedError

    def push_data(self):
        cam_frames = self.cam_frames
        if cam_frames['ret']:
            self.sig_data.emit(cam_frames)

    @qtbase.enable_debugpy(THREAD_DEBUG)
    def run(self):
        self.is_run = 1
        while self.is_run:
            self.pull_data()
            self.push_data()
            #self.msleep(self.intv)
        # end while
    
    def stop(self):
        self.is_run = 0
        self.msleep(50)


class Camera3DWrapper():
    is_debug = 0

    def __init__(self, cam: Camera3DBase, is_sync=0):
        self.frames = {
            "ret": 0,
            "v1": zero_img,
            "v2": zero_img,
        }
        self.cam = cam
        self.cam_data = {}
        self.is_sync = is_sync

    def read(self):
        is_sync = self.is_sync
        # if isinstance(self.cam, OrbbecCamera):
        if APPCFG['cam_type'] == "orbbec":
            data = self.cam.read(is_sync=is_sync, is_bgr=0, read_pc=1, read_depth=1)
            self.cam_data.update(data)
            self.frames['ret'] = 1
            self.frames['v1'] = data['color']
            self.frames['v2'] = data['depth_img']
            return self.frames
            
        # elif isinstance(self.cam, RealsenseCameraDual):
        elif APPCFG['cam_type'] == "realsense":
            data = self.cam.read(is_sync=is_sync, is_bgr=0, read_pc=0)
            self.cam_data.update(data)
            self.frames['ret'] = 1
            self.frames['v1'] = data['color_static']
            self.frames['v2'] = data['color_gripper']
            return self.frames
        
        else:
            raise NotImplementedError
        

    def stop(self):
        self.cam.stop()


class RobotCamTask(IRobotCamTask):
    """机器人本地摄像头"""

    def __init__(self, cam: Camera3DBase, conf={}) -> None:
        super().__init__(conf)
        self.cam = cam
        self.local_cam = Camera3DWrapper(cam)
        self.cam_frames = self.local_cam.frames
        self.cam_data = self.local_cam.cam_data

    def pull_data(self):
        self.local_cam.read()
    
    def stop(self):
        self.is_run = 0
        self.msleep(50)
        self.local_cam.stop()
        self.msleep(50)
