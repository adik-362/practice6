from datetime import datetime, timedelta
d = datetime.strptime(input(), "%Y-%m-%d")
n = int(input())
result = d + timedelta(days=n)
print(result.strftime("%Y-%m-%d"))