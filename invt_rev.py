ir = "*"
s = int(input("Enter a number: "))
for i in range (0,s):
    for j in range(0,s):
        if i > j:
            print(" ",end="\t")
        else:
            print(ir, end="\t")
    print("")