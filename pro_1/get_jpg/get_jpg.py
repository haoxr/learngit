# coding=utf-8
import urllib.request
import urllib
import re

'''
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

'''


def getHtml(url):
    with urllib.request.urlopen(url) as f:
        html = f.read()
    return str(html)


def getImg(html):
    reg = r'http\:\/\/imgsrc\.baidu\.com\/forum\/\S+\.jpg'
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg, html)
    imglist
    # return imglist
    x = 1
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1


html = getHtml('http://tieba.baidu.com/p/4356535602')
# print(html)
getImg(html)
