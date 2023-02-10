import rclpy
from rclpy.node import Node
import array

from sensor_msgs.msg import JointState
from std_msgs.msg import Float64

import json
import serial

ser = serial.Serial("/dev/ttyUSB0",115200)


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('serial_ctrl')
        
        self.position = []
        
        self.subscription = self.create_subscription(
            JointState,
            'joint_states',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
    
    def posGet(self, radInput, direcInput, multiInput):
        if radInput == 0:
            return 2047
        else:
            getPos = int(2047 + (direcInput * radInput / 3.1415926 * 2048 * multiInput) + 0.5)
            return getPos

    def listener_callback(self, msg):
        a = msg.position
        
        join1 = self.posGet(a[0], -1, 1)
        join2 = self.posGet(a[1], -1, 3)
        join3 = self.posGet(a[2], -1, 1)
        join4 = self.posGet(a[3],  1, 1)
        join5 = self.posGet(a[4], -1, 1)
        
        data = json.dumps({'T':3,'P1':join1,'P2':join2,'P3':join3,'P4':join4,'P5':join5,'S1':0,'S2':0,'S3':0,'S4':0,'S5':0,'A1':60,'A2':60,'A3':60,'A4':60,'A5':60})
        
        ser.write(data.encode())
        
        print(data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
