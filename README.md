# People-counter
# People-counter
Week 3: Sensor and Actuator Demonstration
During this week, I conducted tests for the individual sensors and actuators needed for the project. For the distance sensors, I evaluated their accuracy in detecting objects at varying ranges and ensured they can handle the required real-world conditions. The tilt sensor was tested for sensitivity to small angular changes, and the PIR sensor was validated for its ability to reliably detect motion. Each sensor was connected to the Raspberry Pi, and initial readings were logged to verify communication and data integrity. This testing phase ensured that all components were functioning as expected before integration into the larger system.

Week 4: Sensor and Actuator Optimization
Building on the previous week, I fine-tuned the configuration of each sensor and actuator. Threshold values were calibrated for the distance sensors to avoid false positives or negatives. The tilt sensor's performance was optimized for responsiveness and stability, while the PIR sensor was further tested in various lighting and environmental conditions to ensure reliability. A Python script was used to automate sensor testing and to log data in real-time, making it easier to identify and address any inconsistencies.

Week 5: Preparing Components for Housing
This week focused on preparing the sensors and actuators for installation into the project’s housing. I designed and 3D-printed mounts and supports to securely hold each sensor in place within the enclosure. Wire lengths were adjusted, connectors were soldered, and protective casings were applied to ensure durability. The housing design was reviewed to accommodate all components while maintaining proper airflow and accessibility for troubleshooting.

Week 6: Finalizing the Housing
Continuing from the previous week, I assembled the sensors, actuators, and other hardware into the prepared housing. This required precise alignment to ensure optimal functionality, particularly for the distance sensors, which needed unobstructed views of their measurement zones. Additional tests were performed with the components installed to confirm that the housing did not interfere with performance. I also added labels and organized internal wiring to make future maintenance straightforward.

Week 7: Integrating Components with the Raspberry Pi
This week marked the integration of all sensors and actuators with the Raspberry Pi. I set up GPIO pin configurations and connected the hardware to the Raspberry Pi using a custom breakout board. I developed a Python script to read sensor data and tested the full system for data acquisition accuracy. Debugging was done to resolve any issues with signal interference or communication errors.

Week 8: Assembling the Complete System
The final assembly stage involved installing the Raspberry Pi into the housing alongside the sensors and actuators. Cable management was a priority to prevent tangling and potential damage during operation. I tested the entire system to ensure all components worked seamlessly together. The housing was then securely sealed, and the device was powered on to verify its full functionality in a simulated environment.

Week 9: Demonstrating Model Functionality
With the complete system assembled, I performed a full demonstration of the pedestrian counter. This included testing all sensors under various conditions and logging the results to confirm the device’s accuracy and reliability. While the web application was not yet implemented, data was displayed directly on a connected monitor or logged locally for analysis. Any minor adjustments were made to optimize performance based on the demonstration findings.

Week 10: Database Development for the Web Application
The focus this week was on designing and implementing a database to store sensor readings and event logs. I created the database schema to include tables for devices, sensor data, and alerts. The database was integrated with the Raspberry Pi using SQLite, enabling efficient storage and retrieval of information.

Week 11: Web Application Development
TODO
