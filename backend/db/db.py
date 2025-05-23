import sqlite3
import os

# Define path for SQLite DB
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'library.db')

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    price_suggestion REAL,
    cover_path TEXT,
    status TEXT DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database and table 'books' are ready.")
