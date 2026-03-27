import json
data = json.loads(input())
for item in data:
    if item["age"] > 21:
        print(item["owner"])