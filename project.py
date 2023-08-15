import random
import json
f=open("websites.json")
data=json.load(f)
number = random.randint(1,10)
print(data[str(number)])