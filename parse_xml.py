
#return two deltas(of IDs) for two compared xml files

import xml.etree.ElementTree

e = xml.etree.ElementTree.parse(r'C:/Users/aking/Documents/Python/xml/data/SXM_LinkIncCon_V3.xml').getroot()
f = xml.etree.ElementTree.parse(r'C:/Users/aking/Documents/Python/xml/data/SXM_LinkIncCon_V3_dev.xml').getroot()

a=[]
b=[]

[a.append(x.get('ID')) for x in e.findall('INCIDENT')]
[b.append(x.get('ID')) for x in f.findall('INCIDENT')]

def returnNotMatches(c, d):
    return [[x for x in c if x not in d], [x for x in d if x not in c]]
        
print(returnNotMatches(a, b))

