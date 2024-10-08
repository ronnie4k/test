while(1):
    print("WELCOME TO THE IRS BANKING SYSTEM \n""Please select the Desired Option"  "\n1 OPEN ACCOUNT""\n2 ACCOUNT DETAILS" "\n3 CURRENT BALANCE" "\n4 EXIT")
    ir = input("Enter your choice: ")
    age = "i"
    if ir == "1":
        try:
            age = int(input("Enter your AGE : "))
            if age < 18:
                print("NOT ELIGIBLE TO MAKE A BANK ACCOUNT")
                break
            elif age > 100:
                print("NOT ELIGIBLE TO MAKE A BANK ACCOUNT")
                break
            else:
                print("ELIGIBLE TO MAKE A BANK ACCOUNT")
        except ValueError:
            print("Please enter an integer")

        name = input("Enter your Name : ")
        try:
            acc = int(input("Enter your Account No : "))
        except ValueError:
            print("invalid input")

        add = input("Enter your Address : ")
        pan = input("Enter your Pan Card : ")
        if len(pan)==10:
            print("VALID PAN CARD NUMBER")
        else:
            print("INVALID PAN CARD NUMBER")
            break
        try:
            adh = int(input("Enter your 12 digit Aadhar Card No : "))
            cnt = 0
            while adh != 0:
                r = adh % 10
                cnt = cnt + 1
                adh = adh // 10
            if cnt == 12:
                print("AADHAR CARD NUMBER IS VALID")
            else:
                print("PLEASE ENTER A VALID AADHAR CARD NUMBER")
                break
        except ValueError:
            print("INVALID AADHAAR CARD NUMBER")
        try:
            bal = int(input("Enter your Balance : "))
            if bal < 5000:
                print("NOT ELIGIBLE TO MAKE A BANK ACCOUNT")
                break
        except ValueError:
            print("INVALID ACCOUNT BALANCE")
    elif ir == "2":
        print(f"Name : {name}")
        print(f"Account No : {acc}")
        print(f"Address : {add}")
        print(f"Pan Card : {pan}")
        print(f"Aadhar Card : {adh}")

    elif ir == "3":
       print("CURRENT BALANCE is : ", bal)

    elif ir == "4":
       print("EXIT")
       break

    else:
       print("INVALID CHOICE")






