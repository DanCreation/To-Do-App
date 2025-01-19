import datetime


lst = []
lst_work = []
lst_personal = []
lst_urgent = []
lst_none = []


class Task: 
    def __init__(self, name, description, tag, status, date_time):
        self.name = name
        self.description = description
        self.tag = tag
        self.status = status
        self.date_time = date_time

    def __str__(self):
        return f"\nName: {self.name} \nDescription: {self.description} \nTag: {self.tag} \nStatus: {self.status} \nDate/Time: {self.date_time}"


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
                           "1. Pending \n"
                           "        2. In Progress \n"
                           "        3. Completed \n"
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
                           "1. Work \n"
                           "     2. Personal \n"
                           "     3. Urgent \n"
                           "     4. None \n"
                           "     Command: ")
    return tag


def task_number():
    while(True):
        task_num = input("\nTask Number: ")
        if(task_num.isdigit() and int(task_num) > 0 and int(task_num) <= len(lst)):
            return False
        else:
            print("\nError\n")


def add_task(task_name, task_description, task_tag, task_status):
    task_tag = tag(task_tag)
    task_status = status(task_status)
    lst.append(Task(task_name, task_description, task_tag, task_status, datetime.datetime.now()))
    

def view_tasks():
    print("\nTASKS:")
    #print(datetime.datetime.now())
    #print(datetime.datetime(2025, 4, 18))
    for x in range(len(lst)):
        print("\nTask "+ str(x + 1) + ":", lst[x])


def update_task(task_num, new_name, new_description, new_tag, new_status):
    lst[task_num - 1].name = new_name
    lst[task_num - 1].description = new_description
    lst[task_num - 1].tag = tag(new_tag)
    lst[task_num - 1].status = status(new_status)


def delete_task(number):
    lst.pop(number - 1)


def prioritise_tasks():
    for x in range(len(lst)):
        if(lst[x].tag == "Work"):
            lst_work.append(lst[x])
        elif(lst[x].tag == "Personal"):
            lst_personal.append(lst[x])
        elif(lst[x].tag == "Urgent"):
            lst_urgent.append(lst[x])
        else:
            lst_none.append(lst[x])

    while(True):
        priority = input("\n1. Work Priority\n"
                         "2. Personal Priority\n"
                         "3. Urgent Priority\n"
                         "4. None Priority\n"
                         "Command: ")
        if(priority == "1"):
            for x in range(len(lst_work)):
                lst[x] = lst_work[x]
            for x in range(len(lst_personal)):
                lst[x + len(lst_work)] = lst_personal[x]
            for x in range(len(lst_urgent)):
                lst[x + len(lst_work) + len(lst_personal)] = lst_urgent[x]
            for x in range(len(lst_none)):
                lst[x + len(lst_work) + len(lst_personal) + len(lst_urgent)] = lst_none[x]
            lst_work.clear()
            lst_personal.clear()
            lst_urgent.clear()
            lst_none.clear()
            break

        elif(priority == "2"):
            for x in range(len(lst_personal)):
                lst[x] = lst_personal[x]
            for x in range(len(lst_urgent)):
                lst[x + len(lst_personal)] = lst_urgent[x]
            for x in range(len(lst_none)):
                lst[x + len(lst_personal) + len(lst_urgent)] = lst_none[x]
            for x in range(len(lst_work)):
                lst[x + len(lst_personal) + len(lst_urgent) + len(lst_none)] = lst_work[x]
            lst_work.clear()
            lst_personal.clear()
            lst_urgent.clear()
            lst_none.clear()
            break

        elif(priority == "3"):
            for x in range(len(lst_urgent)):
                lst[x] = lst_urgent[x]
            for x in range(len(lst_none)):
                lst[x + len(lst_urgent)] = lst_none[x]
            for x in range(len(lst_work)):
                lst[x + len(lst_urgent) + len(lst_none)] = lst_work[x]
            for x in range(len(lst_personal)):
                lst[x + len(lst_urgent) + len(lst_none) + len(lst_work)] = lst_personal[x]
            lst_work.clear()
            lst_personal.clear()
            lst_urgent.clear()
            lst_none.clear()
            break

        elif(priority == "4"):
            for x in range(len(lst_none)):
                lst[x] = lst_none[x]
            for x in range(len(lst_work)):
                lst[x + len(lst_none)] = lst_work[x]
            for x in range(len(lst_personal)):
                lst[x + len(lst_none) + len(lst_work)] = lst_personal[x]
            for x in range(len(lst_urgent)):
                lst[x + len(lst_none) + len(lst_work) + len(lst_personal)] = lst_urgent[x]
            lst_work.clear()
            lst_personal.clear()
            lst_urgent.clear()
            lst_none.clear()
            break
            
        else:
            print("\nError\n")

    view_tasks()


