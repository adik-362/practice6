import re
s = input()
findall = re.findall(r'\d{2}/\d{2}/\d{4}',s)
print(len(findall))