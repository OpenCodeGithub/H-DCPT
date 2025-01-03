class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/pretrained_networks'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/vid'
        self.imagenet_lmdb_dir = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
        self.lasot_dir = '/home/lsw/data/lasot'
        self.got10k_dir = '/home/lsw/data/got10k/train'
        self.got10k_val_dir = '/home/lsw/data/got10k/val'
        self.lasot_lmdb_dir = '/home/lsw/data/lasot_lmdb'
        self.got10k_lmdb_dir = '/home/lsw/data/got10k_lmdb'
        self.trackingnet_dir = '/home/lsw/data/trackingnet'
        self.trackingnet_lmdb_dir = '/home/lsw/data/trackingnet_lmdb'
        self.coco_dir = '/home/lsw/data/coco'
        self.coco_lmdb_dir = '/home/lsw/data/coco_lmdb'
