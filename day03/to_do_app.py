tasks = []

while True:
    choice = input("\n Choose 1,2 or 3 to continue\n 1. Add task\n 2. View tasks\n 3. Quit\n : ")
    if choice == "1":
        task = input("Enter to do : ").strip()
        tasks.append(task)
    
    elif choice  == "2":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.capitalize()}")
        if not tasks:
            print("No task yet!")

    elif choice == "3":
        print("App Closed!")
        break

    else:
        print("Invalid Choice")
        
