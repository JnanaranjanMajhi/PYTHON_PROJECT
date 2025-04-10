import os

FILE_NAME = "todo.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, 'w', encoding='utf-8').close()
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        for task in tasks:
            file.write(task + '\n')


def get_importance():
    levels = {'1': 'High', '2': 'Medium', '3': 'Low'}
    while True:
        print("\nSelect importance level:")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        choice = input("Enter choice (1-3): ").strip()
        if choice in levels:
            return levels[choice]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def add_task():
    task = input("Enter the task: ").strip()
    if task:
        importance = get_importance()
        tasks = load_tasks()
        tasks.append(f"☐ ({importance}) {task}")
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- Your To-Do List ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print("------------------------\n")

def mark_task_done():
    tasks = load_tasks()
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            if "☑" not in tasks[num-1]:
                tasks[num-1] = tasks[num-1].replace("☐", "☑", 1)
                save_tasks(tasks)
                print("Task marked as done.")
            else:
                print("Task already marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_all_tasks():
    confirm = input("Are you sure you want to delete all tasks? (y/n): ").lower()
    if confirm == 'y':
        save_tasks([])
        print("All tasks cleared.")
    else:
        print("Operation cancelled.")

def main():
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Clear All Tasks")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            clear_all_tasks()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
