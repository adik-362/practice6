import re
s = input()
findall = re.findall(r'\b[a-zA-Z]{3}\b',s)
print(len(findall))