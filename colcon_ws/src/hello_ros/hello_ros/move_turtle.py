#/turtle1/cmd_vel [geometry_msgam/msg/Twist]
import rclpy 
from geometry_msgs.msg import Twist
from rclpy.node import Node


class Move_turtle(Node):
    def __init__(self):
        super().__init__('move_turtle') # Node name
        self.create_timer(0.1, self.pub_turtle)
        self.pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.vel= 0.0
       

    def pub_turtle(self):
        msg = Twist()
        msg.angular.z = 0.5 # python type casting is free in terms of choosing number in real or integer 
        msg.linear.x = self.vel # but it is recommended consider the type should be congruent
        self.pub.publish(msg)
        self.vel += 0.01
        

def main():
    rclpy.init()
    node = Move_turtle()
    
    try: 
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__== '__main__':
    main()