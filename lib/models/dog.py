from models.__init__ import CURSOR, CONN

class Dog:
    def __init__(self, id, name, breed, sex, blog, human_name):
        self.id = id
        self.name = name
        self.breed = breed
        self.sex = sex
        self.blog = blog
        self.human_name = human_name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 20:
            raise ValueError("Name must be between 1 and 20 characters.")
        self._name = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        value = value.upper()
        if value not in ['M', 'F']:
            raise ValueError("Sex must be 'M' or 'F'.")
        self._sex = value

    def create_dog(self):
        CURSOR.execute("INSERT INTO dogs (name, breed, sex, blog, human_name) VALUES(?, ?, ?, ?, ?)",
        (self.name, self.breed, self.sex, self.blog, self.human_name))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def delete_dog(cls, id):
        CURSOR.execute("DELETE FROM dogs WHERE id = ?", (id,))
        if CURSOR.rowcount == 0:
            raise ValueError(f"No dog found with id {id}")
        CONN.commit()

    @classmethod
    def get_all_dogs(cls):
        CURSOR.execute("SELECT * FROM dogs")
        return [cls(*row) for row in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM dogs WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None