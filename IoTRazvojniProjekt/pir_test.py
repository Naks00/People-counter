import RPi.GPIO as GPIO
import time

PIR_PIN = 17  # PIR Sensor GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("PIR Sensor Test - Waiting for motion...")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped")
    GPIO.cleanup()
