import rospy
from std_msgs.msg import Int8


rospy.init_node('tmp')
pub = rospy.Publisher('hijacking_topic', Int8, queue_size=1)

rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(0)
    print('pub')
    rate.sleep()
