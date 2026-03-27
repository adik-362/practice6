import re
s = input()
p = input()
patt = re.escape(p)
matches = re.findall(patt,s)
print(len(matches))
