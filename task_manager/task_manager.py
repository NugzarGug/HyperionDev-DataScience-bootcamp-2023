# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    task_list.append(curr_t)
    
    #====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True
        
# Defines function which if the user is an admin they can display statistics about number
# of users and tasks. It opens and displays files task_overiview.txt and user_overview.txt
# if not have this files, it runs function gen_stat for generating it
def disp_stat():
        
    if not os.path.exists("task_overview.txt" or 'user_overview.txt'):
        gen_stat()    
    with open('task_overview.txt','r') as task_overview:
        x = task_overview.read()
        print(f'\n{x}')
    with open('user_overview.txt','r') as user_overview:
        y = user_overview.read()
        print(f'\n{y}')
# Defines function which allows user to see all tasks which assigns to him 
# and edit completion of the task, name of the user, and date of the task 
def view_mine():
    #counter for tasks   
    task_counter = 0
 # Checks tasks for current user and prints it on display
    for t in task_list:
            if t['username'] == curr_user:
                disp_str = f"Task: Nr {task_counter} \t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                if curr_t["completed"] == True:
                    disp_str += f"Task completed: \t Yes\n"
                else:
                    disp_str += f"Task completed: \t No\n"                 
                disp_str += f"Task Description: \n {t['description']}\n"                
                print(disp_str)
                task_counter +=1
    # Asks user if he want to change completion of the task or user name or enter new task date         
    answer = False
    while answer != True:
        task_number = int(input('Please enter the number of the task or enter "-1" for return to main menu: '))
        if task_number == -1:
            answer = True
            break
        else:
            task = task_list[task_number]
            edit_choice = input('Do you want to change completion of the work or edit the task (C for change, E for Edit:) ').lower()
            if edit_choice == 'c':
                task['completed'] = True
                print('\nTask changed to completed')
                break
            if edit_choice == 'e':
                edit_change1 = input('Do you want to edit "user name" or "task date" (N for edit name, T for task date ): ').lower()
            if edit_change1 == 'n':
                new_user_name = input('Please enter the new user name: ')
                task['username'] = new_user_name
            if edit_change1 == 't' and task['completed'] != 'Yes':
                new_date = input('Please enter the new date in YYYY-MM-DD format: ')
                new_date = datetime.strptime(new_date,DATETIME_STRING_FORMAT)           
                
            else:
                print('Your task is already completed !')
                return
# Defines function which generates statistics for admin user               
def gen_stat():
    # num_tasks - number of all tasks
    num_tasks = len(task_list)
    num_users = len(username_password.keys())
    # calculates completed tasks
    num_completed_tasks = 0
    for t in task_list:
        if t['completed'] == True:
            num_completed_tasks +=1
    overdyed_tasks = 0
    # calculates uncompleted tasks
    num_uncompleted_tasks = num_tasks - num_completed_tasks
    # calculates tasks which are overdyed
    for t in task_list:
        if t['completed'] == False and t['due_date'].strftime(DATETIME_STRING_FORMAT) <\
            datetime.today().strftime(DATETIME_STRING_FORMAT):
            overdyed_tasks += 1
    # calculates percent overdyed tasks
    percent_overdue_tasks = round(overdyed_tasks / num_tasks,2) * 100
    #calculates percent incompleted tasks
    percent_inc_tasks = round(num_uncompleted_tasks/num_tasks,2) * 100
    
    # writes data to the file
    with open('task_overview.txt', 'w+') as task_overview:
        task_overview.write(f'The total number of tasks is:                          {num_tasks}\n'
                            f'The total number of completed tasks is:                {num_completed_tasks}\n'
                            f'The total number of uncompleted tasks is:              {num_uncompleted_tasks}\n'
                            f'The total number of uncompleted and overdyed tasks is: {overdyed_tasks}\n'
                            f'The percentage of incomplete tasks:                    {percent_inc_tasks}%\n'
                            f'The percentage of tasks that are overdue is:           {round(percent_overdue_tasks,2)}%\n')
   
    # Creates dictionary and calculates tasks for every user
    task_count = {}
    for task in task_list:
        username = task['username']
        if username in task_count:
            task_count[username] +=1
        else:
            task_count[username] = 1
    # Creates dictionary and calculates completed tasks for every user
    task_completed ={}
    for task in task_list:
        username = task['username']
        if task['completed'] == True:
            task_completed[username] +=1
        else:
            task_completed[username] = 0       
    # Creates dictionary and calculates overdued tasks for every user
    task_overdyed = {}
    for task in task_list:
        username = task['username']
        due_date = task['due_date']
        if username not in task_overdyed:
            task_overdyed[username] = 0
        if task['completed'] == False and due_date.strftime(DATETIME_STRING_FORMAT) <\
            datetime.today().strftime(DATETIME_STRING_FORMAT):
                if username in task_overdyed:
                    task_overdyed[username] += 1
                else:
                    task_overdyed[username] = 0
        
    # writes data to the file
    with open('user_overview.txt', 'w+') as user_overview:
        del user_overview
    for username, count in task_count.items():
        if task_overdyed[username] == 0:
            with open('user_overview.txt','a+') as user_overview:
                user_overview.write(f'----------------------------------------------------------\n'
                                    f'{username} have tasks: {count}\n'
                                    f'{username} has been assigned: {round(count/len(task_list)*100, 2)}% of all tasks\n'
                                    f'{username} has completed tasks: {task_completed[username]/count * 100}%\n'
                                    f'{username} have uncompleted tasks: {(1- task_completed[username]/count) * 100}%\n'
                                    f'{username} have no overdyed tasks\n'
                                    f'----------------------------------------------------------\n')
        else:
            with open('user_overview.txt','a+') as user_overview:
                user_overview.write(f'----------------------------------------------------------\n'
                                    f'{username} have tasks: {count}\n'
                                    f'{username} has been assigned: {round(count/len(task_list)*100, 2)}% of all tasks\n'
                                    f'{username} has completed tasks: {task_completed[username]/count * 100}%\n'
                                    f'{username} have uncompleted tasks: {(1- task_completed[username]/count) * 100}%\n'
                                    f'{username} overdue tasks are: {task_overdyed[username]/task_count[username] * 100}%\n'
                                    f'----------------------------------------------------------\n')
           
               
      
    
    
