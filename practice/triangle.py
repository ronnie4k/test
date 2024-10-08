ir = 5

for i in range(0,ir):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")

for i in range(ir,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print("\r")