# Low-Light Object Tracking: A Benchmark

## Overview

[Paper](https://arxiv.org/abs/2408.11463) | [LLOT benchmark](https://pan.baidu.com/s/1NvLQYoDFZgvMA0Jnq6YUkA?pwd=exyr)

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







## Citing H-DCPT

```
@article{zhong2024low,
  title={Low-Light Object Tracking: A Benchmark},
  author={Zhong, Pengzhi and Guo, Xiaoyu and Huang, Defeng and Peng, Xiaojun and Li, Yian and Zhao, Qijun and Li, Shuiwang},
  journal={arXiv preprint arXiv:2408.11463},
  year={2024}
}
```

