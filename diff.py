from unittest import removeResult

x = int(input("Enter the first value: "))
y = int(input("Enter the second value: "))
operat = input("Please select the fuction you want to use (+,-,*,/) : ")

if operat == "+":
    print (x+y)
elif operat == "-":
    print (x-y)
elif operat == "*":
    print (x*y)
elif operat == "/":
    print (x/y)
else:
    print("Please select a valid operation.")



