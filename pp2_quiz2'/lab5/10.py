import re
s = input()
findall = re.findall(r'dog|cat',s)
if findall:
    print("Yes")
else:
    print("No")