"""
simple_stack.py
Implements a simple interactive stack data structure using a Python list.
Allows users to push, pop, and view the elements in the stack.
"""

simple_stack = []
loop_on = True

def push(user_val):
    """Pushes a value to the top of the stack."""
    simple_stack.append(user_val)

def pop():
    """Removes and prints the top value from the stack."""
    del simple_stack[-1]
    print("Stack = ", simple_stack)


def control():
    """Prompts the user to enter a value to be pushed onto the stack."""
    global user_val
    user_val = int(input("Enter a number to be pushed: "))

def view_stack():
    """Displays the current state of the stack."""
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

    
    
