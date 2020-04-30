#!/bin/bash

pip3 install cython pandas numpy future pillow

wget https://github.com/lbaitemple/ubuntu_server_rpi/raw/master/torch/torch-1.6.0a0%2B521910e-cp36-cp36m-linux_armv7l.whl
pip3 install torch-1.6.0a0+521910e-cp36-cp36m-linux_armv7l.whl

wget https://github.com/lbaitemple/ubuntu_server_rpi/raw/master/torch/torchvision-0.7.0a0%2Bfed843d-cp36-cp36m-linux_armv7l.whl
pip3 install torchvision-0.7.0a0+fed843d-cp36-cp36m-linux_armv7l.whl

 

# sudo apt install libopenblas-dev libblas-dev m4 cmake cython python3-dev python3-yaml python3-setuptools