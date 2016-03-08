# coding=utf-8

import urllib.request
import urllib.error
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    print(response.status, response.reason)
    content = response.read().decode('utf-8')
except urllib.error.URLError as e:
    print(e)

pattern = re.compile('<h2>(.*?)</h2>.*?class="content">(.*?)<!--.*?</div>(.*?)<div class="stats">', re.S)
# pattern = re.compile('<h2>(.*?)</h2>.*?class="content">(.*?)<!--', re.S)
items = re.findall(pattern, content)
n = 1
for item in items:
    haveIMG = re.search('img',item[2])
    if not haveIMG:
        print('第%d条消息：\n用户：%s\n内容：%s' % (n, item[0], item[1]))
    n += 1


# with open('qsbk_save.txt','w') as f:
#     f.write(str(item))
