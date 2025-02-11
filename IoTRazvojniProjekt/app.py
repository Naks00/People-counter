from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

DB_PATH = "/home/student/Documents/Nakic/IoTRazvojniProjekt/pedestrian_counter.db"

# Function to get pedestrian count
def get_pedestrian_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT total_count FROM summary")  
    count = cursor.fetchone()[0]
    conn.close()
    return count

def reset_pedestrian_count(): # I gave up on this since I cant figure out why it wont reset :(
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=False)
