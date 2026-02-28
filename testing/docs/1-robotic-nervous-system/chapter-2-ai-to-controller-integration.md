# Module 1: The Robotic Nervous System (ROS 2)

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

Consider a system where an AI agent (running as a ROS 2 node) makes high-level decisions. This agent subscribes to sensor data topics (e.g., camera images, odometry) and publishes desired actions (e.g., target velocity, navigation goal) to command topics. A separate `robot_controller` node subscribes to these command topics, interprets the AI's intentions, and translates them into low-level commands for the robot's hardware drivers. The `robot_controller` node might also publish feedback on the robot's current state (e.g., joint positions, current velocity) back to a shared state topic, which the AI agent can subscribe to for state awareness. For specific tasks like "move to location X", the AI agent could call a service provided by the `robot_controller`.
