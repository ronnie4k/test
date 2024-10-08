n = int(input("Enter a number: "))
m = n
s = 0
while n!=0:
    r = n%10
    s = s*10+r
    n = n//10

if m == s:
     print("THE NUMBER IS A PALINDROME")
else:
     print("THE NUMBER IS NOT A PALINDROME")



