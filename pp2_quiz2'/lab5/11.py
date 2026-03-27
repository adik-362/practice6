import re
s = input()
upper = re.findall(r'[A-Z]',s)
print(len(upper))