simple_stack = []
loop_on = True

def push(user_val):
    simple_stack.append(user_val)

def pop():
    del simple_stack[-1]
    print("Stack = ", simple_stack)


def control():
    global user_val
    user_val = int(input("Enter a number to be pushed: "))

def view_stack():
    print("View current stack", end="\n")
    print("Stack = ", simple_stack)



while loop_on:
    print()
    print("Choose 'push' , 'pop' , 'view' or 'exit' ")
    string = input("Enter choice here: ")

    if string == "push":
        control()
        push(user_val)
    elif string == "view":
        view_stack()
    elif string == "exit":
        loop_on = False
    elif string == "pop":
        pop()

    
    
