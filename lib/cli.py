# lib/cli.py

from helpers import (
    exit_program,
    create_dog,
    delete_dog,
    create_blog,
    delete_blog,
    create_post,
    delete_post,
    get_blogs,
    get_posts_by_blog,
    get_all_posts
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_dog()
        elif choice == "2":
            delete_dog()
        elif choice == "3":
            create_blog()
        elif choice == "4":
            delete_blog()
        elif choice == "5":
            create_post()
        elif choice == "6":
            delete_post()
        elif choice == "7":
            get_blogs()
        elif choice == "8":
            get_posts_by_blog()
        elif choice == "9":
            get_all_posts()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a Dog Account")
    print("2. Delete a Dog Account")
    print("3. Create a Dog Blog")
    print("4. Delete a Dog Blog")
    print("5. Create a Blog Post")
    print("6. Delete a Blog Post")
    print("7. Get a list of Blogs")
    print("8  Get a list Posts by Blog")
    print("9. Get a List of All Posts")

if __name__ == "__main__":
    main()
