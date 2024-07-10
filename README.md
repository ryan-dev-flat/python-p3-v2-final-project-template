
---

# Dog Blog CLI Application

This Python CLI application allows users to manage dog blogs and posts. The application uses an SQLite database to store data, and provides a command-line interface for users to interact with the data.

## Project Structure

The project is organized into several Python files:

- `models/__init__.py`: This file sets up the SQLite database and provides a cursor for executing SQL commands.
- `models/dog.py`: This file defines the `Dog` class, which represents a dog with a blog. The class includes methods for creating and deleting dogs, and finding dogs by id.
- `models/post.py`: This file defines the `Post` class, which represents a blog post. The class includes methods for creating and deleting posts, and finding posts by id or by dog.
- `helpers.py`: This file provides functions for interacting with `Dog` and `Post` objects. These functions are used in the CLI to perform various operations such as creating and deleting dogs and posts.
- `cli.py`: This file provides the command-line interface for the application. It displays a menu of options to the user, gets the user's choice, and performs the chosen action.

## How to Use

To use the application, run the `cli.py` script. You will see a menu of options:

```
Please select an option:

0. Exit the program
1. Create a Dog Blog Account
2. Delete a Dog Blog Account
3. Display all Dog Blogs
4. Find a Dog Blog by ID
5. Create a Blog Post
6. Delete a Blog Post
7. Display all Posts
8. Find a Post by ID
9. Display Posts by Dog
```

Enter the number of the option you want to choose, and then follow the prompts.

## Requirements

This application requires Python 3 and SQLite.

---