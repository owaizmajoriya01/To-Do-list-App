tasks=[]

if __name__=="__main__":
    print("Welcome to the to-do list App!")
    
    while True:
        print("\n\n")
        print("please select one of the following options")
        print("------------------------------------------- ")
        print("1. Add a new task")
        print("2. delete a task")
        print("3. List Tasks")
        print("4. Quit")

        choice = input("\nEnter your choice:  ")

        if (choice =="1"):
            print("\nyou selected to add a task!")
            task = input("write a task: ")
            tasks.append(task)
            print("\nTask added successfully")

        elif (choice == "2"):
            count=int(input("enter the # of the task to delete: "))
            if count > len(tasks) or count < 0 :
                print("invalid # number")
            else:
                print("your want to remove the task "+tasks[count-1])
                tasks.pop(count-1)
                print("tasks removed successfully!")


        elif (choice == "3"):
            print("you selected to lists all the task: ")
            for index,task in enumerate(tasks):
                print(f"Task #{index}. {task}")
                
        elif (choice == "4"):
            break
        else:
            print("invalid input, please try again!")
