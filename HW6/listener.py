#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.axes)
    # duty cycle in range [0.10, 0.20]

    steer = (data.axes[0]*.05)+.15
    #steering.pulse(steer)
    rospy.loginfo(rospy.get_caller_id() + 'steering: %s, duty cycle %f', data.axes[0], steer)

    throttle = (data.axes[1]*.05)+.15
    #throttle.pulse(throttle)
    rospy.loginfo(rospy.get_caller_id() + 'throttle: %s, duty cycle %f', data.axes[1], throttle)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('joy', Joy, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
