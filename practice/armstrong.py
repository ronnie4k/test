n = int(input("Enter a Number: "))
m = n
s = 0
while n!=0:
    r = n%10
    s = s+r**3
    n = n//10
if m == s:
    print("THE NUMBER IS A ARMSTRONG")
else:
    print("THE NUMBER IS NOT A ARMSTRONG")
