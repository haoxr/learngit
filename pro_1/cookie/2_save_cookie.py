# coding=utf-8
import urllib.request
import http.cookiejar

filename = 'save_cookie.txt'

# 声明一个CookieJar对象保存cookie
#cj = http.cookiejar.CookieJar()

# MozillaCookieJar对象保存cookie，之后写入文件
cj = http.cookiejar.MozillaCookieJar(filename)

# 利用HTTPCookieProcessor对象创建cookie处理器
pro = urllib.request.HTTPCookieProcessor(cj)
# 通过handler来构建opener
opener = urllib.request.build_opener(pro)
opener.open('http://www.baidu.com')
# for item in cj:
#     print('name=', item.name)
#     print('value=', item.value)

cj.save(ignore_discard=True,ignore_expires=True)
