n = int (input())
arr = input().split()
max_val=0
for x in arr:
    if int(x)>max_val:
        max_val=int(x)
print(max_val)