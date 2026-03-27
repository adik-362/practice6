n = int(input())
arr = input().split()
count = 0
for x in arr:
    if int(x)>0:
        count+=1
print(count)