import re
s = input()
match = re.match(r'Hello',s)
if match:
    print("Yes")
else:
    print("No")