import json

data = {}


# Open and read the JSON file
with open('strippedCloudResults.json', 'r') as file:
    data = json.load(file)

output = ""
for image in data:
    key = image["filename"]
    lat = "NULL"
    long = "NULL"
    if "location" in image.keys():
        lat = image["location"]["lat"]
        long = image["location"]["lng"]
    toadd = f"{key},{lat},{long}\n"
    output = output + toadd
        
with open('strippedresult.csv', 'w') as out:
    out.write(output)
    out.close()
