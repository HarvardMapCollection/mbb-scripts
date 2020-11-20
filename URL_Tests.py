import urllib.request
import xmltodict
#import xml.etree.ElementTree as ET


xml_request = urllib.request.urlopen('http://api.lib.harvard.edu/v2/items?recordIdentifier=990117369670203941')

doc = xmltodict.parse(xml_request)
#for key, value in doc.items():
#    print(key, value)

print(doc['results']['items']['mods:mods']['mods:titleInfo']['mods:title'])





#tree = ET.parse(xml_request)
#root = tree.getroot()
#print([elem.tag for elem in root.iter()])

#for title in root:
#    print(child.tag, child.attrib)


