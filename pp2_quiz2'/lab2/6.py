p = int(input())
n = map(int,input().split())
max_val = 0
for i in n:
    if(max_val<i):
        max_val=i
print(max_val)