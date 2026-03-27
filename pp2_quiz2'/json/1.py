import json
data = json.loads(input())
for name,email in data.items():
    if "@" in email and "." in email:
        print(name)