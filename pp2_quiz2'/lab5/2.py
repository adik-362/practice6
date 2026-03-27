import re
s = input()
p = input()
search = re.search(p,s)
if search:
    print("Yes")
else:
    print("No")