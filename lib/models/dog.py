from . import CURSOR, CONN

class Dog:
    def __init__(self, id, name, breed, sex, blog):
        self.id = id
        self.name = name
        self.breed = breed
        self.sex = sex
        self.blog = blog

    #ORM methods for class Blog
    def create_dog(self):
        #check if the dog already exists
        CURSOR.execute("SELECT * FROM dogs WHERE id - ?", (self.dog))
        blog = CURSOR.fetchone()
        if blog is None:
            #if the blog does not exist, create a new one
            CURSOR.execute("INSERT INTO dogs (id, name, breed, sex, blog) VALUES(?, ?, ?, ?, ?)", (self.id, self.name, self.breed, self.sex, self.blog))
            CONN.commit()
        else:
            print("A dog with this name already exists. Try again")

    def get_blogs(self):
        #retrieve list of blogs
        CURSOR.execute("SELECT * FROM dogs", (self.blog))
