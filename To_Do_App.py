
lst = []

class Task: 
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"\nName: {self.name} \nDescription: {self.description}"
    #def task_data(self):
        #lst.append("Name: " + self.name + " Description: " + self.description)

def add_task(task_name, task_description):
    lst.append(task(task_name, task_description))

def view_tasks():
    print("\nTASKS:")
    for x in range(len(lst)):
        print("\nTask "+ str(x + 1) + ":", lst[x])

def update_task(task_number, new_name, new_description):
    lst[task_number - 1].name = new_name
    lst[task_number - 1].description = new_description

def delete_task(number):
    lst.pop(number - 1)

def main():
    while(True):
        command = input("Press 1 to Add Task\nPress 2 to View Tasks\nPress 3 to Update Task\nPress 4 to Delete Task\nPress 5 to Exit\nCommand: ")
        if(command == "1"):
            add_task(input("\nTask Name: "), input("Task Description: "))
        elif(command == "2"):
            if(len(lst) == 0):
                print("\nThere are no tasks to view")
            else:
                view_tasks()
        elif(command == "3"):
            if(len(lst) == 0):
                print("\nThere are no tasks to update")
            else:
                update_task(int(input("Task Number: ")), input("New Task Name: "), input("New Task Description: "))
        elif(command == "4"):
            if(len(lst) == 0):
                print("\nThere are no tasks to delete")
            else:
                delete_task(int(input("\nTask Number: ")))
        elif(command == "5"):
            return False
        else:
            print("\nError")
        print("")

main()