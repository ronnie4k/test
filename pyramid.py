y = "x"
size = int(input("Enter the desired number of stars: "))
for i in range(0,8, -1):
    for j in range(size,i):
        print(y,end="\t")
    for k in range(i + 1):
        print("* ", end="")
    print()


