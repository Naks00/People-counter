
from flask import Flask, jsonify, render_template, request
import sqlite3
import random
from datetime import datetime, timedelta

app = Flask(__name__)

DB_PATH = "C:\\Users\\ante.nakic\Desktop\ppl\People-counter\Software\People-counter\pedestrian_counter.db"

def create_sensors_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # SQL query to create the sensors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_name TEXT NOT NULL,
            sensor_location TEXT NOT NULL,
            status TEXT DEFAULT 'active'
        )
    ''')
    
    conn.commit()
    conn.close()

# Call the function to create the table
create_sensors_table()


# Function to get pedestrian count
def get_pedestrian_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT total_count FROM summary")  
    count = cursor.fetchone()[0]
    conn.close()
    return count

def reset_pedestrian_count(): 
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE summary SET total_count = 0")
        conn.commit()
    except Exception as e:
        print("Error:",e)
    finally:
        conn.close()

def get_sensors():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensors")  
    sensors_data = cursor.fetchall()
    conn.close()
    return [{"id": s[0], "sensor_name": s[1], "sensor_location": s[2]} for s in sensors_data]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/count")
def count():
    return jsonify(count=get_pedestrian_count())

@app.route("/sensors")
def sensors():
    return jsonify(sensors=get_sensors())

@app.route("/api/add-sensor", methods=["POST"])
def add_sensor():
    data = request.json
    sensor_name = data.get('sensor_name')
    sensor_location = data.get('sensor_location')
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO sensors (sensor_name, sensor_location) VALUES (?, ?)", 
                       (sensor_name, sensor_location))
        conn.commit()
        return jsonify(message="Sensor added successfully!")
    except Exception as e:
        conn.rollback()
        return jsonify(error=str(e)), 500
    finally:
        conn.close()

@app.route("/api/update-sensor", methods=["PUT"])
def update_sensor():
    data = request.json
    id = data.get('id')
    sensor_name = data.get('sensor_name')
    sensor_location = data.get('sensor_location')
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("UPDATE sensors SET sensor_name = ?, sensor_location = ? WHERE id = ?", 
                       (sensor_name, sensor_location, id))
        conn.commit()
        return jsonify(message="Sensor updated successfully!")
    except Exception as e:
        conn.rollback()
        return jsonify(error=str(e)), 500
    finally:
        conn.close()

@app.route("/api/delete-sensor", methods=["DELETE"])
def delete_sensor():
    data = request.json
    id = data.get('id')
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM sensors WHERE id = ?", (id,))
        conn.commit()
        return jsonify(message="Sensor deleted successfully!")
    except Exception as e:
        conn.rollback()
        return jsonify(error=str(e)), 500
    finally:
        conn.close()

@app.route("/reset", methods=["POST"])
def reset():
    reset_pedestrian_count()
    return jsonify(message="Counter reset successfully!")

@app.route("/daily_counts")
def daily_counts():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        # Query to count pedestrians grouped by date
        cursor.execute("""
            SELECT DATE(timestamp) as date, COUNT(*) as count
            FROM pedestrians
            GROUP BY DATE(timestamp)
            ORDER BY DATE(timestamp);
        """)
        
        daily_counts = [{"date": row[0], "count": row[1]} for row in cursor.fetchall()]
        return jsonify(daily_counts)
    except Exception as e:
        print("Error fetching daily counts:", e)
        return jsonify(error="Failed to fetch daily counts"), 500
    finally:
        conn.close()

@app.route("/insert_bulk_data/<int:num_records>")
def insert_bulk_data(num_records):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Base date for inserting records
    base_date = datetime(2025, 1, 31)

    try:
        for _ in range(num_records):
            # Generate a random time offset in minutes (e.g., -30 to +30 minutes)
            time_offset = random.randint(-30, 30)
            timestamp = base_date + timedelta(minutes=time_offset)
            direction = random.choice(['right', 'left'])
            
            cursor.execute("INSERT INTO pedestrians (timestamp, direction) VALUES (?, ?)", 
                           (timestamp.strftime('%Y-%m-%d %H:%M:%S'), direction))
        
        conn.commit()
        return jsonify(message=f"{num_records} records inserted successfully!")
    except Exception as e:
        conn.rollback()
        return jsonify(error=str(e)), 500
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=False)
