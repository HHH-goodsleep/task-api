
from storage import load_tasks, save_tasks

tasks = load_tasks()
# tasks = []

def add_task(task_title, description=""):
    task = {
        "id": len(tasks) + 1,
        "title": task_title,
        "description": description,
        "done": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task['title']}")
    return task

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "Done" if task["done"] else "Not Done"
        print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {status}")

def mark_task_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Task marked as done: {task['title']}")
            return task
    save_tasks(tasks)
    print(f"Task with ID {task_id} not found.")
    return None

def delete_task(task_id):
    global tasks
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task deleted: {task['title']}")
            return task
    save_tasks(tasks)
    print(f"Task with ID {task_id} not found.")
    return None

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            add_task(title, description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as done: "))
            mark_task_done(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            print("Exiting Task Manager.Bye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()