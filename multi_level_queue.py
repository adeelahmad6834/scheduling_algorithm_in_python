

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print items,


fcfs_queue1 = Queue()
round_robin_queue2 = Queue()
fcfs_queue3 = Queue()

array_for_processes = []
executed_processes_array = []
running_time = -1

def scheduler(cpu_running_time):
    index = 0
    for every_process in array_for_processes:
        if every_process["arrival_time"] <= cpu_running_time:
            if every_process["burst_time"] < 4:
                fcfs_queue1.enqueue(array_for_processes.pop(index))
            elif process["burst_time"] >= 4 or process["burst_time"] < 7:
                round_robin_queue2.enqueue(array_for_processes.pop(index))
            else:
                fcfs_queue3.enqueue(array_for_processes.pop(index))
        index += 1



print("\t\t\t\t Mulit-level Queue Algorithm")
while True:
    try:
        count = int(input("Enter count of process(es): "))
        break
    except:
        print("Wrong Input!!!")

while True:
    try:
        print "Enter Quantum Time of CPU"
        quantum_time = int(input())
        break
    except:
        print("Wrong Input!!!")

if count == 0 or count < 0:
    print("There's no any process!!!")
else:
    for process_no in range(1, count + 1):
        process = {"id": "None", "arrival_time": "None", "burst_time": "None", "start_time": "None",
                   "remaining_burst_time": "None", "finish_time": "None", "quantum_time": quantum_time}
        process["id"] = process_no
        while True:
            try:
                print "Enter Arrival Time of Process ", process_no
                process["arrival_time"] = int(input())
                break
            except:
                print("Wrong Input!!!")

        while True:
            try:
                print "Enter Burst Time of Process ", process_no
                process["remaining_burst_time"] = process["burst_time"] = int(input())
                break
            except:
                print("Wrong Input!!!")

        array_for_processes.append(process)
    scheduler(0)
    while True:
        if not fcfs_queue1.isEmpty():
            running_process = fcfs_queue1.dequeue()

            if running_time == -1:
                running_time = running_process["arrival_time"]

            running_process["start_time"] = running_time
            running_time += running_process["burst_time"]
            running_process["finish_time"] = running_time
            executed_processes_array.append(running_process)

            scheduler(running_time)

        elif not round_robin_queue2.isEmpty():
            running_process = round_robin_queue2.dequeue()

            if running_time == -1:
                running_time = running_process["arrival_time"]

            if running_process["start_time"] == "None":
                running_process["start_time"] = running_time

            if running_process["remaining_burst_time"] > running_process["quantum_time"]:
                running_time += running_process["quantum_time"]
                running_process["remaining_burst_time"] -= running_process["quantum_time"]
            else:
                running_time += running_process["remaining_burst_time"]
                running_process["remaining_burst_time"] -= running_process["remaining_burst_time"]

            scheduler(running_time)

            if running_process["remaining_burst_time"] == 0:
                running_process["finish_time"] = running_time
                executed_processes_array.append(running_process)
            else:
                round_robin_queue2.enqueue(running_process)

        else:
            if not fcfs_queue3.isEmpty():
                running_process = fcfs_queue1.dequeue()

                if running_time == -1:
                    running_time = running_process["arrival_time"]

                running_process["start_time"] = running_time
                running_time += running_process["burst_time"]
                running_process["finish_time"] = running_time
                executed_processes_array.append(running_process)

                scheduler(running_time)
            else:
                break

    average_waiting_time = 0
    while True:
        if len(executed_processes_array) == 0:
            break
        else:
            process = executed_processes_array.pop()
            waiting_time = process["finish_time"] - process["burst_time"] - process["arrival_time"]
            average_waiting_time += waiting_time
            turn_around_time = process["finish_time"] - process["arrival_time"]

            print "Waiting Time of Process with ID: ", process["id"], " is ", waiting_time
            print "Turn Around Time of Process with ID: ", process["id"], " is ", turn_around_time
            print "\n"

    print "Average Waiting Time is: ", (average_waiting_time / count)
    print "CPU Burst Time is: ", running_time
