# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
pos=input('Pos - ')
times=input('Times - ')
def Getname(url,pos,times):
    times=int(times)-1
    if times >=0:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        count=-1
        for tag in tags:
            count=count+1
            if count==int(pos)-1 :
                Getname(tag.get('href',None),pos,times)
                print(tag.get('href',None))
                break
Getname(url,pos,times)
