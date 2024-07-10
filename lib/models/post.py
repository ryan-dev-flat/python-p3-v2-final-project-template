from models.__init__ import CURSOR, CONN
from datetime import datetime

class Post:
    def __init__(self, id, date, content, dog_id):
        self.id = id
        self.date = date
        self.content = content
        self.dog_id = dog_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        try:
            datetime.strptime(value, '%d-%m-%Y')
        except ValueError as e:
            raise ValueError("Date must be in the format DD-MM-YYYY") from e
        self._date = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str) or len(value) < 1:
            raise ValueError("Content must be a non-empty string.")
        self._content = value

    def create_post(self):
        CURSOR.execute("INSERT INTO posts (dog_id, date, content) VALUES (?, ?, ?)",
        (self.dog_id, self.date, self.content))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def delete_post(cls, id):
        CURSOR.execute("DELETE FROM posts WHERE id = ?", (id,))
        if CURSOR.rowcount == 0:
            raise ValueError(f"No post found with id {id}")
        CONN.commit()

    @classmethod
    def get_all_posts(cls):
        CURSOR.execute("SELECT * FROM posts")
        return [cls(*row) for row in CURSOR.fetchall()]

    @classmethod
    def get_posts_by_dog(cls, dog_id):
        CURSOR.execute("SELECT * FROM posts WHERE dog_id = ?", (dog_id,))
        return [cls(*row) for row in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM posts WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None