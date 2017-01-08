print("\t\t\t\tFirst come First serve Algo")
count = int(input("Enter count of processes: "))
arrival_time = []
burst_time = []
start_time = []
int(count)

for process in range(1, count + 1):
    print("Enter Arrival Time of Process ", process)
    arrival_time.append(int(input()))
    print("Enter Burst Time of Process ", process)
    burst_time.append(int(input()))

running_time = arrival_time[0]
for process in range(0, count):
    start_time.append(running_time)
    running_time += burst_time[process]
    average_waiting_time = 0

for process in range(0, count):
    waiting_time = start_time[process] - arrival_time[process]
    average_waiting_time += waiting_time
    total_average_time = start_time[process]+burst_time[process]-arrival_time[process]
    print("Waiting Time of Process ", (process+1), " is ", waiting_time)
    print("Total Average Time of Process ", (process+1), " is ", total_average_time)
    print("\n")

print("Average Waiting Time is: ", (average_waiting_time / count))
print("CPU Running Time is: ", running_time)

