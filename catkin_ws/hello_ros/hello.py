#catkin make
#ros
import rospy
from std_msgs.msg import String


def main():
    rospy.init_node('hello', anonymous=True)
    pub = rospy.Publisher('message', String, queue_size=10)
    data =String()
    i=0
    data.data = f"hollo, ROS neotic {i]"
    rate = rospy.Rate(3)
    while True:
    pub.publish(data)   
    print("hello ROS1")
    rate.sleep()
        
if __name__ =="__main__":
    main()    


