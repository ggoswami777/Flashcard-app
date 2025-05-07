import json
d=dict()
n=1
comp=dict()
def to_do_menu():
    try:
        key=int(input("Press the key \n 1 -> To Add a task\n 2-> To View a Task \n 3-> Complete task \n 4-> Delete a task \n 5-> Exit\n"))
        if key==1:
            addtask()
        elif key==2:
            view_task()
        elif key==3:
            complete_task()
        elif key==4:
            delete_task()
        elif key==5:
            exitfunc()
        else:
            print("Invalid Key!")
            to_do_menu()
    except ValueError:
        print("Invalid Key")
    
def addtask():
    global d
    global n
    

    while True:
        d[n]=input("Enter the task you want to complete: ")
        n+=1
        choice=input("Do you want to add more task: Y->YES,N->NO: ").upper()
        if choice=="Y" or choice=="YES":
            continue
        else:
            break
    return to_do_menu()


  
def view_task():
    global d
    global n
    try:
        check=int(input("Enter key\n1->To view number of task\n2->To get a specific task\n3->To view all tasks\n"))
        if check==1:
            print(f"Total tasks: {len(d)}")
        elif check==2:
            specific_task_num=int(input("Enter number of task which you want to see!"))
            specificnumtask=d.get(specific_task_num)
            if specificnumtask:
                print(f"Task{specific_task_num}:{specificnumtask}")
            print(specificnumtask)
        elif check==3:
        
         if not d:
            print("No tasks to display :(")
         else:
            print("All tasks")
            j=json.dumps(d,indent=4)
            print(j)
        else:
            print("Invalid input returning to main menu :/")
    except ValueError:
        print("Invalid number input")
        
    return to_do_menu()
       
def complete_task():
    global d
    global comp
    try:
        opt=int(input("Enter key\n1->Enter completed task\n2->To view completed tasks:"  ))
        if opt==1:
            completed=int(input("Enter number of task you have completed:"))
            if completed in d:
                comp[completed]=d[completed]
                del d[completed]
                print(f"task {completed} completed")
            else:
                print("This task number not found")


        elif opt==2:
            print("Completed tasks")
            comptask=json.dumps(comp,indent=4)
            print(comptask)
        else:
            print("No task completed")
    except ValueError:
        print("Invalid number input")
    return to_do_menu()

def delete_task():
    global d
    while True:
        try:
            delete=int(input("Enter task number which you want to delete"))
            if delete in d:
                del d[delete]
                print("Task delete successfully ")
            else:
                print("Task number not found.")
        except ValueError:
            print("Invalid number input")
        delc=input("Do you want to delete more task: Y->YES,N->NO: ").upper()
        
        if delc=="Y" or delc=="YES":
            continue
        else:
            print("Invalid input")
            break
    print("Returning to main menu")
    return to_do_menu()
    
def exitfunc():
    print("Exiting to main menu")
    exit()

  
to_do_menu()
