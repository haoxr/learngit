# 获取单页的所有url

import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time
import datetime

url = input('请输入扫描的url:')
domain = input('请输入包含的域名：')
pages = set()


# 获取一个页面的所有url
def get_local_pages(url):

    repeat_time = 0

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

        if ret is '':
            continue

        # 整理输出
        if ret not in pages:
            parse = urlparse(ret)
            print('Add New Page:',ret)
            print(parse,'\n')
            pages.add(ret)
            with open(text_name, 'a') as f:
                f.write(ret + '\n' + str(parse)+'\n\n')
            continue

    return 'Success!'

text_name = domain + '单页所有url解析扫描.txt'
with open(text_name, 'a') as f:
    f.write('\n\n' + str(datetime.datetime.now()) + '\n\n')
get_local_pages(url)
