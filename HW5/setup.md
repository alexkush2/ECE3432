## Racecar project
This can control the car over wifi using ROS
### Setup workspace and package
'''
./HW5_Setup.sh
'''
### To Run Program
On talker PC run 
'''
roscore
'''
Then in another terminal run
'''
./talkerPi.py
'''

On listener PC run
'''
export ROS_MASTER_URI:<hostIP>:11311
export ROS_IP:<clientIP>
./listenerPi.py
'''
