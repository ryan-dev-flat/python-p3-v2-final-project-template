from . import CURSOR, CONN

class Post:
    def __init__(self, id, date, content):
        self.date = date
        self.content = content
        self.id = id

    # ORM methods for class Post
    def create_post(self):
        CURSOR.execute("INSERT INTO posts (id, date, content) VALUES (?, ?, ?)", (self.id, self.date, self.content))
        CONN.commit()

    @staticmethod
    def delete_post(id):
        CURSOR.execute("DELETE FROM posts WHERE id = ?", (id,))
        CONN.commit()

    @staticmethod
    def get_all_posts():
        CURSOR.execute("SELECT * FROM posts")
        return CURSOR.fetchall()

    @staticmethod
    def find_post_by_id(id):
        CURSOR.execute("SELECT * FROM posts WHERE id = ?", (id,))
        return CURSOR.fetchone()