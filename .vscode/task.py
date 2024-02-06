class Process:
    def __init__(self, tid, arrival_time, burst_time, priority):
        self.pid = tid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

    def __repr__(self):
        return f"Process(pid={self.tid}, arrival_time={self.arrival_time}, burst_time={self.burst_time}, priority={self.priority})"

def priority_scheduling(processes):
    
    processes.sort(key=lambda process: process.priority, reverse=True)

    # Create a ready queue
    ready_queue = []

    # Initialize the current time
    current_time = 0

    # While there are processes in the ready queue
    while ready_queue:
        # Get the process with the highest priority
        process = ready_queue.pop(0)

        # Execute the process
        current_time += process.burst_time

        # If the process is not finished, add it back to the ready queue
        if process.burst_time > 0:
            ready_queue.append(process)

    # Return the current time
    return current_time

# Example usage
processes = [
    Process(1, 0, 10, 3),
    Process(2, 1, 5, 2),
    Process(3, 2, 2, 1),
]

print(priority_scheduling(processes))