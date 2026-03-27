from datetime import datetime
dates= (datetime.strptime(input(),"%Y-%m-%d"))
start = [datetime.strptime(input(),"%Y-%m-%d") for _ in range(4)]
start = dates[0]
for d in dates[1:]:
    print((d-start).days)

      