# People-counter
# People-counter
---
# Week 3: Sensor and Actuator Demonstration
During this week, I conducted tests for the individual sensors and actuators needed for the project. For the distance sensors, I evaluated their accuracy in detecting objects at varying ranges and ensured they can handle the required real-world conditions. The tilt sensor was tested for sensitivity to small angular changes, and the PIR sensor was validated for its ability to reliably detect motion. Each sensor was connected to the Raspberry Pi, and initial readings were logged to verify communication and data integrity. This testing phase ensured that all components were functioning as expected before integration into the larger system.

## Components Used

-Raspberry Pi

-HC-SR501 PIR Sensor (Motion detection)

-HC-SR04 Ultrasonic Sensors (Distance measurement, two used for accuracy)

-KY-002 Shock Sensor (Detects vibrations or movement)

-QAPASS Display (Displays real-time pedestrian count)

-Jumper wires & Breadboard

# Week 4: Schematic drawing
Schematic drawing was created to provide a clear visual representation of how all components are connected. This includes wiring for the HC-SR501 PIR sensor, two HC-SR04 ultrasonic sensors, KY-002 shock sensor module, and the display module labeled 'QAPASS'. The schematic helps ensure proper connections and makes troubleshooting easier if any issues arise.

# Week 5: Preparing Components for Housing
This week focused on preparing the sensors and actuators for installation into the project’s housing. I designed and 3D-printed mounts and supports to securely hold each sensor in place within the enclosure. Protective casings were applied to ensure durability. The housing design was reviewed to accommodate all components.

# Week 6: Finalizing the Housing
Continuing from the previous week, I assembled the sensors, actuators, and other hardware into the prepared housing. This required precise alignment to ensure optimal functionality, particularly for the distance sensors, which needed unobstructed views of their measurement zones.

# Week 7: Integrating Components with the Raspberry Pi
This week marked the integration of all sensors and actuators with the Raspberry Pi. I set up GPIO pin configurations and connected the hardware to the Raspberry Pi using a custom breakout board. I developed a Python script to read sensor data and tested the full system for data acquisition accuracy. Debugging was done to resolve any issues with signal interference or communication errors.

# Week 8: Assembling the Complete System
The final assembly stage involved installing the Raspberry Pi into the housing alongside the sensors and actuators. Cable management was a priority to prevent tangling and potential damage during operation. I tested the entire system to ensure all components worked seamlessly together. The housing was then securely sealed, and the device was powered on to verify its full functionality in a simulated environment.

# Week 9: Demonstrating Model Functionality
With the complete system assembled, I performed a full demonstration of the pedestrian counter. This included testing all sensors under various conditions and logging the results to confirm the device’s accuracy and reliability. While the web application was not yet implemented, data was displayed directly on a connected monitor or logged locally for analysis. Any minor adjustments were made to optimize performance based on the demonstration findings.

# Week 10: Database Development for the Web Application
The focus this week was on designing and implementing a database to store sensor readings and event logs. I created the database schema to include tables for devices, sensor data, and alerts. The database was integrated with the Raspberry Pi using SQLite, enabling efficient storage and retrieval of information.

# Week 11: Web Application Development
This week, I focused on developing the web application that serves as the interface for monitoring and managing pedestrian counting data. The backend was built using Node.js to handle API requests, while SQLite was used as the database to store sensor readings.

On the frontend, I used HTML, CSS, and JavaScript to create a user-friendly dashboard where real-time data from the Raspberry Pi is displayed. The web application allows users to view pedestrian counts, access historical data, and receive alerts based on predefined thresholds.

API endpoints were implemented for fetching sensor data, adding new sensor readings, and managing devices. Security measures such as authentication and data validation were also added to protect the system from unauthorized access and incorrect data inputs.

To test the web application, I deployed it locally and verified that sensor data was correctly stored and displayed. Debugging and performance optimization were also performed to ensure smooth operation.
