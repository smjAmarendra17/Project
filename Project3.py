class Task:
    def __init__(self, id, title, description, status):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}, Status: {self.status}"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self):
        id = len(self.tasks) + 1
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        status = input("Enter task status (Open/Closed): ")
        task = Task(id, title, description, status)
        self.tasks.append(task)
        print("Task created successfully!")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self):
        id = int(input("Enter task ID to update: "))
        for task in self.tasks:
            if task.id == id:
                task.title = input("Enter new task title: ")
                task.description = input("Enter new task description: ")
                task.status = input("Enter new task status (Open/Closed): ")
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self):
        id = int(input("Enter task ID to delete: "))
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found.")

def main():
    task_manager = TaskManager()
    while True:
        print("\n1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task_manager.create_task()
        elif choice == "2":
            task_manager.read_tasks()
        elif choice == "3":
            task_manager.update_task()
        elif choice == "4":
            task_manager.delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()