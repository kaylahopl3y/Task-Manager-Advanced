# Everything works but I accidentally deleted everything in the tasks.txt file though :( 
# Import datetime for when the admin adds a task and needs to input a start & due date
import datetime

# Open both files (opened both as read only for now, will be opened as append or write when need be)
user_file = open('user.txt','r')
tasks_file = open('tasks.txt','r')

# This menu is only available to the admin. It allows the admin to register a user and display statistics
# Defined it as a function that will be called on later (two seperate menus were made so the user doesn't have all the options)
def adminMenu():
    print("r - register user")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("gr - generate reports")
    print("ds - display statistics")
    print("e - exit")
    print("\n")

# Depending on what the admin chooses to do it will call on a function that has been defined below. Also display a message when action completed
    ans=input("What would you like to do? ")
            
    if ans=="r":
        print("\n")
        reg_user()
                                     
    elif ans=="a":
        print("\n")
        add_task()
        print("\n")
        print("Thank you, you have successfully added a task")
                
    elif ans=="va":
        print("\n")
        view_all()
        print("\n")
        print("These are all the tasks in the file")
                                     
    elif ans=="vm":
        print("\n")
        view_mine()

    elif ans=="gr":
        print("\n")
        generate()
        print("\n")
        print("Reports generated")
                                         

    elif ans=="ds":
        print("\n")
        display_statistics()
        print("\n")
        print("Statistic display complete")
                                     
    elif ans == "e":
        print("\n")
        print("Goodbye!")
        quit()


# Only a registered user can access this menu. It does not allow them to register a user or see task/ user statistics 
def userMenu():
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("e - exit")
    print("\n")
    
    ans=input("What would you like to do? ")

    if ans=="a":
        print("\n")
        add_task()
        print("\n")
        print("Thank you, you have successfully added a task")
        
    elif ans=="va":
        print("\n")
        view_all()
        print("\n")
        print("These are all the tasks in the file")
                       
    elif ans=="vm":
        print("\n")
        view_mine()             
                      
    elif ans == "e":
        print("\n")
        print("Goodbye!")
        quit()
        

# This function allows the admin to register a user. Open file using 'a' for append so it does not write over any users already in the file
# Asks admin for the usermane and password. Will only register a user if the password and password confirmation match and if username doesnt exist already
# using write() to put this information into the txt file (always close file after) and .format so it printes neatly
def reg_user():
    user_file = open('user.txt','a')
    username = input("Please enter a new username: ")
    if username in userNames:
        print("Sorry this username already exists")
        reg_user()
    else:       
        password = input("Please enter your new password: ")
        confirm_password = input("Please confirm your new password: ")
        if password == confirm_password:
            print("\n")
            print("Thank you, you have successfully registered a user")
            user_file.write("\n{}, {}".format(username, password))
            user_file.close()
        else:
            print("Could not register - passwords do not match!")


# This function allows the admin or user to add a task. Open file using 'a' for append so it does not write over any users already in the file
# Asks for all information about the task then writes them to the txt file using write()
def add_task():
    task_file = open('tasks.txt','a')
    username = input("Please enter the username the task is assigned to: ")
    task_title = input("Please enter the title of the task: ")
    task_description = input("Please enter a description of the task: ")
    task_start = input("Please enter the date that this task was assigned: ")
    task_due = input("Please enter the due date of this task: ")
    task_completed = input("Please specifiy if the task has been completed by putting either 'Yes' or 'No': ")
    task_file.write("\n{}, {}, {}, {}, {}, {}" .format(username, task_title, task_description, task_start, task_due, task_completed))                              
    task_file.close()
                          
# This function allows all the contents of the task file to be printed out. Use 'r' as it is only being read 
def view_all():
    task_file = open('tasks.txt','r')
    content = task_file.read()
    print(content)
    task_file.close()
    
# This function searches for the username in everyline and only prints the lines that the username is found in
def view_mine():
    task_file = open('tasks.txt','r')
    all_tasks = task_file.readlines()
    
    num = 1
    task_count = 1
    all_tasks_copy = all_tasks.copy()
    user_tasks = []
    
# Displays the tasks with a number in a nice way    
    for line in all_tasks: 
      temp = line.strip()
      temp = temp.split(", ")
      if username in line:
          print("")
          print("{} Task User:    {}".format(num,temp[0]))
          print("   Task Name:    {}".format(temp[1]))
          print("   Task Description:    {}".format(temp[2]))
          print("   Date Assigned:    {}".format(temp[3]))
          print("   Due Date:    {}".format(temp[4]))
          print("   Completed Status:    {}".format(temp[5]))
          user_tasks.append(all_tasks_copy.pop(task_count - num))
          num += 1
      task_count += 1

    all_tasks = all_tasks_copy.copy()

