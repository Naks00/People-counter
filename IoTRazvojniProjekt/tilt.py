import RPi.GPIO as GPIO
import time

SHOCK_PIN = 5  # KY-002 Digital Output Pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(SHOCK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("KY-002 Shock Sensor Test - Tap or Tilt the Device")

try:
    while True:
        if GPIO.input(SHOCK_PIN) == 0:
            print("Shock/Tilt Detected!")
            time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopped")
    GPIO.cleanup()