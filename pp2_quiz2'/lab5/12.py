import re
s = input()
digit = re.findall(r'\d{2}',s)
result = ' '.join(digit)
print(result)