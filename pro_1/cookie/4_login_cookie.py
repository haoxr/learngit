# coding=utf-8

import urllib.request
import http.cookiejar
import urllib.parse

filename = 'login_cookie.txt'
cj = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

login_url = 'http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
values = {'username': '370324753@qq.com', 'password': 'Haor900804'}
post_data = urllib.parse.urlencode(values).encode('utf-8')

result = opener.open(login_url, post_data)
cj.save(ignore_discard=True, ignore_expires=True)
# ignore_discard的意思是即使cookies将被丢弃也将它保存下来
# ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
print(result.status, result.reason)
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'}
headers = {'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
url = 'http://my.csdn.net/'
request = urllib.request.Request(url, headers=headers)
result = opener.open(request)

with open('my_csdn.html', 'wb') as f:
    f.write(result.read())
