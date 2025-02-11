import sqlite3

def create_database():

    conn = sqlite3.connect("pedestrian_counter.db")
    conn.close()
    print("Uspijelo")

create_database()