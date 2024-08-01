# Ebookstore Database Management

## Overview

This Python project provides a command-line interface to manage a bookstore database using SQLite. The script allows users to add, update, search, and delete book records in the database.

## Features

- **Add Book**: Add a new book with details such as ID, title, author, and quantity.
- **Update Book**: Update book information including ID, title, author, or quantity.
- **Search Book**: Search for books by ID, title, or author.
- **Delete Book**: Remove a book record from the database.

## Requirements

- Python 3.x
- `sqlite3` library (comes with Python)
- `prettytable` library (install via `pip install prettytable`)

## How to Use

1. **Clone the Repository**

   ```bash
   git clone https://github.com/NugzarGug/HyperionDev-DataScience-bootcamp-2023.git
Navigate to the Directory

bash
Copy code
cd path_to_cloned_directory
Run the Script

bash
Copy code
python your_script_name.py
Follow the Prompts to add, update, search, or delete book records.

Script Overview
Database Initialization: The script creates a SQLite database named ebookstore and a table named books if they do not exist.
Class Book: A class to represent book objects and create new book records.
Functions:
search(search_object, search_input): Searches the database for books based on title, ID, or author.
main_menu(): Displays the main menu options.
update_menu(): Displays options for updating book information.
## Contact

- **Email**: nugzargug@gmail.com
- **GitHub**: [NugzarGug](https://github.com/NugzarGug)
