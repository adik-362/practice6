from datetime import datetime
b = datetime.strptime(input(), "%Y-%m-%d UTC%z")
now = datetime.strptime(input(), "%Y-%m-%d UTC%z")
year = now.year
try:
    next_b = b.replace(year=year)
except:
    next_b = b.replace(year=year,day=28)
if next_b < now:
    try:
        next_b = b.replace(year=year+1)
    except:
        next_b = b.replace(year=year+1,day=28)
diff = (next_b - now).total_seconds()
print(int(diff/86400))