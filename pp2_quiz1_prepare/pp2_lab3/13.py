n = int(input())
arr = list(map(int,input().split()))
count=0
avg = sum(arr)/n
for x in arr:
    if x > avg:
        count+=1
print(count)