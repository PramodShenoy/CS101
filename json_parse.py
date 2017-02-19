import json
from pprint import pprint

f = open('pets1.txt', 'r')
pets = json.loads(f.read())
f.close()

pprint(pets)