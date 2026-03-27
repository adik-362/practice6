n = int(input())
result = []
for i in range(n+1):
    if 2**i > n:
        break
    result.append(str(2**i))
print(" ".join(result))