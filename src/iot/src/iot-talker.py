#!/usr/bin/env python
#
# This talker example uses Python2.7 

import rospy
from std_msgs.msg import String
from iot.msg import IoTSensor

def talker():
    pub = rospy.Publisher('/iotsensor/status', IoTSensor, queue_size=10)
    rospy.init_node('iotsensor1', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        iotMsg = IoTSensor()
        iotMsg.id = 1
        iotMsg.name = "sensor1"
        iotMsg.temperature = 98.6
        iotMsg.humidity = 32.4
        rospy.loginfo("Sent IoT")
        pub.publish(iotMsg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass