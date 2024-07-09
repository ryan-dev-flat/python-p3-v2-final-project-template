from . import CURSOR, CONN

class Breed:
    def __init__(self, id, breed_name):
        self.id = id
        self.breed_name = breed_name

    def create_breed(self):
        CURSOR.execute("INSERT OR IGNORE INTO breeds (breed_name) VALUES (?)", (self.breed_name,))
        if CURSOR.rowcount == 0:
            print("A breed with this name already exists. Try again.")
        else:
            CONN.commit()

    def get_all_breeds():
        CURSOR.execute("SELECT * FROM breeds")
        return CURSOR.fetchall()

