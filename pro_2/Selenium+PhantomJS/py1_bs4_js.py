from bs4 import BeautifulSoup
import urllib.request

url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

web = urllib.request.urlopen(url)
html = web.read()
# print(html.decode())

soup = BeautifulSoup(html)
# text = soup.find_all(name='content')
# print(soup)
for tag in soup.tagStack:
    print('开始：\n', tag)
