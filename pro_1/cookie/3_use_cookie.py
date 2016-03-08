# coding=utf-8
import urllib.request
import http.cookiejar

# filename = 'cookie.txt'

# 声明一个CookieJar对象保存cookie
# cj = http.cookiejar.CookieJar()

# MozillaCookieJar对象保存cookie，之后写入文件
# cj = http.cookiejar.MozillaCookieJar(filename)

# 创建一个MozillaCookieJar实例对象
cj = http.cookiejar.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cj.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求
req = urllib.request.Request('http://www.baidu.com')

# 利用HTTPCookieProcessor对象创建cookie处理器
pro = urllib.request.HTTPCookieProcessor(cj)
# 通过handler来构建opener
opener = urllib.request.build_opener(pro)

response = opener.open(req)
print(response.read())
# for item in cj:
#     print('name=', item.name)
#     print('value=', item.value)

# cj.save(ignore_discard=True,ignore_expires=True)