# Defines function for user registration
def reg_user():
    user_done = False
    while not user_done:
        
    # - Request input of a new username
        new_username = input("New Username: ")
        # Checks if user name is in the file
        if new_username in username_password.keys():
            print('This user is already added ! Please enter a new name')
            continue
        elif new_username not in username_password.keys():
            # - Request input of a new password
            new_password = input("New Password: ")
            # - Request input of password confirmation.
            confirm_password = input("Confirm Password: ")
            # - Check if the new password and confirmed password are the same.
            if new_password == confirm_password:
                # - If they are the same, add them to the user.txt file,
                print("New user added")
                username_password[new_username] = new_password
                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                        out_file.write("\n".join(user_data))
                user_done = True

            
        
            # - Otherwise you present a relevant message.
            else:
                print("Passwords do no match")
# Defines function which display all users and tasks
def view_all():
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        if t["completed"] == True:
            disp_str += f"Task completed: \tYes\n"
        else:
            disp_str += f"Task completed: \t No\n" 
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
        
       
# Defines function for adding new task       
def add_task():
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
    Include 'No' to indicate if the task is complete.'''
    new_task = {
         "username": task_username,
         "title": task_title,
         "description": task_description,
         "due_date": due_date_time,
         "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")
# Defines function which saves changes in tasks.txt file and closes the programm
def programm_exit():
     with open("tasks.txt", "w+") as task_file:
                task_list_to_write = []
                for t in task_list:
                    str_attrs = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                    ]   
                    task_list_to_write.append(";".join(str_attrs))
                task_file.write("\n".join(task_list_to_write))
     print('Goodbye!!!')
     exit()
            
if curr_user == 'admin':
    while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        print()
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()

    


        if menu == 'r':
            reg_user()

        elif menu == 'a':
            '''Allow a user to add a new task to task.txt file
                Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.'''
            add_task()

        elif menu == 'va':
            '''Reads the task from task.txt file and prints to the console in the 
               format of Output 2 presented in the task pdf (i.e. includes spacing
               and labelling) 
            '''
            view_all()
     


        elif menu == 'vm':
            '''Reads the task from task.txt file and prints to the console in the 
               format of Output 2 presented in the task pdf (i.e. includes spacing
               and labelling)
            '''
            view_mine()                
    
        elif menu == 'ds' and curr_user == 'admin':
            disp_stat()
        elif menu == 'gr' and curr_user == 'admin':
            gen_stat() 
        elif menu == 'e':
            programm_exit()

        else:
            print("You have made a wrong choice, Please Try again")
else:
    while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        print()
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    ds - Display statistics
    e - Exit
    : ''').lower()
        if menu == 'r':
            reg_user()

        elif menu == 'a':
            '''Allow a user to add a new task to task.txt file
                Prompt a user for the following: 
                 - A username of the person whom the task is assigned to,
                 - A title of a task,
                 - A description of the task and 
                 - the due date of the task.'''
            add_task()

        elif menu == 'va':
            '''Reads the task from task.txt file and prints to the console in the 
                format of Output 2 presented in the task pdf (i.e. includes spacing
                and labelling) 
            '''
            view_all()
        elif menu == 'vm':
            '''Reads the task from task.txt file and prints to the console in the 
               format of Output 2 presented in the task pdf (i.e. includes spacing
               and labelling)
            '''
            view_mine()                
    
        elif menu == 'ds' and curr_user == 'admin':
            disp_stat()

        elif menu == 'e':
            programm_exit()
        else:
            print("You have made a wrong choice, Please Try again")