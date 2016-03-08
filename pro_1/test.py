
from urllib import request,error,parse

url = 'https://s.taobao.com/list?q=宠物洗牙&cat=50097750'
url_p = parse.quote('宠物洗牙')
print(type(url_p),url_p)
print(parse.quote(url))
# url_p ='宠物洗牙'.encode()
# print(type(url_p),url_p)
# print(url.encode())
url = 'https://s.taobao.com/list?q='+url_p+'&cat=50097750'

#url = 'https://www.taobao.com'

#print(url_p)

rq = request.Request(url)
response = request.urlopen(rq)
html = response.read()
print(type(html))
page = html.decode('gbk')
print(page)
print(response.status,response.reason)