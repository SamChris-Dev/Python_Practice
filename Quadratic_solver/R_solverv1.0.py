"""
R_solverv1.0.py
The first GUI iteration of the Quadratic Equation Solver, built using Python's standard `tkinter` library.
"""

import tkinter as tk
from tkinter import messagebox
import math

# --- 1. The Logic (Event Handler) ---
def calculate_roots():
    """This function runs every time the 'Solve' button is clicked."""
    try:
        # Grab the text from the input fields and convert to floats
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
             # Update the result label directly on the window
             label_result.config(text="If 'a' is 0, this is a linear equation.", fg="red")
             return

        d = (b**2 - 4 * a * c)

        if d < 0:
            label_result.config(text="Oops, the roots are complex.", fg="orange")
        elif d == 0:
            x = -b / (2 * a)
            label_result.config(text=f"Discriminant is zero. Root: x = {x:.2f}", fg="green")
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            label_result.config(text=f"Two roots: x1 = {x1:.2f} | x2 = {x2:.2f}", fg="green")

    except ValueError:
        # Trigger a pop-up error box for bad inputs
        messagebox.showerror("Input Error", "Invalid input! Please enter numbers only.")


# --- 2. The GUI Setup (The Scene) ---
# Create the main window
root = tk.Tk()
root.title("Quadratic Equation Solver")
root.geometry("350x300") # Set window size
root.eval('tk::PlaceWindow . center') # Center it on the screen

# Create a title label
label_title = tk.Label(root, text="ax² + bx + c = 0", font=("Helvetica", 16, "bold"))
label_title.pack(pady=15) # .pack() places the widget in the window with some padding

# Create Input for 'a'
frame_a = tk.Frame(root)
frame_a.pack(pady=5)
tk.Label(frame_a, text="Value a:").pack(side=tk.LEFT)
entry_a = tk.Entry(frame_a, width=10)
entry_a.pack(side=tk.LEFT, padx=5)

# Create Input for 'b'
frame_b = tk.Frame(root)
frame_b.pack(pady=5)
tk.Label(frame_b, text="Value b:").pack(side=tk.LEFT)
entry_b = tk.Entry(frame_b, width=10)
entry_b.pack(side=tk.LEFT, padx=5)

# Create Input for 'c'
frame_c = tk.Frame(root)
frame_c.pack(pady=5)
tk.Label(frame_c, text="Value c:").pack(side=tk.LEFT)
entry_c = tk.Entry(frame_c, width=10)
entry_c.pack(side=tk.LEFT, padx=5)

# Create the Solve Button
# Notice command=calculate_roots connects the button to our math logic
btn_solve = tk.Button(root, text="Solve Equation", command=calculate_roots, bg="#4CAF50", fg="white")
btn_solve.pack(pady=15)

# Create a Label to display the results
label_result = tk.Label(root, text="", font=("Helvetica", 10))
label_result.pack(pady=10)

# --- 3. The Event Loop ---
# This keeps the window open and listens for clicks
root.mainloop()