import json
import re
data = json.loads(input())
for item in data:
    if re.fullmatch(r'\+7\d{10}',item['phone']):
        print(item['id'])

