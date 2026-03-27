p = int(input())
keys = input().split()
values = input().split()
q = input()
d = dict(zip(keys, values))
if q in d:
    print(d[q])
else:
    print("Not found")