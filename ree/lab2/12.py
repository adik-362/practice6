n = int(input())
f = list(map(int,input().split()))
result = []
for i in f:
    result.append(str(i*i))
print(" ".join(result))