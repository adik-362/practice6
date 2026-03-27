lst = input().split()
n = int(input())
gen = (i for _ in range(n) for i in lst)
for i in gen:
    print(i, end=" ")
