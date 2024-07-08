# lib/models/__init__.py
import sqlite3

CONN = sqlite3.connect('dog_blogs.db')
CURSOR = CONN.cursor()

# create dogs table
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS dogs (
      id INTEGER PRIMARY KEY,
      blog_name TEXT NOT NULL,
      dog_id INTEGER,
      FOREIGN KEY(blog_id)  REFERENCES blogs(id)
    )
""")

# create blogs table
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS blogs (
        id INTEGER PRIMARY KEY, blog_name TEXT NOT NULL,
        dog_id INTEGER,
        FOREIGN KEY(dog_id) REFERENCES dogs(id)
    )
""")

# create posts table
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        content TEXT NOT NULL,
        blog_id INTEGER,
        FOREIGN KEY(blog_id) REFERENCES blogs(id)
    )
""")

CONN.commit()
