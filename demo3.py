import re
import urllib.request
from urllib.request import urlopen

myURL = urlopen("https://www.nipic.com/")
with open("../PyDemo/test.txt",'w+') as f:
    f.write(str(myURL.read()))
with open("../PyDemo/test.txt",'r') as f:
    e=f.read()
result = re.findall(r'src="(.*?)"/>',e)
for i in range(len(result)):
    urllib.request.urlretrieve(result[i], '../PyDemo/test/%d.jpg'%i)
