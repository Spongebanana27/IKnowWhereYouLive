import json

data = {}


# Open and read the JSON file
with open('result.json', 'r') as file:
    data = json.load(file)

output = ""
for image in data:
    key = image["filename"]
    lat = image["gps_location"]["latitude"]
    long = image["gps_location"]["longitude"]
    
    toadd = f"{key},{lat},{long}\n"
    output = output + toadd
        
with open('result.csv', 'w') as out:
    out.write(output)
    out.close()
