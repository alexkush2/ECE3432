#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from rpiHAT import ServoNT
import time
# used Float32 as datatype so that it can contain a fractional value for the dutycycle

s=ServoNT(channel=1, freq=94.5)
t=ServoNT(channel=2, freq=94.5)

def callbackSteer(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard steer %f', data.data)
    s.pulse(float(data.data))

def callbackThrottle(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard throttle %f', data.data)
    t.pulse(float(data.data))


def listener():
    
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('steer', Float32, callbackSteer)
    rospy.Subscriber('throttle', Float32, callbackThrottle)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except (KeyboardInterrupt, SystemExit):
        s.pulse(0.15)
        t.pulse(0.15)

