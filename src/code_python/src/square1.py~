#!/usr/bin/env python

import roslib; roslib.load_manifest('mini_max_tutorials')
import rospy
from geometry_msgs.msg import Twist
class square1:

def __init__(self):

rospy.on_shutdown(self.cleanup)
# publish to cmd_vel
self.pub = rospy.Publisher('cmd_vel', Twist)
 rospy.sleep(1)
 r = rospy.Rate(5.0)

while not rospy.is_shutdown():
twist = Twist()
twist.linear.x = 0.15
for i in range(10): # 10*5hz = 2sec
self.pub.publish(twist)
r.sleep()
# create a twist message, fill it in to turn
twist = Twist()
twist.angular.z = 1.57/2 # 45 deg/s * 2sec = 90 degrees for i in range(10): # 10*5hz = 2sec
self.pub.publish(twist) r.sleep()
def cleanup(self):
# stop the robot!
twist = Twist() self.pub.publish(twist)
if __name__=="__main__": rospy.init_node('square')
square()
