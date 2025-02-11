import RPi.GPIO as GPIO
import time

# Change these based on your wiring
TRIG = 10  # Trigger Pin
ECHO = 9  # Echo Pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # Send 10us pulse
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # Convert to cm
    return round(distance, 2)

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped")
    GPIO.cleanup()
