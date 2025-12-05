import json
import os
import random
from datetime import datetime
from task import Task

class TaskManager:
    def __init__(self,filename ='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def load_from_file(self):
        if not os.path.exists(self.filename):
            self.tasks = []
            return 
        
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            self.tasks = []

            for item in data:
                task = Task(
                    id=item['id'],
                    title=item['title'],
                    description=item['description'],
                    created_at=item['created_at']
                )
                self.tasks.append(task)

        except:
            print("\nError loading tasks from file.")
            self.tasks = []

    def save_to_file(self):
        data = [task.to_dict() for task in self.tasks]
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_task(self):
        title = input("Task title: ")
        description = input("Task description: ")
        created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        task_id = random.randint(100, 999)
        new_task = Task(task_id, title, description, created_at)
        self.tasks.append(new_task)
        print("\nTask added successfully.")
        
        
    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return
        
        print("\n--- Task List ---")
        for task in self.tasks:
            print(f"ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Created_at: {task.created_at}")
            print("------------------------")

    def update_task(self):
        try:
            task_id = int(input("Enter Task ID to update: "))
        except:
            print("\nInvalid ID.")
            return
        for task in self.tasks:
            if task.id == task_id:
                new_title = input("New Task title: ")
                new_description = input("New description: ")

                if new_title:
                    task.title = new_title
                if new_description:
                    task.description = new_description

                print("\nTask updated successfully.")
                return

        print("\nTask not found.")

    def delete_task(self):
        try:
            task_id = int(input("Enter Task ID to delete: "))
        except:
            print("\nInvalid ID.")
            return
        
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print("\nTask deleted successfully.")
                return

        print("\nTask not found.")