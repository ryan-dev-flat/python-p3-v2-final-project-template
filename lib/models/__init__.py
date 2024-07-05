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
