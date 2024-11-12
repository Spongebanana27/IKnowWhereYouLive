import json

data = {}

# Open and read the JSON file
with open('compareDistance.json', 'r') as file:
    data = json.load(file)

pguesses = 0
gguesses = 0
cguesses = 0
nimages = 0

ptotal = 0
gtotal = 0
ctotal = 0
for image in data.values():
    pdistance = image["picarta"].strip().replace("miles","")
    gdistance = image["google"].strip().replace("miles","")
    cdistance = image["chatgpt"].strip().replace("miles","")
    nimages = nimages + 1
    if "-1" not in pdistance:
        pguesses = pguesses + 1
        ptotal = ptotal + float(pdistance)
    if "-1" not in gdistance:
        gguesses = gguesses + 1
        gtotal = gtotal + float(gdistance)
    if "-1" not in cdistance:
        cguesses = cguesses + 1
        ctotal = ctotal + float(cdistance)   
        
print("Number of images tested")
print(nimages)
print("Number of results for Picarta")
print(pguesses)
print("Number of results for Google")
print(gguesses)
print("Number of results for ChatGPT")
print(cguesses)

pavg = ptotal / pguesses
gavg = gtotal / gguesses
cavg = ctotal / cguesses

print("Average error distance for Picarta")
print("{0:.2f} miles".format(pavg))
print("Average error distance for Google")
print("{0:.2f} miles".format(gavg))
print("Average error distance for ChatGPT")
print("{0:.2f} miles".format(cavg))