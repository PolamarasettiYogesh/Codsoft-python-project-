def to_do_list(): 
    tasks = []

    while True:
        print("\n1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            t = input("Enter the task: ")
            tasks.append(t)

        elif choice == "2":
            t = input("Enter the task to remove: ")
            if t in tasks:
                tasks.remove(t)
                print("Task removed.")
            else:
                print("Task not found.")

        elif choice == "3":
            print("\nTasks:")
            if not tasks:
                print("No tasks available.")
            else:
                for task in tasks:
                    print("- " + task)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

to_do_list()