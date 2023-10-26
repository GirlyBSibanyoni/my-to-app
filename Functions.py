#FILEPATH = "todos.txt"
FILEPATH = "todos.txt"



def read_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__Organising the code modules(#modules#import)__":
    print("Hello from funtions")
    print(read_todos)

