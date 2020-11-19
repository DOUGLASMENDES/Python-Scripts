# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def navigate(url, count, position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    i = 0
    for tag in tags:
        i+=1
        if i == int(position):
            new_url = tag.get('href', None)
            new_count = int(count) - 1
            print_item(new_url)
            if new_count > 0:
                navigate(new_url, new_count, position)
            break

def print_item(link):
    temp_s = link.replace('http://py4e-data.dr-chuck.net/known_by_','')
    temp_s = temp_s.replace('.html','')
    print(temp_s)


url = input('Enter URL: ')
count = input('Enter Count: ')
position = input('Enter position: ')

print(" ")
print_item(url)
navigate(url, count, position)