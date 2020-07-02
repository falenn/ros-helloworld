# Assignment 2
Curtis Bates
20200702

## Question 1
Find the topic name of the pose turtlesim and its message type:

```
curtis@rosmaster:~$ rostopic list
/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

```
curtis@rosmaster:~$ rostopic info /turtle1/pose
Type: turtlesim/Pose

Publishers: 
 * /turtlesim (http://192.168.1.180:38057/)

Subscribers: 
 * /turtlesim_motion_pose_6543_1593645078119 (http://192.168.1.180:35029/)
```
Message type is turtlesim/Pose:

```
curtis@rosmaster:~$ rosmsg info turtlesim/Pose
float32 x
float32 y
float32 theta
float32 linear_velocity
float32 angular_velocity
```

## Question 2:
Find the topic name of the velocity comand of turtlesim and its message type:

```
curtis@rosmaster:~$ rostopic info /turtle1/cmd_vel
Type: geometry_msgs/Twist

Publishers: 
 * /teleop_turtle (http://192.168.1.180:34779/)
 * /turtlesim_motion_pose_6543_1593645078119 (http://192.168.1.180:35029/)

Subscribers: 
 * /turtlesim (http://192.168.1.180:38057/)
```

Message type is geometry_msgs/Twist
```
curtis@rosmaster:~$ rosmsg info geometry_msgs/Twist
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```

## Question 3:
Write simple ROS program called turtlesim_pose.py...


## Question 4:
Complete code to add a publisher to make the robot move for a certain distance...