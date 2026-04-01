#To-Do List Applicaation

tasks=[]

def show_menu():

    print("\n---TO-DO LIST MENU---")
    print("1.Add Task")
    print("2.View Tasks");
    print("3.Remove task");
    print("4.Exit");

while True:

    show_menu

    choice=input("enter your choice:")

    if choice == "1":

        task=input("enter task:")
        tasks.append(task)
        print("task added successfully!")

    elif choice  == "2":
            
        if len(tasks)==0:
                print("No tasks available.")

        else:
            print("\nYour Tasks:")
            for i,task in enumerate(tasks):
                print(i+1,".",task)

    elif  choice == "3":
    
       task_no = int(input("enter task number to remove:"))

       if 0 <task_no <= len(tasks):
         tasks.pop(task_no - 1)
         print("Task removed successfully!")
   
       else:
        print("invalid task number!")
  
    elif  choice == "4":

      print("Exiting program...")
      break
else:
 print("invalid choice!")
                                            
    