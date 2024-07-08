# lib/helpers.py
from models.dog import Dog
from models.blog import Blog
from models.post import Post
# from models.human import Human

def create_dog():
    name = input("Enter your name: Name of Dog  ")
    breed = input("Enter your Breed:  ")
    dog = Dog(name, breed)
    dog.create_dog()
    print(f"{name}, your account is created as a {breed}.")

def delete_dog():
    id = input("Enter the id of the dog to delete:  ")
    Dog.delete_dog(id)
    print(f"Dog with id {id} deleted")

def create_blog():
    blog_name = input("Enter the blog name:  ")
    dog_id = input("Enter the id of the dog:  ")
    blog = Blog(blog_name, dog_id)
    blog.create_blog()
    print(f"Your Blog {blog_name} created.")

def delete_blog():
    id = input("Enter the id of the blog to delete: ")
    Blog.delete_blog(id)
    print(f"Blog with {id} deleted.")

def create_post():
    blog_id = input("Enter the id of the blog:  ")
    date = input("Enter the date of the post: (MM-DD-YYYY): ")
    content = input("Enter the content of your post: ")
    post = Post(blog_id, date, content)
    post.create_post()
    print(f"Post created on {date}.")

def delete_post():
    id = input("Enter the id of the post to delete: ")
    Post.delete_post(id)
    print(f"Post with id {id} deleted.")

def get_blogs():
    blog_name = print(f"{blog_name}")
    Blog.blog_name.get_blogs()

def get_posts_by_blog():
    blog_list = Blog.blog_name.blog_post

def exit_program():
    print("Goodbye!")
    exit()
