#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import sys
# used Float32 as datatype so that it can contain a fractional value for the dutycycle

def talker():    
    # create two plublish things for steering and throttle
    pubSteer = rospy.Publisher('steer', Float32, queue_size=10)
    pubThrottle = rospy.Publisher('throttle', Float32, queue_size=10)

    # start ros node
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        steer = float(sys.argv[2])
        throttle = float(sys.argv[1])
        rospy.loginfo(steer)
        pubSteer.publish(steer)
        rospy.loginfo(throttle)
        pubThrottle.publish(throttle)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
