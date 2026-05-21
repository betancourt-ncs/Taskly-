Taskly — CLI Task Tracker
A simple command line task manager built with Python. Add, update, delete, and track the status of your tasks, all stored locally in a JSON file.


Requirements
Python 3


Setup
1. Clone or download the project

git clone https://github.com/betancourt-ncs/taskly.git

cd taskly

2. Create a terminal alias so you can run taskly from anywhere

echo 'alias taskly="python3 /full/path/to/main.py"' >> ~/.zshrc

source ~/.zshrc

Replace /full/path/to/main.py with the actual path to your file. You can find it by navigating to the project folder in your terminal and running pwd.


Usage
Add a task
taskly add "Buy groceries"

# Task added successfully (ID: 1)
Update a task description
taskly update 1 "Buy groceries and cook dinner"

# Task updated successfully (ID: 1)
Delete a task
taskly delete 1

# Task deleted successfully (ID: 1)
Mark a task as in progress
taskly mark-in-progress 1

# Task status updated successfully (ID: 1)
Mark a task as done
taskly mark-done 1

# Task status updated successfully (ID: 1)
Mark a task back to to-do
taskly mark-to-do 1

# Task status updated successfully (ID: 1)
List all tasks
taskly list
List tasks by status
taskly list to-do

taskly list in-progress

taskly list done


Task Properties
Each task is stored in tasks.json with the following fields:

Field
Description
id
Unique identifier, auto-incremented
description
Task description
status
to-do, in-progress, or done
created at
Timestamp when the task was created
updated at
Timestamp when the task was last modified



Notes
Tasks are stored in tasks.json in the project directory, created automatically on first use.
Task IDs are not reused after deletion.
Multi-word descriptions should be wrapped in quotes: taskly add "Walk the dog"

