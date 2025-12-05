from task_manager import TaskManager

def main():
    task_manager = TaskManager()

    while True:
        print("\n==== Student Task Tracker ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_manager.add_task()
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_manager.update_task()
        elif choice == '4':
            task_manager.delete_task()
        elif choice == '5':
            task_manager.save_to_file()
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please select between(1-5).")

main()