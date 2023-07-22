# Initialize an empty list to store tasks
to_do_list = []

def add_task(task):
    # Add a new task to the to-do list
    to_do_list.append(task)
    print(f"Task '{task}' has been added to the list.")

def view_tasks():
    # View the list of tasks
    if to_do_list:
        print("Here are your tasks:")
        for index, task in enumerate(to_do_list, 1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

def mark_completed(task_index):
    # Mark a task as completed
    if 1 <= task_index <= len(to_do_list):
        task = to_do_list[task_index - 1]
        print(f"Task '{task}' has been marked as completed.")

        to_do_list.pop(task_index - 1)
    else:
        print("Invalid task index.")

def delete_task(task_index):
    # Delete a task from the list
    if 1 <= task_index <= len(to_do_list):
        task = to_do_list[task_index - 1]
        print(f"Task '{task}' has been deleted.")
        to_do_list.pop(task_index - 1)
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nWhat do you want to do?")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task you want to add: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the index of the task you want to mark as completed: "))
            mark_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the index of the task you want to delete: "))
            delete_task(task_index)
        elif choice == "5":
            print("Thank you for using the To-Do List application. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()
