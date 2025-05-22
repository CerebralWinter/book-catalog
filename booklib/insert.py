import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'library.db')

def insert_book(title, author, cover_path):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO books (title, author, cover_path)
        VALUES (?, ?, ?)
    """, (title, author, cover_path))
    conn.commit()
    conn.close()
    print(f"Inserted into database: {title} by {author}")
