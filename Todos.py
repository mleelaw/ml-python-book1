todo_list = []


def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added.")


def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")


def display_tasks():
    print("To-Do List:")
    for task in todo_list:
        print(f" - {task}")


add_task("Read a book")
add_task("Write some code")
add_task("Go for a walk")


display_tasks()


remove_task("Write some code")


display_tasks()
