# lib/helpers.py
from models.dog import Dog
from models.post import Post
from datetime import datetime

def create_dog():
    name = input("Enter the name of the dog: ")
    breed = input("Enter the breed of the dog: ")
    sex = input("Enter the sex of the dog (M or F): ")
    blog = input("Enter the blog name: ")
    human_name = input("Enter the name of the dog's human companion: ")
    try:
        dog = Dog(None, name, breed, sex, blog, human_name)
        dog.create_dog()
        print(f"{name}'s account is created as a {sex} {breed} with human companion {human_name}.")
        print(f"Blog '{blog}' created.")
    except ValueError as e:
        print(f"Error: {e}")

def delete_dog():
    id = input("Enter the id of the dog blog to delete: ")
    try:
        Dog.delete_dog(id)
        print(f"Dog blog with id {id} deleted.")
    except ValueError as e:
        print(f"Error: {e}")

def display_all_dogs():
    dogs = Dog.get_all_dogs()
    if dogs:
        for dog in dogs:
            print(f"ID: {dog.id}, Name: {dog.name}, Breed: {dog.breed}, Sex: {dog.sex}, Blog: {dog.blog}, Human: {dog.human_name}")
    else:
        print("No dogs found.")

def find_dog_by_id():
    id = input("Enter the id of the dog to find: ")
    try:
        dog = Dog.find_by_id(id)
        if dog:
            print(f"ID: {dog.id}, Name: {dog.name}, Breed: {dog.breed}, Sex: {dog.sex}, Blog: {dog.blog}, Human: {dog.human_name}")
        else:
            print(f"No dog found with id {id}.")
    except ValueError as e:
        print(f"Error: {e}")



def create_post():
    while True:
        dog_id = input("Enter the id of the dog: ")
        dog = Dog.find_by_id(dog_id)
        if dog:
            break
        else:
            print(f"No dog found with id {dog_id}. Please try again.")

    while True:
        date = input("Enter the date of the post (DD-MM-YYYY): ")
        try:
            datetime.strptime(date, '%d-%m-%Y')
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    while True:
        content = input("Enter the content of your post: ")
        if content.strip():
            break
        else:
            print("Content cannot be empty. Please enter some content.")

    try:
        post = Post(None, date, content, dog_id)
        post.create_post()
        print(f"Post created on {date} for dog {dog.name}.")
    except ValueError as e:
        print(f"Error: {e}")

from models.dog import Dog
from models.post import Post

def delete_post():
    max_attempts = 3

    for attempt in range(max_attempts):
        dog_id = input("Enter the id of the dog: ")
        dog = Dog.find_by_id(dog_id)
        if dog:
            break
        else:
            attempts_left = max_attempts - attempt - 1
            print(f"No dog found with id {dog_id}. {attempts_left} attempts left.")
    else:
        input("Max attempts reached. Press any key to return to the main menu.")
        return

    for attempt in range(max_attempts):
        date = input("Enter the date of the post to delete (YYYY-MM-DD): ")
        posts = Post.get_posts_by_dog(dog_id)
        matching_posts = [post for post in posts if post.date == date]

        if matching_posts:
            post = matching_posts[0]  # one post per day
            confirm = input(f"Delete {dog.name}'s post for {date}? (Y/n): ").lower()
            if confirm == 'y' or confirm == '':
                Post.delete_post(post.id)
                print(f"Deleted: {post.id}, dog's {dog.name}, for {date} blog post.")
            else:
                print("Deletion cancelled.")
            return
        else:
            attempts_left = max_attempts - attempt - 1
            print(f"No post found for {dog.name} on {date}. {attempts_left} attempts left.")
    else:
        input("Max attempts reached. Press any key to return to the main menu.")

def display_all_posts():
    posts = Post.get_all_posts()
    if posts:
        for post in posts:
            print(f"ID: {post.id}, Date: {post.date}, Content: {post.content}, Dog ID: {post.dog_id}")
    else:
        print("No posts found.")

def find_post_by_id():
    id = input("Enter the id of the post to find: ")
    try:
        post = Post.find_by_id(id)
        if post:
            print(f"ID: {post.id}, Date: {post.date}, Content: {post.content}, Dog ID: {post.dog_id}")
        else:
            print(f"No post found with id {id}.")
    except ValueError as e:
        print(f"Error: {e}")

def display_posts_by_dog():
    dog_id = input("Enter the id of the dog: ")
    try:
        posts = Post.get_posts_by_dog(dog_id)
        if posts:
            for post in posts:
                print(f"ID: {post.id}, Date: {post.date}, Content: {post.content}")
        else:
            print(f"No posts found for dog with id {dog_id}.")
    except ValueError as e:
        print(f"Error: {e}")

def exit_program():
    print("Goodbye!")
    exit()