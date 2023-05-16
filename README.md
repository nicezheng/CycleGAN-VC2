# **CycleGAN-VC2-PyTorch**
## Task 

Transform my voice into Jay Chou's voice with CycleGan-v2

## Model 

[CycleGAN-VC2: Improved CycleGAN-based Non-parallel Voice Conversion](https://arxiv.org/abs/1904.04631])

## Dataset
1. `data/jz/*.wav`: 115 my sound file
2. `data/jay/*.wav`: 149 Jay Chou's sound file

## Usage
1. Preprocess audio:
```python
python preprocess_training.py
```
2. Train Model
```python
python train.py
```
3. Inference
```python
python test.py
```


Refer:
**https://github.com/jackaduma/CycleGAN-VC2**