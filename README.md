# People-counter

## [Table of Contents](pplx://action/followup)
1. [Project Overview](#project-overview)
2. [Week 3: Sensor and Actuator Demonstration](#week-3-sensor-and-actuator-demonstration)
3. [Week 4: Schematic Drawing](#week-4-schematic-drawing)
4. [Week 5: Preparing Components for Housing](#week-5-preparing-components-for-housing)
5. [Week 6: Finalizing the Housing](#week-6-finalizing-the-housing)
6. [Week 7: Integrating Components with the Raspberry Pi](#week-7-integrating-components-with-the-raspberry-pi)
7. [Week 8: Assembling the Complete System](#week-8-assembling-the-complete-system)
8. [Week 9: Demonstrating Model Functionality](#week-9-demonstrating-model-functionality)
9. [Week 10: Database Development for the Web Application](#week-10-database-development-for-the-web-application)
10. [Week 11: Web Application Development](#week-11-web-application-development)
11. [Final Remarks](#final-remarks)

## [Project Overview](pplx://action/followup)
The People-counter project is a system designed to accurately monitor pedestrian traffic using a combination of distance sensors, motion detection, and a Raspberry Pi. The data collected is stored in an SQLite database and presented through a Flask-based web application, providing real-time pedestrian counts, historical data access, and threshold-based alerts.

---

## [Week 3: Sensor and Actuator Demonstration](pplx://action/followup)
During this week, I conducted tests for the individual sensors and actuators needed for the project. For the distance sensors, I evaluated their accuracy in detecting objects at varying ranges and ensured they can handle the required real-world conditions. The tilt sensor was tested for sensitivity to small angular changes, and the PIR sensor was validated for its ability to reliably detect motion. Each sensor was connected to the Raspberry Pi, and initial readings were logged to verify communication and data integrity. This testing phase ensured that all components were functioning as expected before integration into the larger system.

### [Components Used](pplx://action/followup)
- Raspberry Pi
- HC-SR501 PIR Sensor (Motion detection)
- HC-SR04 Ultrasonic Sensors (Distance measurement, two used for accuracy)
- KY-002 Shock Sensor (Detects vibrations or movement)
- QAPASS Display (Displays real-time pedestrian count)
- Jumper wires & Breadboard

## [Week 4: Schematic Drawing](pplx://action/followup)
Schematic drawing was created to provide a clear visual representation of how all components are connected. This includes wiring for the HC-SR501 PIR sensor, two HC-SR04 ultrasonic sensors, KY-002 shock sensor module, and the display module. The schematic helps ensure proper connections and makes troubleshooting easier if any issues arise.

![Schematic](Software/Frizting/shemaPC.png)

## [Week 5: Preparing Components for Housing](pplx://action/followup)
This week focused on preparing the sensors and actuators for installation into the project’s housing. I designed and 3D-printed mounts and supports to securely hold each sensor in place within the enclosure. Protective casings were applied to ensure durability. The housing design was reviewed to accommodate all components.

![Case](Hardware/3D-design/Images/Case-collage.png)

## [Week 6: Finalizing the Housing](pplx://action/followup)
Continuing from the previous week, I assembled the sensors, actuators, and other hardware into the prepared housing. This required precise alignment to ensure optimal functionality, particularly for the distance sensors, which needed unobstructed views of their measurement zones.

![Case](Hardware/3D-design/Images/Case-lid-collage.png)

## [Week 7: Integrating Components with the Raspberry Pi](pplx://action/followup)
This week marked the integration of all sensors and actuators with the Raspberry Pi. I set up GPIO pin configurations and connected the hardware to the Raspberry Pi using a custom breakout board. I developed a Python script to read sensor data and tested the full system for data acquisition accuracy. Debugging was done to resolve any issues with signal interference or communication errors.

**[Code](pplx://action/followup):**
```c
GPIO pin assignments for sensors and LCD
SENSORS = {
"Left": {"TRIG": 27, "ECHO": 22}, # Left-side ultrasonic sensor
"Right": {"TRIG": 10, "ECHO": 9}, # Right-side ultrasonic sensor
}

PIR_SENSOR = 17 # Motion sensor (detects heat)
SHOCK_SENSOR = 5 # Detects movement or tilt

LCD Setup - Configures the LCD screen for displaying the count
lcd = CharLCD(cols=16, rows=2, pin_rs=7, pin_e=8, pins_data=, numbering_mode=GPIO.BCM)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_SENSOR, GPIO.IN)
GPIO.setup(SHOCK_SENSOR, GPIO.IN)

Setup GPIO for ultrasonic sensors
for sensor in SENSORS.values():
GPIO.setup(sensor["TRIG"], GPIO.OUT)
GPIO.setup(sensor["ECHO"], GPIO.IN)
```
