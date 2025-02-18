
from flask import Flask, jsonify, render_template
import sqlite3
import random
from datetime import datetime, timedelta

app = Flask(__name__)

DB_PATH = "C:\\Users\\anten\\Desktop\\IoTRazvojniProjekt\\pedestrian_counter.db"
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


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/count")
def count():
    return jsonify(count=get_pedestrian_count())

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
