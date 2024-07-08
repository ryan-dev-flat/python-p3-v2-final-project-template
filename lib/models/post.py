from . import CURSOR, CONN

class Post:
     def __init__(self, date, content, blog_id):
         self.date = date
         self.content = content
         self.blog_id = blog_id

    #ORM methods for class Post
def create_post(self):
    CURSOR.execute("INSERT INTO posts (date, content, blog_id) VALUES (?, ?, ?)", (self.date, self.content, self.blog_id))
    CONN.commit()

@staticmethod
def delete_post(id):
    CURSOR.execute("DELETE FROM posts WHERE id - ?", (id,))
    CONN.commit()

@staticmethod
def get_all_posts():
    CURSOR.execute("SELECT * FROM posts")
    return CURSOR.fetchall()

@staticmethod
def find_post_by_id(id):
    CURSOR.execute("SELECT * FROM posts WHERE id = ?", (id,))
    return CURSOR.fetchone()

@staticmethod
def get_posts_by_blog(id):
    CURSOR.execute("SELECT * FROM POSTS WHERE blog_id = ?", (id,))
    return CURSOR.fetchmany()