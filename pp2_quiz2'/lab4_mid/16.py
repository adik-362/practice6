from datetime import datetime
t1 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S UTC%z")
t2 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S UTC%z")
print(int((t2 - t1).total_seconds()))