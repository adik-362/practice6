import json
import re
data = json.loads(input())
for item in data:
    if re.fullmatch(r'@[a-z_]+',item['username']):
        print(item['id'])