# Create a menu that lets the user choose what they'd like to do to the task   
    print("\n")
    print("What would you like to do? ")
    print("\n")
    print("1 - mark the task as complete")
    print("2 - edit the task due date")
    print("-1 - return to previous menu")
    print("\n")
    
    ans = input("Please enter a number now: ")

# If user chooses to mark task as complete make sure the task number entered is valid and that is has not been completed already
# Call on mark_complete function
    if ans == "1":
        print("\n")
        choice = input("Select task using its number: ")
        choice = int(choice) - 1
        if choice > len(user_tasks) -1:
            print("\nNo task with that number")
        elif "Yes" in user_tasks[choice]:
            print("\nThis task is already completed")
        else: 
            mark_complete(all_tasks, choice, user_tasks)
            print("\nTask marked as complete")

# If user chooses to edit date call on the edit_date function 
    elif ans == "2":
        choice = input("Select task using its number: ")
        choice = int(choice) - 1        
        print("\n")
        edit_date(all_tasks, choice,username,user_tasks)
        print("New date has been saved")
        

# Returns to the main menu if the user enteres '-1'
    elif ans == "-1":
        print("\n")
        print("Please select one of the following options: ")
        print("\n")
        if username == "admin":
            adminMenu()
        else:
            userMenu()

# Define a function to mark tasks as complete 
def mark_complete(all_tasks, choice, user_tasks):
    user_tasks[choice] = user_tasks[choice].replace("No","Yes")
    
    task_file = open('tasks.txt','r')
    all_tasks = task_file.readlines()

    all_tasks.extend(user_tasks)

    all_tasks_sort = []
    for line in all_tasks:
        line = line.split(', ')
        all_tasks_sort.append(line)

    all_tasks_out = []
    all_tasks = sorted(all_tasks_sort, key = lambda x: datetime.datetime.strptime(x[3], "%d %b %Y"))
    for array in task_file:
        array = ", ".join(array)
        all_tasks.out.append(array)

    task_file = open('tasks.txt','a')
    task_file.writelines(all_tasks_out)
    task_file.close()

    

# Define a function to edit the date of a task
def edit_date(all_tasks, choice, usernames,user_tasks):   
    task_file = open('tasks.txt','r')
    all_tasks = task_file.readlines()

    edited_date = input("Please enter a new date: ")
    user_tasks[choice] = user_tasks[choice].split(', ')
    user_tasks[choice][4] = edited_date
    user_tasks[choice] = ', '.join(user_tasks[choice])

# Add new date back to main

    all_task_date = []
    all_task_date.extend(all_tasks)
    all_tasks_date.extend(user_tasks)

# Use the split function to turn lines to lists

    all_tasks_sorted = []
    for line in all_tasks_date:
        line = line.split(', ')
        all_tasks_sorted.append(line)

# Sorting the task output

    all_tasks_output = sorted(all_tasks_sorted,
    key = lambda x: datetime.datetime.strptime(x[3], "%d %b %Y"))
    all_tasks_output_date = []
    
    for array in all_tasks_output:
        array = ", ".join(array)
        all_tasks_output_date.append(array)
        
    task_file = open('tasks.txt','a')
    task_file.writelines(all_tasks_output_date)

    task_file.close()


# Define a function to generate reports and save to text files for the tasks and users
# Starting with tasks define counters to track all completed, uncompleted and overdue then assign conditions 
def generate():
    task_file = open('tasks.txt','r')
    user_file = open('user.txt','r')
    
    task_count = 0
    completed_counter = 0
    uncompleted_counter = 0
    overdue_counter = 0

    for line in task_file:
        line = line.replace("\n","")
        line = line.split(",")
        task_count += 1
        line[5] = line[5].replace(" ","")

        if line[5] == "Yes":
            completed_counter += 1 

        if line[5] == "No":
            uncompleted_counter += 1
            
    for line in task_file.readlines():
        line = line.split(',')
        due_date = datetime.datetime.strptime(line[4],"%d %b %Y")
        date = datetime.datetime.now()
        line = ', '.join(line)
        if date > due_date:
            overdue_counter += 1

# Calculate them as a percentage      

    percentage_incomplete = (uncompleted_counter / task_count) * 100
    percentage_overdue = (overdue_counter / task_count) * 100
    
