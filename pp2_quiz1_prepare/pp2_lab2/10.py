n = int(input())
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])
arr.sort(reverse=True)
for x in arr:
    print(x, end=" ")
