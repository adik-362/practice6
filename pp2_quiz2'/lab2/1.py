s = int(input())
if(s%4==0 and s%400==0 or s%100!=0):
    print("Yes")
else:
    print("No")