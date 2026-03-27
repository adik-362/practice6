n = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]
max_index = 0

for i in range(n):
    if arr[i] > max_val:
        max_val = arr[i]
        max_index = i

print(max_index)