# Function to calculate average waiting time and average turnaround time for First-Come-First-Serve (FCFS) scheduling
def calculate_fcfs_average_times(processes, n):
    # Initialize variables to store waiting time and turnaround time
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time for the first process (it's always 0)
    waiting_time[0] = 0

    # Calculate waiting time for the rest of the processes
    for i in range(1, n):
        waiting_time[i] = processes[i - 1][2] + waiting_time[i - 1]

    # Calculate turnaround time for all processes
    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]

    # Calculate average waiting time and average turnaround time
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    return average_waiting_time, average_turnaround_time

# Function to calculate average waiting time and average turnaround time for Shortest Job First (SJF) scheduling
def calculate_sjf_average_times(processes, n):
    # Sort processes based on burst time (shortest job first)
    processes.sort(key=lambda x: x[2])

    # Initialize variables to store waiting time and turnaround time
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time for the first process (it's always 0)
    waiting_time[0] = 0

    # Calculate waiting time for the rest of the processes
    for i in range(1, n):
        waiting_time[i] = processes[i - 1][2] + waiting_time[i - 1]

    # Calculate turnaround time for all processes
    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]

    # Calculate average waiting time and average turnaround time
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    return average_waiting_time, average_turnaround_time

# Function to calculate average waiting time and average turnaround time for Priority Scheduling
def calculate_priority_average_times(processes, n):
    # Sort processes based on priority (higher priority first)
    processes.sort(key=lambda x: x[3], reverse=True)

    # Initialize variables to store waiting time and turnaround time
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time for the first process (it's always 0)
    waiting_time[0] = 0

    # Calculate waiting time for the rest of the processes
    for i in range(1, n):
        waiting_time[i] = processes[i - 1][2] + waiting_time[i - 1]

    # Calculate turnaround time for all processes
    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]

    # Calculate average waiting time and average turnaround time
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    return average_waiting_time, average_turnaround_time

# Function to calculate average waiting time and average turnaround time for Round-Robin (RR) scheduling
def calculate_rr_average_times(processes, n, time_quantum):
    # Initialize variables to store waiting time and turnaround time
    waiting_time = [0] * n
    turnaround_time = [0] * n

    remaining_time = [processes[i][2] for i in range(n)]
    current_time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > time_quantum:
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum
                else:
                    current_time += remaining_time[i]
                    waiting_time[i] = current_time - processes[i][2]
                    remaining_time[i] = 0

        if done:
            break

    # Calculate turnaround time for all processes
    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]

    # Calculate average waiting time and average turnaround time
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    return average_waiting_time, average_turnaround_time

# Function to find the scheduling algorithm with the least average waiting time and average turnaround time
def find_least_avg_times(processes, n, time_quantum):
    avg_waiting_times = {}
    avg_turnaround_times = {}

    # Calculate average waiting time and average turnaround time for each scheduling algorithm
    avg_waiting_time_fcfs, avg_turnaround_time_fcfs = calculate_fcfs_average_times(processes, n)
    avg_waiting_times['FCFS'] = avg_waiting_time_fcfs
    avg_turnaround_times['FCFS'] = avg_turnaround_time_fcfs

    avg_waiting_time_sjf, avg_turnaround_time_sjf = calculate_sjf_average_times(processes, n)
    avg_waiting_times['SJF'] = avg_waiting_time_sjf
    avg_turnaround_times['SJF'] = avg_turnaround_time_sjf

    avg_waiting_time_ps, avg_turnaround_time_ps = calculate_priority_average_times(processes, n)
    avg_waiting_times['Priority Scheduling'] = avg_waiting_time_ps
    avg_turnaround_times['Priority Scheduling'] = avg_turnaround_time_ps

    avg_waiting_time_rr, avg_turnaround_time_rr = calculate_rr_average_times(processes, n, time_quantum)
    avg_waiting_times['Round-Robin'] = avg_waiting_time_rr
    avg_turnaround_times['Round-Robin'] = avg_turnaround_time_rr

    # Find the scheduling algorithm with the least average waiting time and average turnaround time
    least_avg_waiting_time_algo = min(avg_waiting_times, key=avg_waiting_times.get)
    least_avg_turnaround_time_algo = min(avg_turnaround_times, key=avg_turnaround_times.get)

    return least_avg_waiting_time_algo, least_avg_turnaround_time_algo

# Input
n = int(input("Enter the number of processes: "))
processes = []
time_quantum = 0

for i in range(n):
    arrival_time = int(input(f"Enter arrival time for Process {i + 1}: "))
    burst = int(input(f"Enter burst time for Process {i + 1}: "))
    priority = int(input(f"Enter priority for Process {i + 1}: "))
    processes.append((i + 1, arrival_time, burst, priority))

time_quantum = int(input("Enter the time quantum for Round-Robin scheduling: "))

least_avg_waiting_time_algo, least_avg_turnaround_time_algo = find_least_avg_times(processes, n, time_quantum)

# Output the results
print("Scheduling Algorithm with Least Average Waiting Time:", least_avg_waiting_time_algo)
print("Scheduling Algorithm with Least Average Turnaround Time:", least_avg_turnaround_time_algo)
