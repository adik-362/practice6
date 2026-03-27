import json
import re
data = json.loads(input())
for item in data:
    if re.fullmatch(r'[A-Z]{2}-\d{4}',item['code']):
        print(item['product'])
