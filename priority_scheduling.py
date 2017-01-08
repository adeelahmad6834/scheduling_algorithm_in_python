running_time = 0
process_array = []
executed_process_array = []



def next_ready_process(cpu_running_time):
    current_ready_process = process_array[0]
    index = 0
    current_index = 0
    for every_process in process_array:
        if every_process["arrival_time"] <= cpu_running_time:
            if every_process["remaining_burst_time"] <= current_ready_process["remaining_burst_time"]:
                if every_process["priority_number"] < current_ready_process["priority_number"]:
                    current_ready_process = every_process
                    index = current_index
        current_index += 1
    process_array.pop(index)
    return current_ready_process


print("\t\t\t\t Shortest Remaining Time First")
while True:
    try:
        count = int(input("Enter count of process(es): "))
        break
    except:
        print("Wrong Input!!!")
if count == 0 or count < 0:
    print("There's no any process!!!")
else:
    for process_no in range(1, count + 1):
        process = {"id": "None", "arrival_time": "None", "burst_time": "None", "start_time": "None",
                   "remaining_burst_time": "None", "finish_time": "None", "priority_number": "None"}
        process["id"] = process_no

        while True:
            try:
                print "Enter Priority Number of Process ", process_no
                process["priority_number"] = int(input())
                break
            except:
                print("Wrong Input!!!")

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
        process_array.append(process)

    ready_process = next_ready_process(0)
    running_time = ready_process["arrival_time"]
    while True:
        if len(process_array) >= 0:
            running_time += 1
            if ready_process["start_time"] == "None":
                ready_process["start_time"] = running_time
            ready_process["remaining_burst_time"] -= 1
            if ready_process["remaining_burst_time"] == 0:
                ready_process["finish_time"] = running_time
                executed_process_array.append(ready_process)
            else:
                process_array.insert(0, ready_process)
            if len(process_array) > 0:
                ready_process = next_ready_process(running_time)
            else:
                break
        else:
            break

    average_waiting_time = 0
    while True:
        if len(executed_process_array) == 0:
            break
        else:
            process = executed_process_array.pop()
            waiting_time = process["finish_time"] - process["burst_time"] - process["arrival_time"]
            average_waiting_time += waiting_time

            print "Waiting Time of Process with ID: ", process["id"], " is ", waiting_time
            print "Finish  Time of Process with ID: ", process["id"], " is ", process["finish_time"]
            print "\n"
    print "Average Waiting Time is: ", (average_waiting_time / count)
    print "CPU Burst Time is: ", running_time
