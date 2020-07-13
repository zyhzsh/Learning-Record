import json
import urllib.request, urllib.parse, urllib.error

address=input("Enter the Address- ")
url=urllib.request.urlopen(address)
data=url.read().decode()
info=json.loads(data)

print('Retrieving',address)
print('Retrieved', len(data), 'characters')
sum=0
for item in info['comments']:
    sum=sum+item['count']
print('Sum: ',sum)
