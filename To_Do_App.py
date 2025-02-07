import datetime
import json
import os.path

import tkinter  # NOT FINISHED
from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox


lst = []
deadline_lst = []
string_lst = []
array = []
dicts = {
            "name" : "",
            "description" : "",
            "tag" : "",
            "status" : "",
            "deadline" : "",
            "created_date_time" : "",
            "last_modified_date_time" : ""
            } 


class Task: 
    def __init__(self, name, description, tag, status, deadline, created_date_time, last_modified_date_time):
        self.name = name
        self.description = description
        self.tag = tag
        self.status = status
        self.deadline = deadline
        self.created_date_time = created_date_time
        self.last_modified_date_time = last_modified_date_time

    def __str__(self):
        return (f"\nName: {self.name} \nDescription: {self.description}" 
        f"\nTag: {self.tag} \nStatus: {self.status} \nDeadline: {self.deadline}" 
        f"\nCreated Date/Time: {self.created_date_time}"
        f"\nLast Modified Date/Time: {self.last_modified_date_time}")


def get_task_number():
    try:
        task_number = int(input("\nTask Number: "))
        if(task_number <= 0 or task_number > len(lst)):
            print("\nInvalid Task Number.")
            return get_task_number()
        else:
            return task_number
    except ValueError:
        print("\nInvalid Input.")
        return get_task_number()


def get_name():
    name = input("\nName: ")
    if(bool(name) == False):
        print("\nTask must have a name.")
        return get_name()
    else:
        return name


def get_description():
    return input("\nDescription: ")


def get_deadline():
    deadline_format = "%d-%m-%Y"
    deadline = input("\nDeadline (dd-mm-yyyy): ")
    correct_format = True
    try:
        correct_format == bool(datetime.datetime.strptime(deadline, deadline_format))
        if(check_deadline(deadline) == True):
            return deadline
        else:
            print("\nThe deadline cannot be set in the past.")
            return get_deadline()
    except:
        print("\nIncorrect format. Please enter the date as dd-mm-yyyy.")
        return get_deadline()
    

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
    lst.append(Task(get_name(), get_description(), get_tag(), get_status(), get_deadline(), 
                    datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 
                    datetime.datetime.now().strftime("%d-%m-%Y %H:%M")))

    
def view_tasks():
    print("\nTASKS:")
    for x in range(len(lst)):
        print("\nTask "+ str(x + 1) + ":", lst[x])


def update_task():
    task_num = get_task_number()
    created = lst[task_num - 1].created_date_time
    lst[task_num - 1] = Task(get_name(), get_description(), get_tag(),
                            get_status(), get_deadline(), created,datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))


def delete_task(number):
    lst.pop(number - 1)
    

def check_deadline(deadline):
    due_number = str(deadline)
    due_day = due_number[0] + due_number[1]
    due_month = due_number[3] + due_number[4]
    due_year = due_number[6] + due_number[7] + due_number[8] + due_number[9]

    present_number = str(datetime.datetime.now().strftime("%d-%m-%Y"))
    present_day = present_number[0] + present_number[1]
    present_month = present_number[3] + present_number[4]
    present_year = present_number[6] + present_number[7] + present_number[8] + present_number[9]

    if(due_year < present_year):
        return False
    elif(due_year == present_year and due_month < present_month):
        return False
    elif(due_year == present_year and due_month == present_month and due_day < present_day):
        return False
    else:
        return True


def get_sorted_dates(date_lst):
    split_lst = date_lst.split("-")
    return split_lst[2], split_lst[1], split_lst[0]


def get_priority(priority, user_input):
    num = 0
    if(priority == "name"):
        for x in range(len(lst)):
            if(lst[x].name.find(user_input) != -1):
                temp = lst[num]
                lst[num] = lst[x]
                lst[x] = temp
                num += 1
    elif(priority == "description"):
        for x in range(len(lst)):
            if(lst[x].description.find(user_input) != -1):
                temp = lst[num]
                lst[num] = lst[x]
                lst[x] = temp
                num += 1
    elif(priority == "tag"):
        for x in range(len(lst)):
            if(lst[x].tag == user_input):
                temp = lst[num]
                lst[num] = lst[x]
                lst[x] = temp
                num += 1
    elif(priority == "status"):
        for x in range(len(lst)):
            if(lst[x].status == user_input):
                temp = lst[num]
                lst[num] = lst[x]
                lst[x] = temp
                num += 1
    elif(priority == "deadline"):
        for x in range(len(lst)):
            deadline_lst.append(lst[x].deadline)

        deadline_lst.sort(key=get_sorted_dates)
        reversed_list = list(reversed(deadline_lst))
        if(user_input == "closest"):
            for x in range(len(deadline_lst)):
                for y in range(len(lst)):
                    if(lst[y].deadline == deadline_lst[x]):
                        temp = lst[num]
                        lst[num] = lst[y]
                        lst[y] = temp
                num += 1
                    
        elif(user_input == "furthest"):
            for x in range(len(reversed_list)):
                for y in range(len(lst)):
                    if(lst[y].deadline == reversed_list[x]):
                        temp = lst[num]
                        lst[num] = lst[y]
                        lst[y] = temp
                num += 1

        else:
            for x in range(len(lst)):
                if(lst[x].deadline.find(user_input) != -1):
                    temp = lst[num]
                    lst[num] = lst[x]
                    lst[x] = temp
                    num += 1
                    
    deadline_lst.clear()
    view_tasks()


