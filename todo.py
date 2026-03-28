class TDL:
    def __init__(self):
        self.work = []

    def add_task(self, task):
        self.work.append(task)
        print("✅ Task added.")

    def display(self):
        if not self.work:
            print("No tasks available.")
            return
        
        print("\nYour Tasks:")
        for i in range(len(self.work)):
            print(f"{i + 1}. {self.work[i]}")   # Notice i+1 (user-friendly)

    def remove_task(self):
        if not self.work:
            print("No tasks to remove.")
            return
        
        self.display()  # show tasks first
        
        choice = input("👉 Select task number to remove: ")
        
        if not choice.isdigit():
            print("Invalid input")
            return
        
        index = int(choice) - 1  # convert to actual index
        
        if 0 <= index < len(self.work):
            removed = self.work.pop(index)
            print(f"❌ '{removed}' removed.")
        else:
            print("Invalid choice")


# MAIN PROGRAM
todo = TDL()

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo.add_task(task)

    elif choice == "2":
        todo.display()

    elif choice == "3":
        todo.remove_task()

    elif choice == "4":
        break

    else:
        print("Invalid choice")