def search():
    while(True):
        task_search = input("\n1. Search by Name\n"
                            "2. Search by Description\n"
                            "3. Search by Tag\n"
                            "Command: ")

        if(task_search == "1"):
            while(True):
                search_name = input("\nName: ")
                num = 0
                for x in range(len(lst)):
                    if(search_name == lst[x].name):
                        temp = lst[x]
                        lst[x] = lst[num]
                        lst[num] = temp
                        num += 1
                    else:
                        print("\nThere are no tasks with that name")

                view_tasks()
                return False

        elif(task_search == "2"):
            while(True):
                search_description = input("Description: ")
                num = 0
                for x in range(len(lst)):
                    if(search_description == lst[x].description):
                        temp = lst[x]
                        lst[x] = lst[num]
                        lst[num] = temp
                        num += 1
                    else:
                        print("\nThere are no tasks with that description")

                view_tasks()
                return False

        elif(task_search == "3"):
            while(True):
                search_tag = input("Tag: ")
                num = 0
                for x in range(len(lst)):
                    if(search_tag == lst[x].tag):
                        temp = lst[x]
                        lst[x] = lst[num]
                        lst[num] = temp
                        num += 1
                    else:
                        print("\nThere are no more tasks with that tag")

                view_tasks()
                return False

        else:
            print("\nError\n")


def main():
    while(True):
        command = input("1. Add Task\n"
                        "2. View Tasks\n"
                        "3. Update Task\n"
                        "4. Delete Task\n"
                        "5. Prioritise Tasks\n"
                        "6. Search Tasks\n"
                        "7. Exit\n"
                        "Command: ")

        if(command == "1"):  # Add Task
            add_task(input("\nName: "), 
                     input("Description: "), 
                     input("\nTag: "
                           "1. Work \n"
                           "     2. Personal \n"
                           "     3. Urgent \n"
                           "     4. None \n"
                           "     Command: "),
                     input("\nStatus: "
                           "1. Pending \n"
                           "        2. In Progress \n"
                           "        3. Completed \n"
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
                task_num = task_number()
                update_task(task_num,
                            input("\nNew Name: "), 
                            input("New Description: "),
                            input("\nNew Tag: \n"
                                  "1. Work Priority\n"
                                  "2. Personal Priority\n"
                                  "3. Urgent Priority\n"
                                  "4. None Priority\n"
                                  "Command: "),
                            input("\nNew Status: "
                                  "1. Pending \n"
                                  "        2. In Progress \n"
                                  "        3. Completed \n"
                                  "        Command: "))

        elif(command == "4"):  # Delete Task
            if(len(lst) == 0):
                print("\nThere are no tasks to delete")
            else:
                delete_task(int(input("\nTask Number: ")))

        elif(command == "5"):  # Prioritise
            if(len(lst) == 0):
                print("\nThere are no tasks to prioritise")
            else:
                prioritise_tasks()
        
        elif(command == "6"):  # Search
            search()
        elif(command == "7"):  # Exit
            return False

        else:
            print("\nError")
        print("")


main()