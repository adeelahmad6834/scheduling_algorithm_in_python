

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


ready_queue = Queue()
waiting_queue = []
array_for_processes = []
executed_processes_array = []
io_waiting_time = 0
def scheduler(cpu_running_time, process):
    if process["quantum_time"] == 0:
        process["quantum_time"] = quantum_time
    index = 0
    for every_process in array_for_processes:
        if every_process["arrival_time"] <= cpu_running_time:
            ready_queue.enqueue(array_for_processes.pop(index))
        index += 1
    flag = "true"
    if process["remaining_burst_time"] == 0:
        process["finish_time"] = cpu_running_time
        executed_processes_array.append(process)
        flag = "false"
    elif process["io_time"] == 0:
        process["return_time"] = cpu_running_time + io_waiting_time
        process["io_time"] = io_time
        waiting_queue.append(process)
        flag = "false"

    for every_process in waiting_queue:
        index = 0
        if every_process["return_time"] <= cpu_running_time:
            ready_queue.enqueue(waiting_queue.pop(index))
        index += 1

    if flag == "true":
        ready_queue.enqueue(process)


print("\t\t\t\t Round Robin Algorithm")
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

while True:
    try:
        print "Enter I/O Time for Process(es)"
        io_time = int(input())
        break
    except:
        print("Wrong Input!!!")

while True:
    try:
        print "Enter I/O Waiting Time for Process(es)"
        io_waiting_time = int(input())
        break
    except:
        print("Wrong Input!!!")

while True:
    choice = input("Do you want to ADD io_based Process(es)? 1 for yes 0 for no: ")
    if choice == 1:
        try:
            print "Enter 0 for Even or 1 for Odd Process IO"
            even_or_odd = (int(input())) % 2
            break
        except:
            print("Wrong Input!!!")
    else:
        break

if count == 0 or count < 0:
    print("There's no any process!!!")
else:
    for process_no in range(1, count + 1):
        process = {"id": "None", "arrival_time": "None", "burst_time": "None", "start_time": "None",
                   "remaining_burst_time": "None", "finish_time": "None", "quantum_time": quantum_time, "io_time": "None", "return_time": "None"}
        process["id"] = process_no
        if choice == 1:
            if (process_no % 2) == even_or_odd:
                process["io_time"] = io_time
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

    first_process = array_for_processes[0]
    running_time = first_process["arrival_time"]
    ready_queue.enqueue(array_for_processes.pop(0))

    while True:
        if not ready_queue.isEmpty():
            running_process = ready_queue.dequeue()
            if running_process["start_time"] == "None":
                running_process["start_time"] = running_time
            if running_process["io_time"] == "None":
                if running_process["remaining_burst_time"] > running_process["quantum_time"]:
                    running_time += running_process["quantum_time"]
                    running_process["remaining_burst_time"] -= running_process["quantum_time"]
                else:
                    running_time += running_process["remaining_burst_time"]
                    running_process["remaining_burst_time"] -= running_process["remaining_burst_time"]
            else:
                if running_process["quantum_time"] <= running_process["io_time"]:
                    time_to_switch = running_process["quantum_time"]

                else:
                    time_to_switch = running_process["io_time"]
                if running_process["remaining_burst_time"] > time_to_switch:
                    running_time += time_to_switch
                    running_process["remaining_burst_time"] -= time_to_switch
                    running_process["quantum_time"] -= time_to_switch

                    running_process["io_time"] -= time_to_switch
                else:
                    running_time += running_process["remaining_burst_time"]
                    running_process["remaining_burst_time"] -= running_process["remaining_burst_time"]
            scheduler(running_time, running_process)
        else:
            if len(waiting_queue) > 0:
                running_time += 1
                for every_process in waiting_queue:
                    index = 0
                    if every_process["return_time"] <= running_time:
                        ready_queue.enqueue(waiting_queue.pop(index))
                    index += 1
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
