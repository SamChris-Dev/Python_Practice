"""
main.py
Showcases importing functions from a custom module (module.py) by modifying the system path, 
and using these functions to perform list calculations.
"""

from sys import path
path.insert(0,'C:\\Users\\sam04\\Documents\\Python_Learning\\Python_Practice\\Packages_and_modules\\module')
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

