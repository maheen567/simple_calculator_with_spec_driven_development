# Module 1: The Robotic Nervous System (ROS 2)

## Chapter 1: Foundations of ROS 2 – The Robotic Middleware

### What is ROS 2 and why middleware is required

ROS 2 (Robot Operating System 2) is a set of software libraries and tools that help you build robot applications. It provides services you would expect from an operating system, including hardware abstraction, low-level device control, implementation of widely used functionality, message-passing between processes, and package management. ROS 2 is designed for a production environment, with support for real-time control, embedded systems, and commercial development.

Middleware is essential in robotics to facilitate communication between different software components (nodes) that often run as separate processes. It handles tasks like data serialization, network communication, and synchronization, allowing developers to focus on robot logic rather than low-level communication details.

### ROS 2 architecture overview: Nodes, Topics, Services, Actions

-   **Nodes**: The fundamental computational units in ROS 2. A node typically performs a specific task, such as controlling a motor, processing sensor data, or implementing a decision-making algorithm.
-   **Topics**: Nodes communicate by publishing messages to topics. Other nodes can subscribe to these topics to receive the messages. This is a one-to-many publish-subscribe communication pattern.
-   **Services**: Services provide a request-response communication pattern. A client node sends a request to a service server node, which performs a computation and returns a response.
-   **Actions**: Actions are used for long-running tasks that require feedback. A client sends a goal to an action server, which executes the task and provides periodic feedback and a final result.

### Pub/Sub communication model, DDS (conceptual explanation, not deep protocol internals)

The publish-subscribe (pub/sub) model is a core communication pattern in ROS 2. Nodes publish data (messages) to named channels called topics. Other nodes can subscribe to these topics to receive the published data in real-time. This decouples publishers from subscribers, allowing for flexible and scalable system design.

DDS (Data Distribution Service) is the underlying middleware that ROS 2 uses for intra-process and inter-process communication. DDS provides a standardized, real-time, data-centric publish-subscribe mechanism. ROS 2 leverages DDS to provide features like quality of service (QoS) policies, which allow fine-grained control over message delivery (e.g., reliability, durability).

### Comparison: Traditional software vs distributed robotic systems

Traditional software systems often operate in a more controlled, single-process, or tightly coupled environment. In contrast, distributed robotic systems are inherently concurrent, asynchronous, and often deal with real-world uncertainties and hardware interactions. ROS 2 addresses these challenges by providing:

-   **Concurrency**: Built-in support for managing multiple concurrent processes (nodes).
-   **Asynchronicity**: Communication patterns like pub/sub and actions handle asynchronous events naturally.
-   **Hardware Abstraction**: Standardized interfaces for sensors and actuators.
-   **Interoperability**: Enables components developed by different teams or vendors to work together.

### Simple rclpy node example (publisher + subscriber)

```python
# publisher_node.py
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

```python
# subscriber_node.py
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription  # prevent unused variable warning
        self.subscription = self.create_subscription(
            String, 'topic', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
