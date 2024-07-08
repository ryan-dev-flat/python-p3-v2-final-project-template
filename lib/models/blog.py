from . import CURSOR, CONN

class Blog:
    def __init__(self, blog_name, dog_id):
        self.blog_name = blog_name
        self.dog_id = dog_id

    #ORM methods for class Blog
    def create_blog(self):
        #check if the blog already exists
        CURSOR.execute("SELECT * FROM blogs WHERE blog_name - ?", (self.blog_name))
        blog = CURSOR.fetchone()
        if blog is None:
            #if the blog does not exist, create a new one
            CURSOR.execute("INSERT INTO blogs (blog_name, dog_id) VALUES(?, ?)", (self.blog_name, self.dog_id))
            CONN.commit()
        else:
            print("A blog with this name already exists. Try again")

    def get_blogs(self):
        #retrieve list of blogs
        CURSOR.execute("SELECT * FROM blogs", (self.blog_name))