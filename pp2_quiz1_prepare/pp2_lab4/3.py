n = int(input())
print(*(i for i in range(0, n + 1) if i % 12== 0), sep=" ")
