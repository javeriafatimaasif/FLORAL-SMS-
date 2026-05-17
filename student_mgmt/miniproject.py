# MENU LOOP
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    # ---------------- ADD TASK ----------------
    if choice == "1":
        task = input("Enter task: ")

        with open("tasks.txt", "a") as file:
            file.write(task + " | Pending\n")

        print("Task added!")

    # ---------------- VIEW TASKS ----------------
    elif choice == "2":
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()

            if not lines:
                print("No tasks found.")
            else:
                for i, line in enumerate(lines, 1):
                    print(i, line.strip())

        except FileNotFoundError:
            print("No file found. Add tasks first.")

    # ---------------- UPDATE TASK ----------------
    elif choice == "3":
        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines, 1):
            print(i, line.strip())

        choice_task = int(input("Enter task number to mark completed: "))

        lines[choice_task - 1] = lines[choice_task - 1].replace("Pending", "Completed")

        with open("tasks.txt", "w") as file:
            file.writelines(lines)

        print("Task updated!")

    # ---------------- DELETE TASK ----------------
    elif choice == "4":
        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines, 1):
            print(i, line.strip())

        choice_task = int(input("Enter task number to delete: "))

        del lines[choice_task - 1]

        with open("tasks.txt", "w") as file:
            file.writelines(lines)

        print("Task deleted!")

    # ---------------- EXIT ----------------
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")