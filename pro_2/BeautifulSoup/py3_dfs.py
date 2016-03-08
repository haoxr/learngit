# -*- coding:utf-8 -*-
# 获取整个网站的sitemap

import urllib.request
import urllib.error
import urllib.parse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time
import datetime
import sys

print(sys.getdefaultencoding())

url = input('请输入扫描的url:')
domain = input('请输入包含的域名：')
sites = set()


# 获取一个页面的所有url
def get_local_pages(url, domain):
    pages = set()
    global sites
    repeat_time = 0

    # url = s_url.encode('gbk')

    # 解析传入的url为后面相对路径拼接用
    parse_url = urlparse(url)

    # 防止url读取卡住：自动重读5次
    while True:
        try:
            print('Ready to Open the web!')
            time.sleep(1)
            print('Opening the web : %s' % url)
            # web = urllib.request.urlopen(url=urllib.parse.quote(url),timeout=20)
            web = urllib.request.urlopen(url=url,timeout=20)
            print('Success to Open the web!')
            break
        except urllib.error.URLError as e:
            print('Open Url Error:',e)
            print('Open url Failed!!!Repeat!')
            time.sleep(1)
            repeat_time += 1
            if repeat_time == 5:
                print('打开链接%s错误：%s' % (url,e))
                pages.add('链接打开错误：%s' % url)
                return

    soup = BeautifulSoup(web.read())
    tags = soup.find_all(name='a')

    for tag in tags:
        # 避免参数传递异常
        try:
            ret = tag['href']
        except:
            print('Maybe not the attr : href')
            continue

        parse_page = urlparse(ret)

        # 1 url不为空（协议，域名，路径）
        if parse_page[0] is '' and parse_page[1] is '' and parse_page[2] is '':
            print('Bad Page(协议\域名\路径均为空):%s' % ret)
            continue

        # 2 协议不为空，判断合法性
        if parse_page[0] is not '' and 'http' not in parse_page[0]:
            print('Bad Page(协议不合法,非http):%s' % ret)
            continue

        # 3 域名不为空，domain要包含在域名中
        if parse_page[1] is not '' and domain not in parse_page[1]:
            print('Bad Page(域名不合法,非%s):%s' % (domain, ret))
            continue

        # 4 协议为空，域名不为空(拼接ret),例如：//caipiao.taobao.com
        if parse_page[0] is '' and parse_page[1] is not '':
            print('Fix page(仅域名存在): %s' % ret)
            newpage = parse_url[0] + ':' + ret
            if newpage not in sites:
                print('Add Fix Page(拼接域名):%s' % newpage)
                pages.add(newpage)
            continue

        # 5 协议域名为空，路径不为空(拼接ret)
        if parse_page[0] is '' and parse_page[1] is '':
            print('Fix page(仅路径存在): %s' % ret)
            temp_page = parse_url[0] + '://' + parse_url[1] + '/' + ret
            # 保持URL的干净
            newpage = temp_page[:8] + temp_page[8:].replace('//', '/')
            if newpage not in sites:
                print('Add Fix Page(拼接路径):%s' % newpage)
                pages.add(newpage)
            continue

        # 整理输出
        newpage = ret
        if newpage not in sites:
            print('Add New Page:%s' % newpage)
            pages.add(newpage)

    return pages


# dfs 算法遍历全站(目前中小型网站可用，待完善)
def dfs(pages, domain):
    global sites
    if pages in sites:
        return 'Success!'

    # visited = set()
    # sites = set.union(sites,pages)
    for page in pages:
        if page not in sites:
            sites.add(page)
            get_pages = get_local_pages(page, domain)
            if get_pages is None:
                continue
            dfs(get_pages, domain)
    return

t1 = datetime.datetime.now()
pages = get_local_pages(url, domain)
dfs(pages,domain)
text_name = domain + '全站扫描.txt'
with open(text_name, 'a') as f:
    f.write('\n' + str(datetime.datetime.now()) + '\n')
for i in sites:
    with open(text_name, 'a') as f:
        f.write(i + '\n')

with open(text_name, 'a') as f:
    f.write('\n用时：' + str(datetime.datetime.now() - t1) + '\n')