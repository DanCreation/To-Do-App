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
                   datetime.datetime.now()))

    
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
            temp = []
            for x in range(len(lst_work)):
                temp.append(lst[x])
                lst[x] = lst_work[x]
            lst.append(temp)
            temp.clear()
            lst_work.clear()
            # for x in range(len(lst_work)):
            #     lst[x] = lst_work[x]
            # for x in range(len(lst_personal)):
            #     lst[x + len(lst_work)] = lst_personal[x]
            # for x in range(len(lst_urgent)):
            #     lst[x + len(lst_work) + len(lst_personal)] = lst_urgent[x]
            # for x in range(len(lst_none)):
            #     lst[x + len(lst_work) + len(lst_personal) + len(lst_urgent)] = lst_none[x]
            # lst_work.clear()
            # lst_personal.clear()
            # lst_urgent.clear()
            # lst_none.clear()
            break

        elif(priority == "2"):
            temp = []
            for x in range(len(lst_personal)):
                temp.append(lst[x])
                lst[x] = lst_personal[x]
            lst.append(temp)
            temp.clear()
            lst_personal.clear()
            # for x in range(len(lst_personal)):
            #     lst[x] = lst_personal[x]
            # for x in range(len(lst_urgent)):
            #     lst[x + len(lst_personal)] = lst_urgent[x]
            # for x in range(len(lst_none)):
            #     lst[x + len(lst_personal) + len(lst_urgent)] = lst_none[x]
            # for x in range(len(lst_work)):
            #     lst[x + len(lst_personal) + len(lst_urgent) + len(lst_none)] = lst_work[x]
            # lst_work.clear()
            # lst_personal.clear()
            # lst_urgent.clear()
            # lst_none.clear()
            break

        elif(priority == "3"):
            temp = []
            for x in range(len(lst_urgent)):
                temp.append(lst[x])
                lst[x] = lst_urgent[x]
            lst.append(temp)
            temp.clear()
            lst_urgent.clear()
            # for x in range(len(lst_urgent)):
            #     lst[x] = lst_urgent[x]
            # for x in range(len(lst_none)):
            #     lst[x + len(lst_urgent)] = lst_none[x]
            # for x in range(len(lst_work)):
            #     lst[x + len(lst_urgent) + len(lst_none)] = lst_work[x]
            # for x in range(len(lst_personal)):
            #     lst[x + len(lst_urgent) + len(lst_none) + len(lst_work)] = lst_personal[x]
            # lst_work.clear()
            # lst_personal.clear()
            # lst_urgent.clear()
            # lst_none.clear()
            break

        elif(priority == "4"):
            temp = []
            for x in range(len(lst_none)):
                temp.append(lst[x])
                lst[x] = lst_none[x]
            lst.append(temp)
            temp.clear()
            lst_none.clear()
            # for x in range(len(lst_none)):
            #     lst[x] = lst_none[x]
            # for x in range(len(lst_work)):
            #     lst[x + len(lst_none)] = lst_work[x]
            # for x in range(len(lst_personal)):
            #     lst[x + len(lst_none) + len(lst_work)] = lst_personal[x]
            # for x in range(len(lst_urgent)):
            #     lst[x + len(lst_none) + len(lst_work) + len(lst_personal)] = lst_urgent[x]
            # lst_work.clear()
            # lst_personal.clear()
            # lst_urgent.clear()
            # lst_none.clear()
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
            try:
                search_tag = int(input("\n1. Work\n"
                         "2. Personal\n"
                         "3. Urgent\n"
                         "4. None\n"
                         "Command: "))
                if(search_tag <= 0 or search_tag > 4):
                    raise ValueError("\nInvalid Input")
                elif(search_tag == 1):
                    num = 0
                    for x in range(len(lst)):
                        if(lst[x].tag == "Work"):
                            temp = lst[num]
                            lst[num] = lst[x]
                            lst[x] = temp
                            num += 1
                        else:
                            print("There are no tasks with that tag.")
                elif(search_tag == 2):
                    num = 0
                    for x in range(len(lst)):
                        if(lst[x].tag == "Personal"):
                            temp = lst[num]
                            lst[num] = lst[x]
                            lst[x] = temp
                            num += 1
                        else:
                            print("There are no tasks with that tag.")
                elif(search_tag == 3):
                    num = 0
                    for x in range(len(lst)):
                        if(lst[x].tag == "Urgent"):
                            temp = lst[num]
                            lst[num] = lst[x]
                            lst[x] = temp
                            num += 1
                        else:
                            print("There are no tasks with that tag.")
                elif(search_tag == 4):
                    num = 0
                    for x in range(len(lst)):
                        if(lst[x].tag == "None"):
                            temp = lst[num]
                            lst[num] = lst[x]
                            lst[x] = temp
                            num += 1
                        else:
                            print("There are no tasks with that tag.")
                return search_tag
            except ValueError as e:
                print(e)

            #prioritise_tasks()
            # while(True):
            #     search_tag = input("Tag: ")
            #     num = 0
            #     for x in range(len(lst)):
            #         if(search_tag == lst[x].tag):
            #             temp = lst[x]
            #             lst[x] = lst[num]
            #             lst[num] = temp
            #             num += 1
            #         else:
            #             print("\nThere are no more tasks with that tag")

            #     view_tasks()
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
                            "5. Prioritise Tasks\n"
                            "6. Search Tasks\n"
                            "7. Exit\n"
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
                case 5:  # PRIORITISE TASK
                    if(len(lst) == 0):
                        print("\nThere are no tasks to prioritise")
                    else:
                        prioritise_tasks()
                case 6:  # SEARCH
                    if(len(lst) == 0):
                        print("\nThere are no tasks to search")
                    else:
                        search()
                case 7:  # EXIT
                    return False
        except ValueError as e:
            print(e)


main()