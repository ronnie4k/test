n = int(input("Enter a number: "))
a=n
if n<0:
    print("false")
else:
    s = 0
    while n!=0:
        r = n%10
        s = s*10+r
        n = n//10
    if s == a:
        print("true")
    else:
        print("false")
