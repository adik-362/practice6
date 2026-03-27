n =  int(input())
f = list(map(int,input().split()))
max_val = 0
for i in f:
    if(i>max_val):
        max_val=i
print(max_val)
