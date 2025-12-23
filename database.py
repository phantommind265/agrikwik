import sqlite3
from datetime import datetime

conn = sqlite3.connect("agrikwik.db", check_same_thread=False)
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone TEXT UNIQUE,
    username TEXT,
    location TEXT,
    email TEXT,
    created_at TEXT
)
""")
conn.commit()

def add_user(phone, username, location, email):
    cursor.execute("""
    INSERT INTO users (phone, username, location, email, created_at)
    VALUES (?, ?, ?, ?, ?)
    """, (phone, username, location, email, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def user_exists(phone):
    cursor.execute("SELECT * FROM users WHERE phone=?", (phone,))
    return cursor.fetchone()

def get_user(phone):
    cursor.execute("SELECT * FROM users WHERE phone=?", (phone,))
    return cursor.fetchone()

