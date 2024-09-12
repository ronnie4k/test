name = input("Enter your Name: ")
institution = input("Enter your Institution Name: ")
standard = input("Enter your Class: ")
section = input("Enter your Section: ")
roll_no = input("Enter your Roll no: ")
m = int(input("Enter the Marks Obatained: "))
if m>90:
    print("The Grade Obtained is A+")
if m>80 and m<90:
    print("The Grade Obtained is A")
if m > 70 and m < 80:
    print("The Grade Obtained is B+")
if m > 60 and m < 70:
    print("The Grade Obtained is B")
if m > 50 and m < 60:
    print("The Grade Obtained is C+")
if m > 40 and m < 50:
    print("The Grade Obtained is C")
if m < 40:
    print("Failed")
