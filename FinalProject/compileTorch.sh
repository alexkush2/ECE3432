#!/bin/bash

sudo apt update
sudo apt install libopenblas-dev libblas-dev m4 cmake cython python3-dev python3-yaml python3-setuptools

mkdir /usr/src/pytorch_install && cd /usr/src/pytorch_install
git clone --recursive https://github.com/pytorch/pytorch
cd pytorch

export NO_CUDA=1
export NO_DISTRIBUTED=1
export NO_MKLDNN=1 
export NO_NNPACK=1
export NO_QNNPACK=1

python3 setup.py build

sudo -E python3 setup.py install