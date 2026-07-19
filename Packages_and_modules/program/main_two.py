"""
main_two.py
Demonstrates package structure and importing logic from nested packages/modules 
using system paths.
"""

from sys import path
path.append('C:\\Users\\sam04\\Documents\\Python_Learning\\Python_Practice\\Packages_and_modules\\packages')

import extra.iota
print(extra.iota.FunI())