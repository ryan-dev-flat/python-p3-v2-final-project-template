# lib/cli.py

from helpers import (
    exit_program,
    create_dog,
    delete_dog,
    create_post,
    delete_post,
    get_blogs,
    get_posts_by_blog,
    get_all_posts
)


def main():
    actions = {
        "0": exit_program,
        "1": create_dog,
        "2": delete_dog,
        "3": create_post,
        "4": delete_post,
        "5": get_blogs,
        "6": get_posts_by_blog,
        "7": get_all_posts
    }

    while True:
        menu()
        choice = input("> ")
        if action := actions.get(choice):
            action()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a Dog Blog Account")
    print("2. Delete a Dog Blog Account")
    print("3. Create a Blog Post")
    print("4. Delete a Blog Post")
    print("5. Get a list of Blogs")
    print("6. Get a list Posts by Blog")
    print("7. Get a List of All Posts")

if __name__ == "__main__":
    main()
