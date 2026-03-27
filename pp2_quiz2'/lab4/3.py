n = int(input())
result = []
for i in range(n):
    if (i%3==0 and i%4==0):
        result.append(str(i))
print(" ".join(result))