import re
s = input()
for i in re.findall(r'\d',s):
    print(i,end=" ")