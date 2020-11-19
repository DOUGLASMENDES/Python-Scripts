import json
from urllib.request import urlopen
import ssl

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck",
    "count": 2
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent",
    "count": 5
  } http://py4e-data.dr-chuck.net/comments_42.json
]'''

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

data = urlopen(url, context=ctx).read()
json_data = json.loads(data)

comments_array = json_data['comments']
print('User count:', len(comments_array))

total_sum = 0
for item in comments_array:
    print('Name', item['name'])
    '''
    print('Id', item['id'])
    print('Attribute', item['x'])
    '''
    count = 0
    count = int(item['count'])
    total_sum += count

print('total sum: ' + str(total_sum))