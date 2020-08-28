import geocoder
import csv

adds = []
jsons = []
with open('/Users/daveweimer/Desktop/WFH/BlackBoston/Book1.csv',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        adds.append(row)
for row in adds:
    row = str(row)
    g = geocoder.osm(row)
    jsons.append(g.osm)

keys = jsons[0].keys()

with open('/Users/daveweimer/Desktop/WFH/BlackBoston/results2.csv','w',encoding='utf-8-sig') as res:
    writer = csv.DictWriter(res,fieldnames=keys)
    writer.writeheader()
    for i in jsons:
        writer.writerow(i)

