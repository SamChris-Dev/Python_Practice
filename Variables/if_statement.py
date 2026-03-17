# Simple program that takes three numbers from the user and outputs the largest number
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

#Assume the (nl)largest number is n1(the first number)
nl = n1

if n2 > n1: 
    nl = n2

if n3 > n1:
    nl = n3

print("The largest number is ", nl)