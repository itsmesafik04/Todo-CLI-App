FILE_NAME = "tasks.txt"


# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        # Remove extra newline characters
        tasks = [task.strip() for task in tasks]
        return tasks

    except FileNotFoundError:
        return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# View all tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available.")

    else:
        print("\n===== TO-DO LIST =====")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# Add a new task
def add_task(tasks):
    task = input("\nEnter new task: ")

    if task.strip() == "":
        print("Task cannot be empty.")

    else:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")


# Remove a task
def remove_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully.")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            print("Exiting To-Do List App.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the application
main()