# Create the task overview file and print all counters and calculations to it

    task_overview = open('task_overview.txt','w')
    task_overview.write("The total number of tasks is: " + str(task_count) + "\n"
                        "The total number of completed tasks is: " + str(completed_counter) + "\n"
                        "The total number of uncompleted tasks is: " + str(uncompleted_counter) + "\n"
                        "The total number of overdue tasks is: " + str(overdue_counter) + "\n"
                        "The percentage of incomplete tasks is: " + str(percentage_incomplete) + "\n"
                        "The percentage of overdue tasks is: " + str(percentage_overdue))
                            
    user_file = open('user.txt','r')

# Repeat for user overview    
    date = user_file.readlines()
    info = task_file.readlines()

    num_users = 0
    users = ""

    for lines in data:
        num_users += 1
        temp = lines.split(', ')
        users += temp[0] + " "

    users = users.split()
    total_users_list = []
    users_task_list = []
    comp_user_list = []
    incomp_user_list = []
    overdue_user_list = []

    for user in users:
        num_task_user = 0
        comp_user_num = 0
        incomp_user_num = 0
        overdue_user_num = 0

        for line in info:
            if user in line:
              num_task_user += 1
              if "Yes" in line:
                comp_user_num += 1
              if "No" in line:
                 incomp_user_num += 1
              if "No" in line and date > due_date:
                  overdue_user_num += 1

        if num_task_user > 0:
            
            percentage_user = (100 / task_count) * num_task_user
            percentage_comp = (100 / num_task_user) * comp_user_num
            percentage_incomp = (100 / num_task_user) * incomp_user_num
            percentage_overdue = (100 / num_task_user) * overdue_user_num
            
        else:
            
            percentage_user = 0
            percentage_comp = 0
            percentage_incomp = 0
            percentage_overdue = 0
            
    total_users_list.append(num_task_user)
    users_task_list.append(percentage_user)
    comp_user_list.append(percentage_comp)
    incomp_user_list.append(percentage_incomp)
    overdue_user_list.append(percentage_overdue)

    user_report_out = []

    user_report_out.append("Total users: " + str(num_users))
    user_report_out.append("Total tasks: " + str(task_count))     

    every_users_out = []
    count = 0
    
# Use append. for an empty list 
    for user in users:
        every_users_out.append(user)
        every_users_out.append("Tasks assigned: " + str(total_users_list))
        every_users_out.append("Tasks assigned out of all tasks: " + str(users_task_list))      
        every_users_out.append("Completed out of tasks assigned: " + str(comp_user_list))
        every_users_out.append("Incompleted out of tasks assigned: " + str(incomp_user_list))
        every_users_out.append("Overdue out of tasks assigned: " + str(overdue_user_list))
        
        count += 1
        
    user_overview = open('user_overview.txt','w')
    user_overview.write(str(user_report_out) + "\n")
    user_overview.write(str(every_users_out))

    task_file.close()
    task_overview.close()
    user_file.close()
    user_overview.close()


    
# Reads and prints out all information generated in the task and user overview files
def display_statistics():
    task_overview = open('task_overview.txt','r')
    user_overview = open('user_overview.txt','r')
    content = task_overview.read()
    data = user_overview.read()
    print("Task overview: ")
    print("\n")
    print(content)
    print("\n")
    print("User overview: ")
    print(data)
    
    task_overview.close()
    user_overview.close()


# userNames and userPass are the usernames and passwords already in the txt file. Define them as open strings
userNames = ""
userPass = ""

# they are saved in the file in the form 'username, password' so by removing the space and splitting by the comma
# allows us to say that the usermane will be found in index 0 and the password in index -1 (last position) 
for line in user_file:
    data = line.strip(' ')
    data = line.split(',')
    userNames += data[0]
    userPass += data[-1]

# ask the user to enter their username (If it does not match one in the txt file give an error message)
# without a valid username the user can't move on to the next step 
print("Welcome to your task manager, please login below")
username = input("Please enter your username: ")
if username not in userNames:
    print("This user does not exist!")

# once the username has been accepted ask them to enter their password. If it does not match give an error message
else:
    password = input("Please enter your password: ")    
    if password not in userPass: 
        print("Invalid password")

# when they have successfully loggen in print the menu by calling on the menu functions
# adminMenu() if the admins credentials were entered and userMenu() if not 
    else:
        print("You are now logged in")
        print("\n")
        print("Please select one of the following options: ")
        print("\n")
        if username == "admin":
            adminMenu()
        else:
            userMenu()

# close both files
user_file.close()
tasks_file.close()
