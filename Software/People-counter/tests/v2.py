import RPi.GPIO as GPIO
import time

# Pin configuration
PIR_PIN = 17  # Adjust to the GPIO pin you're using for the PIR sensor
TRIG_PIN = 18  # GPIO pin connected to Ultrasonic Sensor Trigger
ECHO_PIN = 24  # GPIO pin connected to Ultrasonic Sensor Echo
TILT_PIN = 23  # GPIO pin for the Tilt Sensor

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(TILT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to measure distance with ultrasonic sensor
def get_distance():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    start_time = time.time()
    stop_time = time.time()

    # Save start time
    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()

    # Save time of arrival
    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    # Time difference between start and arrival
    time_elapsed = stop_time - start_time
    # Multiply with the speed of sound (34300 cm/s) and divide by 2
    distance = (time_elapsed * 34300) / 2
    return distance

try:
    print("Starting sensors...")
    while True:
        # Check PIR sensor for motion detection
       
        distance = get_distance()
        print(f"Distance measured by Ultrasonic Sensor: {distance:.2f} cm")
        if distance < 50:  # Adjust this threshold based on desired range
                print("Object/person detected within range.")

        # Check Tilt sensor for tilting
        if GPIO.input(TILT_PIN) == GPIO.LOW:
            print("Tilt detected! The device has been moved or knocked over.")

        time.sleep(1)  # Adjust sleep time based on response time requirements

except KeyboardInterrupt:
    print("Program stopped by User")

finally:
    GPIO.cleanup()