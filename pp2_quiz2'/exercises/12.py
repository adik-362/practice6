from datetime import datetime
t1 = datetime.strptime(input(),"%Y-%m-%d")
t2 = datetime.strptime(input(),"%Y-%m-%d")
print(abs((t2-t1).days))

