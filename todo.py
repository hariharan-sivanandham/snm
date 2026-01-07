tasks = []   

while True:
    print("\n--- TO DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

   
    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

   
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to delete: "))
            if num >= 1 and num <= len(tasks):
                removed_task = tasks.pop(num - 1)
                print("Deleted task:", removed_task)
            else:
                print("Invalid task number.")

    
    elif choice == "4":
        print("Thank you! Exiting program.")
        break

   
    else:
        print("Invalid choice. Please try again.")
