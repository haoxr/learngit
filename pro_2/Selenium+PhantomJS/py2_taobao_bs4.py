from bs4 import BeautifulSoup
import urllib.request

url = 'https://s.taobao.com/search?spm=a21bo.7724922.8452-fline.4.n8vjpE&q=%E5%A5%97%E8%A3%85%E8%A3%99&refpid=' \
      '420460_1006&source=tbsy&style=grid&tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f66'

web = urllib.request.urlopen(url)
html = web.read()
# print(html.decode())

soup = BeautifulSoup(html)
# text = soup.find_all(name='content')

# 根本获取不到商品信息
print('开始：\n', soup.decode('gbk'))

