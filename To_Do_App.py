
lst = []


class Task: 
    def __init__(self, name, description, tag, status):
        self.name = name
        self.description = description
        self.tag = tag
        self.status = status

    def __str__(self):
        return f"\nName: {self.name} \nDescription: {self.description} \nTag: {self.tag} \nStatus: {self.status}"


def status(status):
    while(True):
        if(status == "1"): 
            status = "Pending"
            break
        elif(status == "2"):
            status = "In Progress"
            break
        elif(status == "3"):
            status = "Completed"
            break
        else:
            print("\nError\n")
            status = input("Status: "
                           "Press 1 for Pending \n"
                           "        Press 2 for In Progress \n"
                           "        Press 3 for Completed \n"
                           "        Command: ")
    return status


def tag(tag):
    while(True):
        if(tag == "1"): 
            tag = "Work"
            break
        elif(tag == "2"):
            tag = "Personal"
            break
        elif(tag == "3"):
            tag = "Urgent"
            break
        elif(tag == "4"):
            tag = "None"
            break
        else:
            print("\nError\n")
            tag = input("Tag: "
                           "Press 1 for Work \n"
                           "     Press 2 for Personal \n"
                           "     Press 3 for Urgent \n"
                           "     Press 4 for None \n"
                           "     Command: ")
    return tag


def add_task(task_name, task_description, task_tag, task_status):
    task_tag = tag(task_tag)
    task_status = status(task_status)
    lst.append(Task(task_name, task_description, task_tag, task_status))
    

def view_tasks():
    print("\nTASKS:")
    for x in range(len(lst)):
        print("\nTask "+ str(x + 1) + ":", lst[x])


def update_task(task_number, new_name, new_description, new_status):
    new_status = status(new_status)
    lst[task_number - 1].name = new_name
    lst[task_number - 1].description = new_description
    lst[task_number - 1].status = new_status


def delete_task(number):
    lst.pop(number - 1)


def main():
    while(True):
        command = input("Press 1 to Add Task\n"
                        "Press 2 to View Tasks\n"
                        "Press 3 to Update Task\n"
                        "Press 4 to Delete Task\n"
                        "Press 5 to Exit\n"
                        "Command: ")

        if(command == "1"):  # Add Task
            add_task(input("\nName: "), 
                     input("Description: "), 
                     input("Tag: "
                           "Press 1 for Work \n"
                           "     Press 2 for Personal \n"
                           "     Press 3 for Urgent \n"
                           "     Press 4 for None \n"
                           "     Command: "),
                     input("Status: "
                           "Press 1 for Pending \n"
                           "        Press 2 for In Progress \n"
                           "        Press 3 for Completed \n"
                           "        Command: "))

        elif(command == "2"):  # View Tasks
            if(len(lst) == 0):
                print("\nThere are no tasks to view")
            else:
                view_tasks()
        elif(command == "3"):  # Update Task
            if(len(lst) == 0):
                print("\nThere are no tasks to update")
            else:
                update_task(int(input("\nTask Number: ")),
                                input("\nNew Name: "), 
                                input("New Description: "), 
                                input("New Status: "
                                      "Press 1 for Pending \n"
                                      "        Press 2 for In Progress \n"
                                      "        Press 3 for Completed \n"
                                      "        Command: "))
        elif(command == "4"):  # Delete Task
            if(len(lst) == 0):
                print("\nThere are no tasks to delete")
            else:
                delete_task(int(input("\nTask Number: ")))
        elif(command == "5"):  # Exit
            return False
        else:
            print("\nError")
        print("")


main()