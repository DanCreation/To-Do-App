
lst = []

def task_data(name, description):
    lst.append({"name": name, "description" : description})
    print("\nTASKS:\n")
    for x in range(len(lst)):
        print("Task", x + 1, ": ", lst[x])

def add_task(task_name, task_description):
    #print("\nTASKS:\n" + task_name + "\n" + task_description)
    task_data(task_name, task_description)

def update_task(task_number, new_name, new_description):
    lst[task_number - 1]["name"] = new_name
    lst[task_number - 1]["description"] = new_description
    print("\nTASKS:\n")
    for x in range(len(lst)):
        print("Task", x + 1, ": ", lst[x])

def delete_task(number):
    lst.pop(number - 1)
    print("\nTASKS:\n")
    for x in range(len(lst)):
        print("Task", x + 1, ": ", lst[x])

def main():
    while(True):
        command = int(input("Press 1 to Add Task\nPress 2 to Update Task\nPress 3 to Delete Task\nPress 4 to Exit\nCommand: "))
        if(command == 1):
            add_task(input("\nTask Name: "), input("Task Description: "))
        elif(command == 2):
            update_task(int(input("Task Number: ")), input("New Task Name: "), input("New Task Description: "))
        elif(command == 3):
            delete_task(int(input("\nTask Number: ")))
        elif(command == 4):
            return False
        else:
            print("Error")
        print("")


main()