import sys
import json
from datetime import datetime

if len(sys.argv) < 2:
    print("Please provide a command. Example: taskly add/update/delete/list")
    sys.exit()

try:
    with open('tasks.json') as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []


def add_task():
    if len(sys.argv) < 3:
        print("Please input a valid task description")
        return
    task_id = len(tasks) + 1
    description = sys.argv[2]
    status = "to-do"
    now = datetime.now()
    createdAt = now.strftime("%a %b %d, %I:%M:%S %p")

    task = {
        "id": task_id,
        "description": description,
        "status": status,
        "created at": createdAt,
        "updated at": createdAt
    }

    tasks.append(task)

    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f"Task added successfully (ID: {task_id})")


def update_task():
    if len(sys.argv) < 4:
        print("Usage: taskly update <id> <new description>")
        return
    new_description = sys.argv[3]
    now = datetime.now()
    user_task_id = int(sys.argv[2])

    if not any(task['id'] == user_task_id for task in tasks):
        print(f"Task {user_task_id} not found.")
        return

    for task in tasks:
        if task["id"] == int(user_task_id):
            task['description'] = new_description
            task['updated at'] = now.strftime("%a %b %d, %I:%M:%S %p")

    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f"Task updated successfully (ID: {user_task_id})")


def delete_task():
    global tasks
    if len(sys.argv) < 3:
        print("Usage: taskly delete <id>")
        return
    user_task_id = int(sys.argv[2])
    if not any(task['id'] == user_task_id for task in tasks):
        print(f"Task {user_task_id} not found.")
        return

    tasks = [task for task in tasks if task['id'] != user_task_id]

    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f"Task deleted successfully (ID: {sys.argv[2]})")


def mark_task(status):
    if len(sys.argv) < 3:
        print("Usage: taskly mark-in-progress/mark-done/mark-to-do <id>")
        return
    user_task_id = int(sys.argv[2])
    now = datetime.now()
    for task in tasks:
        if task['id'] == user_task_id:
            task['status'] = status
            task['updated at'] = now.strftime("%a %b %d, %I:%M:%S %p")

    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

    print(f"Task status updated successfully (ID: {sys.argv[2]})")


def list_tasks():
    if len(sys.argv) == 2:
        if not tasks:
            print(f"No tasks found")
        else:
            print(json.dumps(tasks, indent=4))

    elif len(sys.argv) == 3:
        filtered = [task for task in tasks if task['status'] == sys.argv[2]]
        if not filtered:
            print(f"No {sys.argv[2]} tasks found")
        else:
            print(json.dumps(filtered, indent=4))


user_action = sys.argv[1]

if user_action == 'add':
    add_task()

elif user_action == 'update':
    update_task()

elif user_action == 'delete':
    delete_task()

elif user_action == 'mark-in-progress':
    mark_task('in-progress')
elif user_action == 'mark-done':
    mark_task('done')
elif user_action == 'mark-to-do':
    mark_task('to-do')

elif user_action == 'list':
    list_tasks()

else:
    print("Unknown command. Valid commands: add, update, delete, mark-in-progress, mark-done, list")
