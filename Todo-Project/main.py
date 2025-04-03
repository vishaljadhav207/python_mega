
while True:
    user_action = input("type add,show,edit,complete todo or exit:  ")
    user_action=user_action.strip()

    if "add" in user_action:
            todo=user_action[4:]

            # file=open('todos.txt','r')
            # todos=file.readlines()
            # file.close()

            with open("todos.txt", "r") as file: #same as above dont need to add file.close()
                todos = file.readlines()

            todos.append(todo)
            with open("todos.txt", "w") as file:
                todos=file.writelines(todos)

    elif "show" in user_action:
            with open("todos.txt", "r") as file:
                todos = file.readlines()


            # new_todos=[item.strip("\n") for item in todos]

            for index,item in enumerate(todos): # enumerate() function adds a counter to each item in a list or other iterable.
                item=item.strip("\n")
                item=item.title()
                print(f"{index+1}.{item}")
    elif "edit" in user_action:

            number=int(user_action[5:])
            print(number)
            number = number - 1


            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo=input("enter new todo: ")
            todos[number]=new_todo+"\n"

            with open("todos.txt", "w") as file:
                todos=file.writelines(todos)


    elif "complete" in user_action:
            number=int(user_action[9:])

            with open("todos.txt", "r") as file:
                todos=file.readlines()

            index=number-1
            todo_to_remove=todos[index]
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message=f"Todo {todo_to_remove} was remove from the list"
            print(message)
    elif "exit" in user_action:
            break
    else:
        print("command is not valid")

print("Bye")
