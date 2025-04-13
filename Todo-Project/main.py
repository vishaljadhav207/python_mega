# import os
# print("Current Working Directory:", os.getcwd())

from functions import get_todos,write_todos
import time #global module
now =time.strftime("%b %d,%Y %H:%M:%S" )
print("It is",now)

while True:
    user_action = input("type add,show,edit,complete todo or exit:  ")
    user_action=user_action.strip()

    if user_action.startswith("add"):
            todo=user_action[4:]


            todos=get_todos()

            todos.append(todo+"\n")
            write_todos(todos)

    elif user_action.startswith("show"):
            todos=get_todos()


            # new_todos=[item.strip("\n") for item in todos]

            for index,item in enumerate(todos): # enumerate() function adds a counter to each item in a list or other iterable.
                item=item.strip("\n")
                item=item.title()
                print(f"{index+1}.{item}")
    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            print(number)
            number = number - 1


            todos=get_todos()

            new_todo=input("enter new todo: ")
            todos[number]=new_todo+"\n"

            # with open("todos.txt", "w") as file:
            #     todos=file.writelines(todos)

            write_todos(todos)
        except ValueError:
           print("your command is invalid")
           continue

    elif user_action.startswith("complete"):
        try:
            number=int(user_action[9:])


            todos=get_todos("todos.txt") #same as above
            index=number-1
            todo_to_remove=todos[index]
            todos.pop(index)

            write_todos(todos)

            message=f"Todo {todo_to_remove} was remove from the list"
            print(message)
        except IndexError:
            print("there is no item with that no !")
            continue
    elif user_action.startswith("exit"):
            break
    else:
        print("command is not valid")

print("Bye")
