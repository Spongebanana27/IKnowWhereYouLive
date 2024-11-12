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

pbest = -1
gbest = -1
cbest = -1

pworst = 10000000
gworst = 10000000
cworst = 10000000

for image in data.values():
    pdistance = image["picarta"].strip().replace("miles","")
    gdistance = image["google"].strip().replace("miles","")
    cdistance = image["chatgpt"].strip().replace("miles","")
    nimages = nimages + 1
    if "-1" not in pdistance:
        pguesses = pguesses + 1
        ptotal = ptotal + float(pdistance)
        if pbest == -1 or pbest > float(pdistance):
            pbest = float(pdistance)
        if pworst == 10000000 or pworst < float(pdistance):
            pworst = float(pdistance)
    if "-1" not in gdistance:
        gguesses = gguesses + 1
        gtotal = gtotal + float(gdistance)
        if gbest == -1 or gbest > float(gdistance):
            gbest = float(gdistance)
        if gworst == 10000000 or gworst < float(pdistance):
            gworst = float(pdistance)
    if "-1" not in cdistance:
        cguesses = cguesses + 1
        ctotal = ctotal + float(cdistance)  
        if cbest == -1 or cbest > float(cdistance):
            cbest = float(cdistance) 
        if cworst == 10000000 or cworst < float(pdistance):
            cworst = float(pdistance)
        
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

print("Lowest error distance for Picarta")
print("{0:.2f} miles".format(pbest))
print("Lowest error distance for Google")
print("{0:.2f} miles".format(gbest))
print("Lowest error distance for ChatGPT")
print("{0:.2f} miles\n".format(cbest))

print("Highest error distance for Picarta")
print("{0:.2f} miles".format(pworst))
print("Highest error distance for Google")
print("{0:.2f} miles".format(gworst))
print("Highest error distance for ChatGPT")
print("{0:.2f} miles\n".format(cworst))

print("Average error distance for Picarta")
print("{0:.2f} miles".format(pavg))
print("Average error distance for Google")
print("{0:.2f} miles".format(gavg))
print("Average error distance for ChatGPT")
print("{0:.2f} miles\n".format(cavg))