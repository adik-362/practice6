import json
import re
data = json.loads(input())
for item in data:
    if item['score']>=85:
        print(item['name'])
