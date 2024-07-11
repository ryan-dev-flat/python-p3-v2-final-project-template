# lib/cli.py

from helpers import (
    exit_program,
    create_dog,
    delete_dog,
    display_all_dogs,
    find_dog_by_id,
    create_post,
    delete_post,
    display_all_posts,
    find_post_by_id,
    display_posts_by_dog
)

def main():
    actions = {
        "0": exit_program,
        "1": create_dog,
        "2": delete_dog,
        "3": display_all_dogs,
        "4": find_dog_by_id,
        "5": create_post,
        "6": delete_post,
        "7": display_all_posts,
        "8": find_post_by_id,
        "9": display_posts_by_dog
    }

    while True:
        menu()
        choice = input("> ")
        if action := actions.get(choice):
            action()
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("Welcome to Dog Blogs!")
    print("_________________________________________")
    print("\nPlease select an option:")
    print("")
    print("0. Exit the program")
    print("1. Create a Dog Blog Account")
    print("2. Delete a Dog Blog Account")
    print("3. Display all Dog Blogs")
    print("4. Find a Dog Blog by ID")
    print("5. Create a Blog Post")
    print("6. Delete a Blog Post")
    print("7. Display all Posts")
    print("8. Find a Post by ID")
    print("9. Display Posts by Dog")

if __name__ == "__main__":
    main()