n = int(input())
result = []

for i in range(2, n):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        result.append(str(i))

print(" ".join(result))