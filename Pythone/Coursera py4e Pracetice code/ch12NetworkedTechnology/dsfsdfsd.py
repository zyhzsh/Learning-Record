import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter - ")
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieving ',url)
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)
allcounts = tree.findall('comments/comment')
print('Count:',len(allcounts))
sum=0
for item in allcounts:
    sum = sum+int(item.find('count').text)
print ("Sum:",sum)
