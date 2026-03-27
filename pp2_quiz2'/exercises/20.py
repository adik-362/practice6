from datetime import datetime,timedelta
d = datetime.strptime(input(),"%Y-%m-%d")
n = int(input())
diff = d+timedelta(days=n)
print(diff.strftime("%Y-%m-%d"))

