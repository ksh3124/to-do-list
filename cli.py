import store_data
import logic

def add_task(tasks):
    task = input("Enter task name to add: ")
    tasks[task] = False
    print("Task added.")

def view_tasks(tasks):
    task_list = logic.view_task(tasks)
    if not tasks:
        print("No tasks entered.")
    else:
        for task, status in task_list:
            print(f"{task} : {'Done' if status else 'Not Done'}")

def edit_task(tasks):
    task = input("Enter task name to edit: ")
    status = input("Is task done? (true/false): ").lower() == "true"
    result = logic.edit_tasks(tasks,task,status)
    if result:
        print("Task edited.")
    else:
        print("Task not found.")

def delete_task(tasks):
    task = input("Enter task name to delete: ")
    result = logic.delete_tasks(tasks,task)
    if result:
        print("Task deleted.")
    else:
        print("Task not found.")

def main():
    print("To-Do App")
    tasks = store_data.load_tasks()
    option = -1

    while option != 0:
        print("\nWhat would you like to do?")
        print("1. View tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Delete task")
        print("0. Exit")

        try:
            option = int(input("Enter option number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1: #view
            view_tasks(tasks)

        elif option == 2: #add
            add_task(tasks)

        elif option == 3: #edit
            edit_task(tasks)

        elif option == 4: #delete
            delete_task(tasks)

        elif option == 0: #exit app
            store_data.save_tasks(tasks)
            print("Exiting application.")

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
