# lib/helpers.py
from models.dog import Dog
from models.post import Post

def create_dog():
    name = input("Enter the name of the dog: ")
    breed = input("Enter the breed of the dog: ")
    sex = input("Enter the sex of the dog (M or F): ")
    dog = Dog(name, breed, sex)
    dog.create_dog()
    print(f"{name}, your account is created as a {sex} {breed}.")
    print(f"Your Blog {name} created.")

def delete_dog():
    id = input("Enter the id of the dog blog to delete: ")
    Dog.delete_dog(id)
    print(f"Dog blog with id {id} deleted.")

def create_post():
    post_id = input("Enter the id of the dog: ")
    date = input("Enter the date of the post (MM-DD-YYYY): ")
    content = input("Enter the content of your post: ")
    post = Post(post_id, date, content)
    post.create_post()
    print(f"Post created on {date}.")

def delete_post():
    id = input("Enter the id of the post to delete: ")
    Post.delete_post(id)
    print(f"Post with id {id} deleted.")
