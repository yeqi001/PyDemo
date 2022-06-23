import re
import urllib.request
from urllib.request import urlopen

myURL = urlopen("https://www.nipic.com/")
with open("../PyDemo/test.txt", 'wb+') as f:
    f.write(myURL.read())
    f.seek(0)  # 将游标移动到文章开头
    # e=f.read()
    # e=f.read().decode('utf-8')
    result = re.findall('src="(.*?)"/>', f.read().decode('utf-8'))
    for i in range(len(result)):
        urllib.request.urlretrieve(result[i], '../PyDemo/test/%d.jpg' % i)
