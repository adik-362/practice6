import json
import re
data = json.loads(input())
for item in data:
    if re.fullmatch(r'[A-Za-z]{5,}', item["owner"]):
        print(item["owner"])