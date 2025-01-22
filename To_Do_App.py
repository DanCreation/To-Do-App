import datetime


lst = []


class Task: 
    def __init__(self, name, description, tag, status, date_time):
        self.name = name
        self.description = description
        self.tag = tag
        self.status = status
        self.date_time = date_time

    def __str__(self):
        return f"\nName: {self.name} \nDescription: {self.description} \nTag: {self.tag} \nStatus: {self.status} \nDate/Time: {self.date_time}"


def get_task_number():
    try:
        task_number = int(input("\nTask Number: "))
        if(task_number < len(lst) or task_number > len(lst)):
            raise ValueError("\nInvalid Input.")
        return task_number
    except ValueError as e:
        print(e)
        return get_task_number()


def get_name():
    return input("\nName: ")


def get_description():
    return input("\nDescription: ")


def get_deadline():  # Not Finished
    return input("\nDeadline (dd-mm-yyyy): ")


def get_tag():
    try:
        tag = int(input("\nTag:\n1. Work\n2.Personal\n3. Urgent\n4. None\nCommand: "))
        if(tag <= 0 or tag > 4):
            raise ValueError("\nInvalid Input.")
        elif(tag == 1): 
            tag = "Work"
        elif(tag == 2):
            tag = "Personal"
        elif(tag == 3):
            tag = "Urgent"
        elif(tag == 4):
            tag = "None"
        return tag
    except ValueError as e:
        print(e)
        return get_tag()


def get_status():
    try:
        status = int(input("\nStatus:\n1. Pending\n2. In Progress\n3. Completed\nCommand: "))
        if(status <= 0 or status > 3):
            raise ValueError("\nInvalid input.")
        if(status == 1): 
            status = "Pending"
        elif(status == 2):
            status = "In Progress"
        elif(status == 3):
            status = "Completed"
        return status
    except ValueError as e:
        print(e)
        return get_status()


def add_task():
    lst.append(Task(get_name(), get_description(), get_tag(), get_status(),
                   datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))

    
def view_tasks():
    print("\nTASKS:")
    #print(datetime.datetime.now())
    #print(datetime.datetime(2025, 4, 18))
    for x in range(len(lst)):
        print("\nTask "+ str(x + 1) + ":", lst[x])


def update_task():
    task_num = get_task_number()
    lst[task_num - 1] = Task(get_name(), get_description(), get_tag(),
                            get_status(), datetime.datetime.now())


def delete_task(number):
    lst.pop(number - 1)


def prioritise(tag):
    num = 0
    for x in range(len(lst)):
        if(lst[x].tag == tag):
            temp = lst[num]
            lst[num] = lst[x]
            lst[x] = temp
            num += 1
    view_tasks()


def search():  # Not finished
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
            try:
                search_tag = int(input("\n1. Work\n"
                         "2. Personal\n"
                         "3. Urgent\n"
                         "4. None\n"
                         "Command: "))
                if(search_tag <= 0 or search_tag > 4):
                    raise ValueError("\nInvalid Input")
                elif(search_tag == 1):
                    prioritise("Work")
                elif(search_tag == 2):
                    prioritise("Personal")
                elif(search_tag == 3):
                    prioritise("Urgent")
                elif(search_tag == 4):
                    prioritise("None")
                return search_tag
            except ValueError as e:
                print(e)
            return False
        else:
            print("\nError\n")


def main():
    while(True):
        try:
            command = int(input("\n1. Add Task\n"
                            "2. View Tasks\n"
                            "3. Update Task\n"
                            "4. Delete Task\n"
                            "5. Search Tasks\n"
                            "6. Exit\n"
                            "Command: "))
            if(command <= 0 or command > 7):
                raise ValueError("\nInvalid Input.")
            match command:
                case 1:  # ADD TASK
                    add_task()
                case 2:  # VIEW TASKS
                    if(len(lst) == 0):
                        print("\nThere are no tasks to view")
                    else:
                        view_tasks()
                case 3:  # UPDATE TASK
                    if(len(lst) == 0):
                        print("\nThere are no tasks to update")
                    else:
                        update_task()
                case 4:  # DELETE TASK
                    if(len(lst) == 0):
                        print("\nThere are no tasks to delete")
                    else:
                        delete_task(int(input("\nTask Number: ")))
                case 5:  # SEARCH
                    if(len(lst) == 0):
                        print("\nThere are no tasks to search")
                    else:
                        search()
                case 6:  # EXIT
                    return False
        except ValueError as e:
            print(e)

if(__name__ == "__main__"):
    main()