import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import re

'''
#Method 1
address = input('Enter location: ')
url=urllib.request.urlopen(address)
x=url.read().strip().decode()
print('Retrieving',url)
print('Retrieved', len(x), 'characters')
y=re.findall('<count>([0-9]+)',x)
print('Count :',len(y))
temp=[int(s)for s in y]
print('Sum :',sum(temp))

'''
sss=list()
#Method 2
url = input('Enter location: ')
print('Retrieving', url)
file =  urllib.request.urlopen(url)
data=ET.fromstring(file.read().decode())
sss.append(data.findall('.//count').text)
print(type(data))





'''
#traceback Message:
#for i in data:
#    print(data.findall('.//count').text)
#print(data.find('count').text)
'''
'''
#if I use this
for i in data:
    print(data.findall('.//count').text)

#Then traceback Message:

...in <module>
print(data.findall('.//count').text)
AttributeError: 'list' object has no attribute 'text'
'''
#traceback Message:
#AttributeError: 'list' object has no attribute 'text'


'''
print(type(data))
print('Retrieved', len(data), 'characters')
tree=ET.fromstring(data)
list=tree.findall('commentinfo/comments/comment')
'''
#print(item.find('name'),text)
#for item in tree:
    #print(item.find('name'),text)




#counts = tree.findall('.//count')
#print('Count:',len(counts))
#print('ssss',tree.find('count').text)
#for item in counts:
#    print(item.find('count').text)
