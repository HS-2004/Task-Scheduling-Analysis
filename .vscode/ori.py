import time
import datetime

class Task:
    def __init__(self, name, start_time, end_time, priority):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.priority = priority

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"
    
    

    def run(self):
        print(f"Running task: {self.name}")


class Scheduler(Task):
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    

    def schedule(self):
        self.tasks.sort(key=lambda task: task.priority, reverse=True)
        for task in self.tasks:
            if task.start_time <= datetime.datetime.now():
                task.run()

class TaskAnalysis:
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def get_task_run_times(self):
        run_times = {}
        for task in self.scheduler.tasks:
            run_time = task.end_time - task.start_time
            run_times[task.name] = run_time
        return run_times

    def get_average_task_run_time(self):
        run_times = self.get_task_run_times()
        total_run_time = datetime.timedelta(seconds=0)

        for run_time in run_times.values():
            total_run_time += run_time
        average_run_time = total_run_time / len(run_times)
        return average_run_time

def main():
    scheduler = Scheduler()

    # Add tasks to the scheduler
    task1 = Task("Task 1", datetime.datetime(2024, 2, 28, 0, 0, 0), datetime.datetime(2024, 2, 28, 1, 0, 0), 1)
    task2 = Task("Task 2", datetime.datetime(2024, 2, 29, 1, 0, 0), datetime.datetime(2024, 2, 29, 3, 0, 0), 2)
    task3 = Task("Task 3", datetime.datetime(2024, 3, 1, 23, 0, 0), datetime.datetime(2024, 3, 2, 6, 15, 0), 3)

    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)

    # Schedule the tasks
    scheduler.schedule()

    # Analyze the tasks
    task_analysis = TaskAnalysis(scheduler)

    # Get the task run times
    run_times = task_analysis.get_task_run_times()

    # Get the average task run time
    average_run_time = task_analysis.get_average_task_run_time()

    # Print the results
    print("Task run times:")
    for task_name, run_time in run_times.items():
        print(f"{task_name}: {run_time}")

    print(f"Average task run time: {average_run_time}")

if __name__ == "__main__":
    main()