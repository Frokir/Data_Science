import json

with open("data.json", "r") as outfile:
    r = json.load(outfile)

print(r)