[Readme.md](https://github.com/user-attachments/files/26039994/Readme.md)
# Python Practice & Projects Portfolio

### **Description**
This repository serves as a timeline of my progression in Python programming. It documents my journey from learning foundational syntax to building fully functional, packaged desktop applications with Graphical User Interfaces (GUIs). 

Each folder focuses on a specific computer science concept, serving as both a learning sandbox and a reference library for future projects.

---

### **Repository Structure & Programs**

#### 🧮 **1. Quadratic Equation Solvers (`Quadratic_solver` & `Quadratic_solver2.0`)**
*This is the capstone project of the repository, demonstrating the evolution of a single concept from a simple script to a polished application.*
* **`general_formula.py`**: A Command-Line Interface (CLI) tool that evaluates quadratic coefficients and calculates real/complex roots with built-in error handling.
* **`GUI_root_solver.py`**: The first GUI iteration, built using Python's standard `tkinter` library. 
* **`R_solver.py` (v2.0)**: A fully styled, production-ready desktop application with a custom interface, dynamic status labeling, and robust exception handling. *(Packaged as a standalone `.exe` using PyInstaller).*

#### 🧱 **2. Core Fundamentals (`Variables` & `Loops`)**
*Foundational scripts focusing on syntax, boolean logic, control flow, and iterative processing.*
* **`if_statement.py`**: Evaluates multiple integer inputs to algorithmically determine the largest value.
* **`largest_number.py`**: Utilizes a `while` loop for dynamic data entry, continuously comparing values until a termination condition (`-1`) is met.
* **`dragons_choice_game.py`**: A text-based adventure game utilizing `if/elif` statements to evaluate user health and predict battle outcomes.
* **`ticket_bot.py`**: A conditional logic script that acts as an automated cinema ticketing system based on age constraints.
* **`Variables.py`**: Demonstrates simple boolean comparisons and standard input handling.

#### 📦 **3. Architecture & Organization (`OOP` & `Packages_and_modules`)**
*Scripts exploring software architecture, code reusability, and object-oriented design.*
* **`class.py`**: Demonstrates Object-Oriented Programming (OOP) concepts, including class definitions, the `__init__` constructor, instance variables, and accessing internal `__dict__` attributes.
* **`main.py` & `module.py`**: Showcases custom module creation, namespace management, and importing external logic to perform list calculations.

#### ✨ **4. Extras & Tools (`Extras`)**
* **`bubble_sort_visualizer.html`**: An interactive, browser-based visualizer for the Bubble Sort algorithm. Written in HTML/JS, it dynamically animates the sorting process, array swapping, and pass completion.
* **`python_timetable.ics`**: My structured, weekly Python study plan and syllabus.

---

### **How to Run**
Most scripts in this repository can be run directly from the terminal.
1. Ensure Python 3.x is installed on your machine.
2. Clone the repository: `git clone <your-repo-link-here>`
3. Navigate to the desired directory and run the script:
   ```bash
   python script_name.py
