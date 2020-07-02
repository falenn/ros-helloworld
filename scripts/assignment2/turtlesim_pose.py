#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose

def poseCallback(pose_msg):
    print "Pose: x:%f y:%f yaw:%f" % (pose_msg.x, pose_msg.y, pose_msg.theta)

if __name__ == '__main__':
    try:
        rospy.init_node("turtlesim_mostion_pose", anonymous=True)
        rospy.Subscriber('/turtle1/pose', Pose, poseCallback)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")

        