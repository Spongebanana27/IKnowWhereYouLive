import csv
import json
from geopy.distance import geodesic

actual = {}
with open('result.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
        file = line[0].split("\\")[-1]
        lat = line[1]
        long = line[2]
        actual[file] = [lat, long]

picarta = {}
with open('output.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
        file = line[0]
        lat = line[1]
        long = line[2]
        picarta[file] = [lat, long]

google = {}
with open('strippedresult.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
        file = line[0].split("\\")[-1]
        lat = line[1]
        long = line[2]
        google[file] = [lat, long]


chatgpt = {}
with open('chatgpt.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
        file = line[0]
        lat = line[1]
        long = line[2]
        chatgpt[file] = [lat, long]

output = {}

for image in actual.keys():
    lat = actual[image][0]
    long = actual[image][1]
    target = (f"{lat},{long}")

    plat = picarta[image][0]
    plong = picarta[image][1]
    pguess =  (f"{plat},{plong}")

    pmiles = geodesic(target, pguess).miles

    glat = google[image][0]
    glong = google[image][1]
    gmiles = -1
    if glat != "NULL" or glong != "NULL":
        gguess =  (f"{glat},{glong}")
        gmiles = geodesic(target, gguess).miles

    clat = chatgpt[image][0]
    clong = chatgpt[image][1]
    cguess =  (f"{clat},{clong}")

    cmiles = geodesic(target, cguess).miles

    data = {}
    data["picarta"] = f"{pmiles:.2f} miles"
    data["google"] = f"{gmiles:.2f} miles"
    data["chatgpt"] = f"{cmiles:.2f} miles"
    output[image] = data

# Serializing json
json_output = json.dumps(output, indent=4)
 
# Writing to json file
with open("compareDistance.json", "w") as outfile:
    outfile.write(json_output)


