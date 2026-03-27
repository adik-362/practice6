import re
s = input()
search = re.search(r'^[A-Z][a-z]+[0-9]$',s)
if search:
    print("Yes")
else:
    print("No")