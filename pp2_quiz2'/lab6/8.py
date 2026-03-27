s = int(input())
p = map(int,input().split())
result = sorted(set(p))
result = list(map(str,result))
print(" ".join(result))

