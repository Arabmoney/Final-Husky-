#!/usr/bin/env python
import time
import rospy
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import *
import time
from geometry_msgs.msg import Twist


JOINT_NAMES = ['ur5_arm_shoulder_pan_joint', 'ur5_arm_shoulder_lift_joint', 'ur5_arm_elbow_joint',
               'ur5_arm_wrist_1_joint', 'ur5_arm_wrist_2_joint', 'ur5_arm_wrist_3_joint']

Q1 = [1.57,-1.57,0,-1.57,0,0]
Q2 = [0,-0.2,1.4,5,1,1]
Q3 = [-0.5,-1.2,1.9,2,0,0]
Q4 = [-0.5,-0.3,1.9,2,2,1]
Q5 = [-0.5,-0.001,1.9,2,2,1]
client = None


def move(position):
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    g.trajectory.points = [
        JointTrajectoryPoint(positions=position, velocities=[0]*6, time_from_start=rospy.Duration(2.0))]
    client.send_goal(g)
    try:
        client.wait_for_result()
    except KeyboardInterrupt:
        client.cancel_goal()
        raise


def move_disordered():
    order = [4, 2, 3, 1, 5, 0]
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = [JOINT_NAMES[i] for i in order]
    q1 = [Q1[i] for i in order]
    g.trajectory.points = [
        JointTrajectoryPoint(positions=q1, velocities=[0]*6, time_from_start=rospy.Duration(2.0))]
    client.send_goal(g)
    client.wait_for_result()


    def distance():
        rospy.init_node('out_and_back', anonymous=False)
        rospy.on_shutdown( distance().shutdown)      
        distance().cmd_vel = rospy.Publisher('husky_velocity_controller/cmd_vel', Twist)        
        # How fast will we update the robot's movement?
        rate = 50        
        # Set the equivalent ROS rate variable
        r = rospy.Rate(rate)        
        # Set the forward linear speed to 0.2 meters per second 
        linear_speed = -0.2        
        # Set the travel distance to 1.0 meters
        goal_distance = 0.5        
        # How long should it take us to get there?
        linear_duration = goal_distance / linear_speed        
        # Set the rotation speed to 1.0 radians per second
        angular_speed = 1.0        
        # Set the rotation angle to Pi radians (180 degrees)
        goal_angle = pi        
        # How long should it take to rotate?
        angular_duration = goal_angle / angular_speed     
        # Loop through the two legs of the trip  
        for i in range(2):
            # Initialize the movement command
            move_cmd = Twist()            
            # Set the forward speed
            move_cmd.linear.x = linear_speed            
            # Move forward for a time to go the desired distance
            ticks = int(linear_duration * rate)            
            for t in range(ticks):
                distance().cmd_vel.publish(move_cmd)
                r.sleep()                
            ticks = int(goal_angle * rate)
            
            for t in range(ticks):           
                distance().cmd_vel.publish(move_cmd)
                r.sleep()                    
    def shutdown(self):
        # Always stop the robot when shutting down the node.
        rospy.loginfo("Stopping the robot...")
        distance().cmd_vel.publish(Twist())
        rospy.sleep(1)


def main():
    global client
    try:
        rospy.init_node("test_move", anonymous=True, disable_signals=True)
        client = actionlib.SimpleActionClient('arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
        print "Waiting for ur5_arm server..."
        client.wait_for_server()
        print "Connected to ur5_arm server"
        move(Q1)
	move(Q2)
	move(Q3)
	move(Q4)

	print "finished"
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise




if __name__ == '__main__': 
	distance()
    
