# Low-Light Object Tracking: A Benchmark

## Overview

[Paper](https://arxiv.org/abs/2408.11463) |[Checkpoints](https://pan.baidu.com/s/1IrDzrDt5Zt_L15Ll1lEG1Q?pwd=y3pk)| [LLOT benchmark（baidu）](https://pan.baidu.com/s/1CQprKcCDTRoEE9xs1690sg?pwd=fbkd)| [LLOT benchmark（google-0）](https://drive.google.com/drive/folders/1zvM7th-2q3NLXSFiLIM1cxVE-ogX1qeC?usp=drive_link)| [LLOT benchmark（google-1）](https://drive.google.com/drive/folders/12UZDYVIq-9bCdPMpB6YE49Z3kD52n4li?usp=drive_link)

### Install the environment

Our implementation is based on PyTorch 1.10.1+CUDA11.3. Use the following command to install the runtime environment:

```bash
conda env create -f HIPTrack_env_cuda113.yaml
```



### Set project paths

Run the following command to set paths for this project

```bash
python3 tracking/create_default_local_file.py --workspace_dir . --data_dir ./data --save_dir ./output
```

After running this command, you can also modify paths by editing these two files

```bash
lib/train/admin/local.py  # paths about training
lib/test/evaluation/local.py  # paths about testing
```



### Training

- For training on datasets except GOT-10k.

  Download pre-trained [DropTrack/DCPT weights](https:) and put it under `$PROJECT_ROOT$/pretrained_models`.

  ```bash
  python3 tracking/train.py --script hiptrack --config hiptrack --save_dir ./output --mode multiple --nproc_per_node 4
  ```

- For training on GOT-10k.

  Download pre-trained [DropTrack/DCPT weights](https:) and put it under `$PROJECT_ROOT$/pretrained_models`.

  ```bash
  python3 tracking/train.py --script hiptrack --config hiptrack_got --save_dir ./output --mode multiple --nproc_per_node 4
  ```



### Evaluation

Change the dataset path in `lib/test/evaluation/local.py` to your storage path.

- LaSOT/LLOT or other off-line evaluated benchmarks (modify `--dataset` correspondingly)

```bash
python3 tracking/test.py hiptrack hiptrack --dataset lasot --threads 1 --num_gpus 1
python3 tracking/analysis_results.py # need to modify tracker configs and names
```

- GOT10K-test

```bash
python3 tracking/test.py hiptrack hiptrack_got --dataset got10k_test --threads 1 --num_gpus 1
python3 lib/test/utils/transform_got10k.py --tracker_name hiptrack --cfg_name hiptrack_got
```

- TrackingNet

```bash
python3 tracking/test.py hiptrack hiptrack --dataset trackingnet --threads 1 --num_gpus 1
python3 lib/test/utils/transform_trackingnet.py --tracker_name hiptrack --cfg_name hiptrack
```



The current repository contains an experimental version of the code, which is directly developed based on the HIPTrack framework.Some classes, functions, and file paths still retain the original HIPTrack naming and have not yet been uniformly updated to our algorithm’s name, H-DCPT. A fully organized and renamed version of the code will be released later.



## Citing H-DCPT

```
@article{zhong2025low,
  title={Low-light object tracking: A benchmark},
  author={Zhong, Pengzhi and Guo, Xiaoyu and Huang, Defeng and Peng, Xiaojun and Li, Yian and Zhao, Qijun and Li, Shuiwang},
  journal={IEEE Transactions on Intelligent Vehicles},
  year={2025},
  publisher={IEEE}
}
```

