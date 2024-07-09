# lib/models/__init__.py
import sqlite3

# Fetch breeds from dog_breeds.db and insert into dog_blogs.db
with sqlite3.connect('dog_breeds.db') as conn_breeds:
    cursor_breeds = conn_breeds.cursor()
    cursor_breeds.execute("SELECT breed FROM akc-data-latest")
    breeds = cursor_breeds.fetchall()

with sqlite3.connect('dog_blogs.db') as conn_blogs:
    cursor_blogs = conn_blogs.cursor()
    for breed in breeds:
        cursor_blogs.execute("INSERT INTO breeds (id, breed_name) VALUES (?, ?)", (id, breed,))
    conn_blogs.commit()

# Create tables in dog_blogs.db
with sqlite3.connect('dog_blogs.db') as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS breeds (
        id INTEGER PRIMARY KEY,
        breed_name TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dogs (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        sex TEXT NOT NULL,
        human_companion TEXT NOT NULL
        FOREIGN KEY(breed_id) REFERENCES breeds(id),
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        content TEXT NOT NULL,
        dog_id INTEGER,
        FOREIGN KEY(dog_id) REFERENCES dogs(id)
        )
    """)
    conn.commit()
