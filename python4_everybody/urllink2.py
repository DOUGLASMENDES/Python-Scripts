# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = 0
total_sum = 0

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    count+=1
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    item = tag.contents[0]
    value = int(item)
    print('Contents:', item)
    print('Attrs:', tag.attrs)
    total_sum += value

print('Count: ' + str(count))
print('Sum: ' + str(total_sum))