import json

data = {}


# Open and read the JSON file
with open('output.json', 'r') as file:
    data = json.load(file)

output = ""
for key, val in data.items():
    if  isinstance(val, dict):
        lat = val["ai_lat"]
        long = val['ai_lon']
        toadd = f"{key},{lat},{long}\n"
        output = output + toadd
        
with open('output.csv', 'w') as out:
    out.write(output)
    out.close()
