import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Int8

class DuckieHijacker:
    def __init__(self):
        rospy.init_node('hijacker', anonymous=False)
        rospy.Subscriber('hijacking_topic', Int8, self.hj_cb)

        self.pub = rospy.Publisher('/erp42/joy', Joy, queue_size=1)
        self.msg = Joy()
        
    def hj_cb(self, msg):
        print(msg.data)
        target = msg.data
        self.msg = self.get_raw_message()

        if target == 0:
            pass
        elif target == 1: #forward

            self.msg.axes[1] = 1.0
            print('forward')
        elif target == 2: #backward
            self.msg.axes[1] = -1.0
            print('backward')
        elif target == 3: #right
            self.msg.axes[3] = -1.0
            print('right')
        elif target == 4: #left
            self.msg.axes[3] = 1.0
            print('left')

    def get_raw_message(self):
        return Joy(
            axes=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            buttons=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

    def run(self):
        self.pub.publish(self.msg)

if __name__ == "__main__":

    hj = DuckieHijacker()
    rate = rospy.Rate(10) #10hz
    while not rospy.is_shutdown():
        hj.run()
        rate.sleep()
