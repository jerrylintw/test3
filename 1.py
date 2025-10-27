number_of_leap_years = []
a,b = map(int,input().split())
for i in range(a+1,b-1):
    if (i%4==0 and i%100!=0) or (i%400==0):
        number_of_leap_years.append(i)
print(len(number_of_leap_years))
