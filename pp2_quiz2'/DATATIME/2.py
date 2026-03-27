from datetime import datetime
start = (datetime.strptime(input(),"%Y-%m-%d"))
n = int(input())
for _ in range(n):
    d = (datetime.strptime(input(),"%Y-%m-%d"))
    print((d-start).days)