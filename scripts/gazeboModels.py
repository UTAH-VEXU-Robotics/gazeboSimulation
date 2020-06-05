import rospy
from std_msgs.msg import String

pub = rospy.Publisher('/gazebo/model_states', String, queue_size=10)
rospy.init_node('node_name')
r = rospy.Rate(10) # 10hz

while not rospy.is_shutdown():
    pub.publish("hello world")
    r.sleep()
