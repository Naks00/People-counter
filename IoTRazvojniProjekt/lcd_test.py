import time
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

# Define LCD in 4-bit mode (adjust pins as per your wiring)
lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2,
              pin_rs=7, pin_e=8, pins_data=[25, 24, 23, 18])

try:
    lcd.clear()
    lcd.write_string("Hello, World!")
    time.sleep(2)
   
    lcd.clear()
    lcd.write_string("Raspberry Pi LCD")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Test Successful!")
    time.sleep(5)

    lcd.clear()
    lcd.write_string("Goodbye!")

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()
    GPIO.cleanup()