#!/bin/zsh

export ROS_IP=192.168.1.108
export ROS_MASTER_URI=http://192.168.1.108:11311

chmod +x listener.py
. ~/ECE3432/HW5/listener.py
