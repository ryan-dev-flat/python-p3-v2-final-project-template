# lib/models/__init__.py
import sqlite3

CONN = sqlite3.connect('dog_blogs.db')
CURSOR = CONN.cursor()

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS dogs (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    breed TEXT NOT NULL,
    sex TEXT NOT NULL,
    blog TEXT NOT NULL,
    human_name TEXT NOT NULL
    )
""")
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    content TEXT NOT NULL,
    dog_id INTEGER,
    FOREIGN KEY(dog_id) REFERENCES dogs(id)
    )
""")
CONN.commit()