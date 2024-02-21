n1 = int(input("Input number 1: "))
n2 = int(input("Input number 2: "))
n3 = int(input("Input number 3: "))

Largest_Number = n1

if n2 > Largest_Number:
    Largest_Number = n2
if n3 > Largest_Number:
    Largest_Number = n3

print("The Largest Number is: ", Largest_Number)