# Create a file called setup_db.py
import sqlite3

# Connect to the database
conn = sqlite3.connect("kneeldiamonds.db")
cursor = conn.cursor()

# Read and execute your SQL script
with open("kneeldiamonds.sql", "r") as f:
    sql_script = f.read()

cursor.executescript(sql_script)
conn.commit()
conn.close()

print("Database setup complete!")
