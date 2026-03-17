n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

nl = n1

if n2 > n1:
    nl = n2
if n3 > n1:
    nl = n3

print("The largest number is ", nl)