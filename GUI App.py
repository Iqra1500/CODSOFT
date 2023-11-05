class Task:
    def __init__(self, name, due_date, description):
        self.name = name
        self.due_date = due_date
        self.description = description
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. Name: {task.name}, Due Date: {task.due_date}, Description: {task.description}, Completed: {task.completed}")

    # Implement other functions for marking tasks as complete, editing, and deleting tasks.

if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("Options:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Exit")
        choice = input("Enter an option: ")

        if choice == "1":
            name = input("Task name: ")
            due_date = input("Due date: ")
            description = input("Description: ")
            task = Task(name, due_date, description)
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            break
