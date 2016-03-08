# 符合条件的单页url扫描

import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time
import datetime

url = input('请输入扫描的url:')
domain = input('请输入包含的域名：')
pages = set()


# 获取一个页面的所有url
def get_local_pages(url,domain):
    global pages
    repeat_time = 0

    # 解析传入的url为后面相对路径拼接用
    parse_url = urlparse(url)

    # 防止url读取卡住：自动重读5次
    while True:
        try:
            print('Ready to Open the web!')
            time.sleep(1)
            print('Opening the web : %s' % url)
            web = urllib.request.urlopen(url=url, timeout=10)
            print('Success to Open the web!')
            break
        except:
            print('Open url Failed!!!Repeat!')
            time.sleep(1)
            repeat_time += 1
            if repeat_time == 5:
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
            if newpage not in pages:
                print('Add Fix Page(拼接域名):%s' % newpage)
                pages.add(newpage)
            continue

        # 5 协议域名为空，路径不为空(拼接ret)
        if parse_page[0] is '' and parse_page[1] is '':
            print('Fix page(仅路径存在): %s' % ret)
            # temp_page = url + '/' + ret
            temp_page = parse_url[0] + '://' + parse_url[1] + '/' + ret
            # 保持URL的干净
            newpage = temp_page[:8] + temp_page[8:].replace('//', '/')
            if newpage not in pages:
                print('Add Fix Page(拼接路径):%s' % newpage)
                pages.add(newpage)
            continue

        # 整理输出
        newpage = ret
        if newpage not in pages:
            print('Add New Page:%s' % newpage)
            pages.add(newpage)
    return pages


get_local_pages(url,domain)
text_name = domain + '符合条件的单页扫描.txt'
with open(text_name, 'a') as f:
    f.write('\n' + str(datetime.datetime.now()) + '\n')
for i in pages:
    with open(text_name, 'a') as f:
        f.write(i + '\n')
