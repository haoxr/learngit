# url和合法性判断
from urllib.parse import urlparse
import urllib.error

url = set()
url.add('javascript:void(0)')
url.add('http://freebuf.com/geek')
url.add('https://freebuf.com:443/geek?id=1#sid')
url.add('ftp://freeme.com/ss/s/s')
url.add('sssfadea://ssss.ss')
url.add('//freebuf.com/s/s/s')
url.add('/freebuf.com/s/s/s/')
url.add('//freebuf.com/s/s/s/')
url.add('path/me')
url.add('path?ss=1')
url.add('path?ss=1&s=1')
url.add('path?ss=1#arch')
url.add('?ss=1')
url.add('#arch')
for item in url:
    try:
        print(item)
        parse = urlparse(item)
        print(parse,'\n')
    except urllib.error as e:
        print(e)
        continue
