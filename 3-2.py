a,b,c =map(int,input().split())
if (a<=b<=c and a+b<=c):
    print("invalid")
elif a**2 + b**2 == c**2:
    print("right")
else:
    print("scalaene")