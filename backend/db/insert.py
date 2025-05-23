import sqlite3
from datetime import datetime

DB_PATH = "library.db"

def insert_book(
    title,
    author,
    isbn=None,
    ai_category=None,
    ai_price_estimate=None
):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO books (
                title, author, isbn,
                ai_category, ai_price_estimate,
                created_at
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            title,
            author,
            isbn,
            ai_category,
            ai_price_estimate,
            datetime.now()
        ))
        conn.commit()
        print(f"[OK] Book inserted: {title} by {author}")
    except sqlite3.Error as e:
        print(f"[ERROR] Database error: {e}")
    finally:
        conn.close()

# Example usage:
if __name__ == "__main__":
    insert_book(
        title="Gödel, Escher, Bach",
        author="Douglas Hofstadter",
        isbn="9780465026562",
        ai_category="Philosophy of mind",
        ai_price_estimate=18.90
    )
