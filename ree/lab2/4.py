n = int(input())
f = list(map(int, input().split()))
count = 0
for i in f:
    if(i>0):
        count+=1
print(count)