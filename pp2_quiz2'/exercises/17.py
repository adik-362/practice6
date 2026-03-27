import json
import re
data = json.loads(input())
for item in data:
    if item['price']<500:
        print(item['product'])


        