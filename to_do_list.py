task = []
completed = []
def add(i):
    task.append(i)

def delete(i):
    print(i + " is deleted from the list")
    task.remove(i)

def view():
    n = 1
    print("Tasks in list")
    if task==[]:
        print("List is empty!")
    for t in task:
        print(str(n)+" : "+t)
        n = n + 1
    n = 1 
    if(completed != []):
        print("Tasks Completed")
        for t in completed:
            print(str(n)+" : "+t)
            n = n + 1
    elif task!=[]:
        print("No task completed yet")

def done(i):
    print( i + " is done")
    task.remove(i)
    completed.append(i)

#main
view()
while True:
    print("Edit to do list")
    print("1. Add Tasks")
    print("2. Delete Tasks")
    print("3. Completed Tasks")
    ch=int(input("Enter your choice: "))
    if ch==1:
        tk=input("Enter task to be added: ")
        add(tk)
        view()
    elif ch==2:
        tk=input("Enter task to be deleted: ")
        delete(tk)
        view()
    elif ch==3:
        tk=input("Enter completed task: ")
        done(tk)
        view()
    else:
        print("Invalid Choice" )
    c=input("Do you want to continue? (y/n) ")
    if c=='y' or c=='Y':
        continue
    else:
        break
