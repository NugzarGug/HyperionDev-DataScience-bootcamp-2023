# Task Management Program

## Overview

This Python project provides a command-line interface for managing tasks. The script supports user registration, task addition, viewing tasks, and generating reports. It differentiates between regular users and administrators, with additional functionality available for admins.

## Features

- **Register User**: Create a new user with a unique username and password.
- **Add Task**: Assign tasks with details such as title, description, due date, and assigned user.
- **View All Tasks**: Display all tasks with their details.
- **View My Tasks**: Show tasks assigned to the logged-in user.
- **Generate Reports**: Admins can generate reports on task statistics and user activity.
- **Display Statistics**: Admins can view overall task statistics and user summaries.

## Requirements

- Python 3.x

## How to Use

1. **Clone the Repository**

   ```bash
   git clone https://github.com/NugzarGug/HyperionDev-DataScience-bootcamp-2023.git
Navigate to the Directory

Run the Script

bash
Copy code
python task_manager.py

## Login
- **Username:**  admin
- **Password:** password
- *Other users need to register first.*

## Menu Options

- *r:* Register a new user.
- *a:* Add a new task.
- *va:* View all tasks.
- *vm:* View tasks assigned to you.
- *ds:* Display statistics (admin only).
- *gr:* Generate and view reports (admin only).
- *e:* Exit the program.
## Script Overview
File Management: Uses tasks.txt for storing tasks and user.txt for user credentials.
Functions:
- *reg_user():* Registers a new user.
- *add_task():* Adds a new task.
- *view_all():* Displays all tasks.
- *view_mine():* Displays tasks assigned to the logged-in user.
- *gen_stat():* Generates task and user statistics.
- *disp_stat():* Displays statistics for admins.
- *programm_exit():* Saves changes and exits the program.

## Contact

- **Email**: nugzargug@gmail.com
- **GitHub**: [NugzarGug](https://github.com/NugzarGug)
