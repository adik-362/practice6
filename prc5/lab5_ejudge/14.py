import re
s = input()
if re.compile(r'^\d+$'):
    print("Match")
else:
    print("No Match")