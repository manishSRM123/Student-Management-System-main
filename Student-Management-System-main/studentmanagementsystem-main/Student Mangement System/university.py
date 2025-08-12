import time
import pandas as pd

class Task:
    def __init__(self, task_name, priority, execution_time, task_type, dependencies=None, required_resources=None):
        self.task_name = task_name
        self.priority = priority
        self.execution_time = execution_time
        self.task_type = task_type
        self.dependencies = dependencies if dependencies is not None else []
        self.required_resources = required_resources if required_resources is not None else {}

class UniversityTaskProcessor:
    def __init__(self):
        self.task_queue = []
        self.task_records = []
        self.resources = {}

    def add_task(self, task):
        self.task_queue.append(task)

    def execute_priority(self):
        print("Executing tasks using Priority scheduling algorithm:")
        task_list = sorted(self.task_queue, key=lambda x: x.priority, reverse=True)
        for task in task_list:
            if self.check_dependencies(task):
                self.execute_task(task)
                self.task_records.append(task)
            else:
                print(f"Cannot execute {task.task_name} due to unfulfilled dependencies.")

    def check_dependencies(self, task):
        for dependency in task.dependencies:
            if dependency not in self.task_records:
                return False
        return True

    def execute_task(self, task):
        print(f"Processing {task.task_name} with priority {task.priority} for {task.execution_time} seconds.")
        if task.required_resources:
            self.allocate_resources(task.required_resources)
        time.sleep(task.execution_time)
        self.release_resources(task.required_resources)

    def allocate_resources(self, required_resources):
        for resource, count in required_resources.items():
            if resource in self.resources:
                if self.resources[resource] >= count:
                    self.resources[resource] -= count
                else:
                    print(f"Not enough {resource} available for the task.")

    def release_resources(self, required_resources):
        for resource, count in required_resources.items():
            if resource in self.resources:
                self.resources[resource] += count
            else:
                self.resources[resource] = count

    def display_task_records(self, algorithm_name) :
        df = pd.DataFrame(
            [(task.task_name, task.execution_time, task.priority, task.task_type) for task in self.task_records],
            columns=["Task Name", "Execution Time", "Priority", "Task Type"]
        )
        print(f"\nTask Processing Report - {algorithm_name}\n")
        print(df)

tasks = [
    Task("Registering for Courses", 2, 5, "Registration", dependencies=[], required_resources={'computers': 1, 'staff': 1}),
    Task("Paying Fees", 1, 3, "Finance", dependencies=[], required_resources={'accounts': 1, 'staff': 1}),
    Task("Scheduling Exams", 3, 4, "Exams", dependencies=[], required_resources={'rooms': 1, 'staff': 1}),
    Task("Research Project", 6, 6, "Research", dependencies=[], required_resources={'researchers': 1, 'staff': 1}),
    Task("Library Study", 8, 3, "Study", dependencies=[], required_resources={'study_spaces': 1, 'staff': 1}),
    Task("Group Discussion", 4, 4, "Discussion", dependencies=[], required_resources={'meeting_rooms': 1, 'staff': 1}),
]

task_processor = UniversityTaskProcessor()

for task in tasks:
    task_processor.add_task(task)

while True:
    algorithm_choice = input("Select the scheduling algorithm (PRIORITY) or 'exit' to exit: ").upper()

    if algorithm_choice == 'EXIT':
        break

    if algorithm_choice != 'PRIORITY':
        print("Invalid choice. Please select PRIORITY or exit.")
        continue

    task_processor.execute_priority()
    task_processor.display_task_records("Priority Scheduling")
    break
