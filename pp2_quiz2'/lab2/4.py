n = int(input())
s = map(int,input().split())
count = 0
for i in s:
    if (i>0):
        count+=1
print(count)