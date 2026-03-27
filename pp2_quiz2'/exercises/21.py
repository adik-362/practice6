from datetime import datetime
d = datetime.strptime(input(),"%Y-%m-%d")
print(d.strftime("%A"))