n = int(input())
result = []
for i in range(n+1):
    if(i%3==0 and i%4==0):
        result.append(str(i))
print(" ".join(result))