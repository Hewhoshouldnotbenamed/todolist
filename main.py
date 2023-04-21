while True:
    user_command=input(" Enter '+' for adding task and 'open' for reading todolist content: ")
    if user_command=="+":
        with open("todolist.txt","a") as td:
            task_name=input("Enter the task to add:")
            task_completion_date=input("Enter the task completion date:")
            td.writelines((task_name," ",task_completion_date,"\n"))

    elif user_command=="open":
        with open("todolist.txt","r") as td:
           print( td.read())


    else:
        break