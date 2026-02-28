# Module 1: The Robotic Nervous System (ROS 2)

This module introduces the fundamentals of ROS 2 and its application in robotics, bridging AI agents with robot control systems.

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

## Chapter 2: Bridging AI Agents to Robot Controllers

### Role of rclpy in Python-based AI systems, Connecting an AI decision loop to ROS topics

`rclpy` is the Python client library for ROS 2. It allows Python programs to act as ROS 2 nodes, enabling them to communicate using topics, services, and actions. For AI systems, `rclpy` acts as the bridge, allowing AI models or decision-making logic written in Python to interact with the robot's hardware and other software components.

To connect an AI decision loop to ROS topics, you would typically:

1.  Initialize `rclpy` and create a ROS 2 node.
2.  Subscribe to relevant topics to receive sensor data or the current state of the robot.
3.  Process this data using your AI model or decision logic.
4.  Publish control commands (e.g., velocities, joint targets) to appropriate topics that are subscribed to by robot control nodes.

### Control signals: velocity commands, joint commands. Writing a minimal ROS 2 control node

Control signals are messages sent to the robot's actuators to command specific movements. Common types include:

-   **Velocity Commands**: Typically used for mobile robots, specifying linear and angular velocities (e.g., `geometry_msgs/Twist`).
-   **Joint Commands**: Used for robotic arms or manipulators, specifying target positions, velocities, or efforts for individual joints (e.g., `sensor_msgs/JointState` or custom joint command messages).

A minimal ROS 2 control node would subscribe to command topics, process the incoming messages, and translate them into low-level commands for the robot's hardware drivers. It might also publish feedback on the robot's current state.

### Service-based command handling. Designing safe control interfaces

While topics are suitable for continuous commands like velocity, services can be used for discrete, one-off commands or configuration requests. For example, a service could be used to request the robot to perform a specific high-level action (e.g., "go to pre-defined pose") or to change operational modes.

Designing safe control interfaces is paramount in robotics:

-   **Clear Contracts**: Define the expected commands and their ranges (e.g., maximum safe velocities).
-   **Input Validation**: Sanitize and validate all incoming commands to prevent erroneous or dangerous movements.
-   **Safety Overrides**: Implement mechanisms for emergency stops or manual control that can immediately override autonomous commands.
-   **State Awareness**: Ensure commands are only sent when the robot is in an appropriate state.
-   **Feedback Loops**: Monitor the robot's actual state and behavior to detect deviations from expected commands.

### Architectural diagram explanation (text-based description)

Consider a system where an AI agent (running as a ROS 2 node) makes high-level decisions. This agent subscribes to sensor data topics (e.g., camera images, odometry) and publishes desired actions (e.g., target velocity, navigation goal) to command topics. A separate `robot_controller` node subscribes to these command topics, interprets the AI's intentions, and translates them into low-level commands for the robot's motors. The `robot_controller` node might also publish feedback on the robot's current state (e.g., joint positions, current velocity) back to a shared state topic, which the AI agent can subscribe to for state awareness. For specific tasks like "move to location X", the AI agent could call a service provided by the `robot_controller`.

## Chapter 3: URDF for Humanoids

### Introduction to URDF

URDF (Universal Robot Description Format) is an XML-based file format used by ROS to represent a robot's kinematic and inertial properties. It describes the robot's structure as a hierarchy of *links* (representing physical components) and *joints* (representing the connections between links, defining their relative motion).

### Defining robot links and joints

-   **Links**: Define the physical properties of robot components, such as their geometry (box, cylinder, mesh), visual appearance, collision properties, and inertial properties (mass, inertia tensor).
-   **Joints**: Define the type of connection between two links and the spatial relationship between them. Common joint types include:
    -   `fixed`: No relative motion between the parent and child link.
    -   `revolute`: Rotational motion around an axis.
    -   `prismatic`: Translational motion along an axis.
    -   `continuous`: Infinite revolute motion (like a wheel).

Each joint also specifies its axis of motion, limits (if applicable), and safety characteristics.

### Creating a basic humanoid model

A URDF for a humanoid robot would typically involve:

-   A `base_link` representing the robot's torso or base.
-   Joints and links for the torso, neck, arms (shoulder, elbow, wrist), head, and legs (hip, knee, ankle).
-   Appropriate joint types (revolute for most arms/legs, fixed for some connections) and limits to define the robot's degrees of freedom.
-   Inertial properties for realistic physics simulation.
-   Visual and collision elements to represent the robot's physical form.

### Visualizing the URDF model

ROS provides tools like `rviz` (ROS Visualization) to visualize URDF models. By loading the URDF file into `rviz`, you can see a 3D representation of the robot, inspect its structure, and even simulate its motion by publishing joint states.
