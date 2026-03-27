import re
s = input()
findall = re.findall(r'\w+',s)
print(len(findall))