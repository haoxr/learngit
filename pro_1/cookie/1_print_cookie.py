# coding=utf-8
import urllib.request
import http.cookiejar

# 声明一个CookieJar对象保存cookie
cj = http.cookiejar.CookieJar()
# 利用HTTPCookieProcessor对象创建cookie处理器
pro = urllib.request.HTTPCookieProcessor(cj)
# 通过handler来构建opener
opener = urllib.request.build_opener(pro)
opener.open('http://www.baidu.com')
for item in cj:
    print('name=', item.name)
    print('value=', item.value)
