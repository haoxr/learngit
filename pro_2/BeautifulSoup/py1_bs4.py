# BeautifulSoup模块解析html

from bs4 import BeautifulSoup
from urllib import request
import re

web = request.urlopen('http://www.freebuf.com')
# 没有特别指明解析器，bs4使用了它认为最好的解析器,但是如果你在不同的环境下运行，可能解析器是不一样的。
# 如果没有'html.parser'，会有warning提示，表明了bs4的自动选择解析器来解析的特性。
soup = BeautifulSoup(web.read(),'html.parser')
tags_a = soup.find_all(name='a', attrs={'href': re.compile('^https?://')})
for tag_a in tags_a:
    print(tag_a['href'])
