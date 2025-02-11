import RPi.GPIO as GPIO
import time

# Define GPIO pins for both ultrasonic sensors
SENSORS = {
    "Entry": {"TRIG": 27, "ECHO": 22},
    "Exit": {"TRIG": 10, "ECHO": 9},
}

GPIO.setmode(GPIO.BCM)

# Setup GPIO for both sensors
for sensor in SENSORS.values():
    GPIO.setup(sensor["TRIG"], GPIO.OUT)
    GPIO.setup(sensor["ECHO"], GPIO.IN)

def get_distance(trig, echo):
    """Measure distance from an ultrasonic sensor."""
    GPIO.output(trig, True)
    time.sleep(0.00001)  # Send 10µs pulse
    GPIO.output(trig, False)

    start_time, stop_time = time.time(), time.time()

    while GPIO.input(echo) == 0:
        start_time = time.time()

    while GPIO.input(echo) == 1:
        stop_time = time.time()

    # Calculate distance (time * speed of sound / 2)
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    return round(distance, 2)

try:
    print("Ultrasonic Sensors Test - Running...")
    while True:
        distances = {}
        for name, sensor in SENSORS.items():
            distances[name] = get_distance(sensor["TRIG"], sensor["ECHO"])

        print(f" Entry Distance: {distances['Entry']} cm | Exit Distance: {distances['Exit']} cm")
        time.sleep(1)  # Wait before next reading

except KeyboardInterrupt:
    print("Stopping...")
    GPIO.cleanup()
