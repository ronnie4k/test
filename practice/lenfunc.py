n = int(input("Enter a number"))
cnt = 0
while n!=0:
    r = n%10
    cnt = cnt + 1
    n = n//10

print(cnt)