# coding=utf-8
from urllib import request, parse

url = 'http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
values = {'username': '370324753@qq.com', 'password': 'Haor900804'}
data = parse.urlencode(values)
with request.urlopen(url, data.encode('utf-8')) as f:
    print('POST方法：\n', f.status, f.reason)


# get

getdata = url + '?' + data
with request.urlopen(getdata) as f:
    print('GET方法：\n', f.status, f.reason)
