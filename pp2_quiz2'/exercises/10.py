import json
import re
data = json.loads(input())
for item in data:
    if item['age']>25:
        print(item['name'])

        