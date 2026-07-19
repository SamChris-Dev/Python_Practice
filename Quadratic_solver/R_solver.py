"""
R_solver.py
A Command-Line Interface (CLI) tool that evaluates quadratic coefficients 
and calculates real/complex roots with built-in error handling.
"""

import math

def rootsolver():
    """
    Main function to compute roots of a quadratic equation.
    Interactively prompts the user for coefficients a, b, and c.
    Handles exceptions like non-numeric inputs.
    """
    print("Welcome to my root solver!")

    while True:
        try:
            a = float(input("Enter the value of the a coefficient: "))
            b = float(input("Enter the value of the b coefficient: "))
            c = float(input("Enter the value of the c coefficient: "))

            if a == 0:
                print("Since 'a' is 0 then this is not quadratic equation")
                value = -(c) / (b)
                print("Thou, Here is the value of 'x': ", value)
            else:
            
                d = (b**2 - 4 * a * c)

                if d < 0:
                    print("Oops the root is complex")
                elif d == 0:
                    x = -b / (2 * a)
                    print("The value of x is: ", x)

                else:
                    x1 = (-b + math.sqrt(d))/(2*a)
                    x2 = (-b - math.sqrt(d))/(2*a)

                    print("The value of x1 is: ", x1, "and the value of x2 is: ", x2)
            break
             

        except ValueError:
            print("Invalid input, Please enter numbers only")


rootsolver()




