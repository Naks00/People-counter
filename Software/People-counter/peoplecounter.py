import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD
import sqlite3
from datetime import datetime
import os

DB_PATH = "/home/student/Documents/Nakic/IoTRazvojniProjekt/pedestrian_counter.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedestrians(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               timestamp TEXT NOT NULL,
               direction TEXT NOT NULL
)

""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS summary(
               id INTEGER PRIMARY KEY,
               total_count INTEGER DEFAULT 0
)

""")
conn.commit()

def log_pedestrian(direction):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO pedestrians (timestamp, direction) VALUES (?, ?)",(timestamp,direction))
    conn.commit()
    update_summary()
    print(f"Logged:{timestamp}-{direction} ")

def update_summary():
    cursor.execute("""
    UPDATE summary
    SET total_count = total_count+ 1
    WHERE id = 1
    """)
conn.commit()


# GPIO Setup
SENSORS = {
    "Left": {"TRIG": 27, "ECHO": 22},  # Left-side ultrasonic sensor
    "Right": {"TRIG": 10, "ECHO": 9},  # Right-side ultrasonic sensor
}

PIR_SENSOR = 17  # Motion sensor (detects heat)
SHOCK_SENSOR = 5  # Detects movement or tilt

# LCD Setup
lcd = CharLCD(cols=16, rows=2, pin_rs=7, pin_e=8, pins_data=[25, 24, 23, 18], numbering_mode=GPIO.BCM)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_SENSOR, GPIO.IN)
GPIO.setup(SHOCK_SENSOR, GPIO.IN)

# Setup GPIO for ultrasonic sensors
for sensor in SENSORS.values():
    GPIO.setup(sensor["TRIG"], GPIO.OUT)
    GPIO.setup(sensor["ECHO"], GPIO.IN)

# Global variables
people_count = 0

def get_distance(trig, echo):
    """Measure distance using an ultrasonic sensor."""
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(echo) == 0:
        start_time = time.time()

    while GPIO.input(echo) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    return round(distance, 2)

def update_lcd():
    """Update LCD display with pedestrian count."""
    lcd.clear()  # Ensure old numbers don’t remain
    lcd.cursor_pos=(0,0)
    lcd.write_string(f"Pedestrian Cnt:")
    lcd.cursor_pos=(1,0)
    lcd.write_string(f"{people_count:03d}")  # Always show 3 digits

def detect_pedestrian():
    """Detect if a person (not an object) is present."""
    return GPIO.input(PIR_SENSOR) == 1  # Returns True if PIR detects heat

def detect_movement():
    """Detect if the device is being moved or tilted."""
    if GPIO.input(SHOCK_SENSOR) == 1:
        print("Device moved!")
        lcd.clear()
        lcd.write_string("Device Tilted!")
        time.sleep(2)
        update_lcd()

def track_movement():
    """Determine movement direction (Left to Right or Right to Left)."""
    global people_count

    while True:
        left_distance = get_distance(SENSORS["Left"]["TRIG"], SENSORS["Left"]["ECHO"])
        right_distance = get_distance(SENSORS["Right"]["TRIG"], SENSORS["Right"]["ECHO"])
        person_detected = detect_pedestrian()


        if right_distance < 50 and person_detected:
        # Person is near the right sensor, wait for left sensor
            start_time = time.time()
            while time.time() - start_time < 3:
                left_distance = get_distance(SENSORS["Left"]["TRIG"], SENSORS["Left"]["ECHO"])
                if left_distance < 50:
                    people_count += 1  # Right → Left (Exited)
                    print(f"Moved Left | Count: {people_count}")
                    update_lcd()
                    time.sleep(2)
                    log_pedestrian("left")
                    return
        if left_distance < 50 and person_detected:
            # Person is near the left sensor, wait for right sensor
            start_time = time.time()
            while time.time() - start_time < 3:
                right_distance = get_distance(SENSORS["Right"]["TRIG"], SENSORS["Right"]["ECHO"])
                if right_distance < 50:
                    people_count += 1  # Left → Right (Entered)
                    print(f"Moved Right | Count: {people_count}")
                    update_lcd()
                    time.sleep(2)
                    log_pedestrian("right")
                    return

     

        detect_movement()  # Check if device was tilted
        time.sleep(1) 

try:
    print("Pedestrian Counter Started...")
    update_lcd()

    while True:
        track_movement()

except KeyboardInterrupt:
    print("Stopping...")
    GPIO.cleanup()
