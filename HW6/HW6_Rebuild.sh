#!/bin/zsh

cd ~/
source /opt/ros/melodic/setup.zsh

cd ~/catkin_ws/
#catkin_make
source devel/setup.zsh
cd ~/catkin_ws
catkin_make
. ~/catkin_ws/devel/setup.zsh
roscd racecar

cd scripts
cp ~/ECE3432/HW6/talker.py ~/catkin_ws/src/racecar/scripts
#wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
chmod +x talker.py
roscd racecar/scripts/
#wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py
cp ~/ECE3432/HW6/listener.py ~/catkin_ws/src/racecar/scripts
chmod +x listener.py
cd ~/catkin_ws
catkin_make

rosparam set joy_node/dev "/dev/input/js0" 