def search():
    try:
        task_search = int(input("\n1. Search by Name\n"
                            "2. Search by Description\n"
                            "3. Search by Tag\n"
                            "4. Search by Status\n"
                            "5. Search by Deadline\n"
                            "Command: "))
        if(task_search <= 0 or task_search > 5):
            raise ValueError("\nInvalid Input.")
        elif(task_search == 1):
            get_priority("name", input("Name: "))

        elif(task_search == 2):
            get_priority("description", input("Description: "))

        elif(task_search == 3):
            try:
                search_tag = int(input("\n1. Work\n"
                         "2. Personal\n"
                         "3. Urgent\n"
                         "4. None\n"
                         "Command: "))
                if(search_tag <= 0 or search_tag > 4):
                    raise ValueError("\nInvalid Input")
                elif(search_tag == 1):
                    get_priority("tag", "Work")
                elif(search_tag == 2):
                    get_priority("tag", "Personal")
                elif(search_tag == 3):
                    get_priority("tag", "Urgent")
                elif(search_tag == 4):
                    get_priority("tag", "None")
                return search_tag
            except ValueError as e:
                print(e)
                search()

        elif(task_search == 4):
            try:
                search_status = int(input("\n1. Pending\n"
                         "2. In Progress\n"
                         "3. Completed\n"
                         "Command: "))
                if(search_status <= 0 or search_status > 3):
                    raise ValueError("\nInvalid Input")
                elif(search_status == 1):
                    get_priority("status", "Pending")
                elif(search_status == 2):
                    get_priority("status", "In Progress")
                elif(search_status == 3):
                    get_priority("status", "Completed")
                return search_status
            except ValueError as e:
                print(e)
                search()

        elif(task_search == 5):  # NOT FINISHED
            try:
                order = int(input("\n1. Closest Deadlines\n"
                                  "2. Furthest Deadlines\n"
                                  "3. Manual Search\n"
                                  "Command: "))
                if(order <= 0 or order > 3):
                    raise ValueError("Invalid Input.")
                elif(order == 1):
                    get_priority("deadline", "closest")
                elif(order == 2):
                    get_priority("deadline", "furthest")
                elif(order == 3):         
                    get_priority("deadline", input("Deadline: "))
            except ValueError as e:
                print(e)
            
    except ValueError as e:
        print(e)
        search()
          
        
def main():  # NOT FINISHED
    #####################################################################
    top = tkinter.Tk()  # TESTING GUI
    top.geometry("200x300")
    def show():
        num = askinteger("Input", "Input an Interger")
        print(num)
    b = Button(top, text = "Click", command = show)
    b.place(x=100,y=150)
    top.mainloop()
    #####################################################################
    if(os.path.isfile("./Task_Data.json")):  # CHECKS IF FILE EXISTS
        with open("Task_Data.json", "r") as file:
            load = json.load(file)

        for x in range(len(load)):
            lst.append(Task(load[x].get("name"), load[x].get("description"), load[x].get("tag"), load[0+x].get("status"), load[x].get("deadline"), 
                            load[x].get("created_date_time"), 
                            load[x].get("last_modified_date_time")))

    while(True):
        try:
            command = int(input("\n1. Add Task\n"
                            "2. View Tasks\n"
                            "3. Update Task\n"
                            "4. Delete Task\n"
                            "5. Search Tasks\n"
                            "6. Save & Exit\n"
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
                case 6:  # SAVE & EXIT
                    dict_data = []
                    with open("Task_Data.json", "w") as outfile:
                        for x in range(len(lst)):
                            dicts = {
                                    "name" : lst[x].name,
                                    "description" : lst[x].description,
                                    "tag" : lst[x].tag,
                                    "status" : lst[x].status,
                                    "deadline" : lst[x].deadline,
                                    "created_date_time" : lst[x].created_date_time,
                                    "last_modified_date_time" : lst[x].last_modified_date_time
                                    }
                            dict_data.append(dicts)
                        json.dump(dict_data, outfile, indent=4,)
                    return False
        except ValueError as e:
            print(e)

if(__name__ == "__main__"):
    main()