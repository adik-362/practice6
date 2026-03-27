import re
s = input()
word = re.findall(r'\w+',s)
print(len(word))