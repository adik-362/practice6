import re
line = input().strip()
pattern = r"Name: (.+), Age: (.+)"
match = re.search(pattern, line)
if match:
    name = match.group(1)
    age = match.group(2)
    print(f"{name} {age}")