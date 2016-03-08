
import urllib.request

url = 'https://s.taobao.com/search?spm=a21bo.7724922.8452-fline.4.n8vjpE&q=%E5%A5%97%E8%A3%85%E8%A3%99&refpid=' \
      '420460_1006&source=tbsy&style=grid&tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f66'

proxy_handler = urllib.request.ProxyHandler({'https': url})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)

data = opener.open(url)
with data as f:
    print(f.read())
