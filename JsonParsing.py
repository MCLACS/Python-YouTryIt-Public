import json

jsonTxt = ""
f = open('contacts.json')
for line in f:
    line = line.strip()
    jsonTxt = jsonTxt + line
    
contacts = json.loads(jsonTxt)
for contact in contacts:
    print contact["Name"]