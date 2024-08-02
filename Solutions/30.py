import json

x = int(input(">>"))
data = {'Data': x}
with open('json.json', 'w') as file:
    json.dump(data, file)
