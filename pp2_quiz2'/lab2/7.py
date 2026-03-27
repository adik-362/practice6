n = int(input())
arr = list(map(int, input().split()))
max_val = arr[0]
pos = 0
for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
        pos = i
print(pos)
