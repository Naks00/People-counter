import sqlite3

def setup_tables():
    """Set up the database tables."""
    conn = sqlite3.connect("pedestrian_counter.db")
    cursor = conn.cursor()

    # Create the `pedestrians` table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedestrians (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            direction TEXT NOT NULL
        )
    ''')

    # Create the `summary` table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS summary (
            id INTEGER PRIMARY KEY,
            total_count INTEGER NOT NULL
        )
    ''')

    # Insert initial data into `summary` table if it doesn't exist
    cursor.execute('''
        INSERT OR IGNORE INTO summary (id, total_count)
        VALUES (1, 0)
    ''')

    conn.commit()
    conn.close()
    print("Tables created successfully!")

setup_tables()
