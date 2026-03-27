s = int(input())
p = map(int, input().split())
print(sum(map(lambda x: x > 0, p)))