start = 25
end = 50
print("Print Prime numbers between",start, "and", end,"are:")
for i in range(start,end ):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)