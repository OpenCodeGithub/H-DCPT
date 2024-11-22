from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/home/lsw/data/got10k_lmdb'
    settings.got10k_path = '/home/lsw/data/GOT-10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.itb_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/itb'
    settings.lasot_extension_subset_path_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/lasot_extension_subset'
    settings.lasot_lmdb_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/lasot_lmdb'
    settings.lasot_path = '/media/lsw/data4/LaSOT/zip'
    settings.network_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/output/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/nfs'
    settings.otb_path = '/media/lsw/data/LLOT/LLOT'
    settings.prj_dir = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT'
    settings.result_plot_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/output/test/result_plots'
    settings.results_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/output'
    settings.segmentation_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/output/test/segmentation_results'
    settings.tc128_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/tnl2k'
    settings.tpl_path = ''
    settings.trackingnet_path = '/media/lsw/data4/trackingnet'
    settings.uav_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/uav'
    settings.vot18_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/vot2018'
    settings.vot22_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/vot2022'
    settings.vot_path = '/home/lsw/PycharmProjects/HIPTrack_Re/H-DCPT/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

