import re
s = input()
findall = re.findall(r'\d', s)
result = ' '.join(findall)
print(result)