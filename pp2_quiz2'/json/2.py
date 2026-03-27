import json
import re
data = json.loads(input())
for car in data:
    if re.fullmatch(r"[A-Z]{3} - \d{3}",car ["plate"]):
        print(car["owner"])