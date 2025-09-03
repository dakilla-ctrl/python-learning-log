import json
import os

# initialize list for tasks
tasks = []

while True:
    choice = input("\n Choose 1,2 or 3 to continue\n 1. Add task\n 2. View tasks\n 3. Quit\n : ")
    if choice == "1":
        task = input("Enter to do : ").strip()
        tasks.append(task)
        with open('to_do_file.json', 'a') as f:
            f.write(task + "\n")

    elif choice  == "2":

        with open('to_do_file.json', 'r') as f:
            tasks = f.read().splitlines()
        if not tasks:
            print("No task yet!")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.capitalize()}")



    elif choice == "3":
        print("App Closed!")
        break

    else:
        print("Invalid Choice")

