import json
import re
data = json.loads(input())
for item in data:
    if re.fullmatch(r'[a-z]+@[a-z]+\.com',item['email']):
        print(item['name'])
