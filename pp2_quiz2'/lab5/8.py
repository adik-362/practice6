import re
s = input()
p = input()
split = re.split(p,s)
result = ' '.join(split)
print(result)