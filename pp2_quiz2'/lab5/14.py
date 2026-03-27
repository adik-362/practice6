import re
s = input()
match = re.match(r'^[0-9]+$',s)
if match:
    print("Yes")
else:
    print("No")