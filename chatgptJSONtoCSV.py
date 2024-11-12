import json

data = {}


# Open and read the JSON file
with open('chatgptResults.json', 'r') as file:
    data = json.load(file)

output = ""
for key, val in data.items():
    if  isinstance(val, dict):
        lat = val["lat"]
        long = val['long']
        toadd = f"{key},{lat},{long}\n"
        output = output + toadd
        
with open('chatgpt.csv', 'w') as out:
    out.write(output)
    out.close()
