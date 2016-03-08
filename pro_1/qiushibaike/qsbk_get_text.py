# coding=utf-8

import urllib.request
import urllib.error
import re


class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}
        # 存放段子的函数，每一个元素是每一页的
        self.stories = []
        # 存放程序是否运行的变量
        self.enable = False

    # 传入页码，返回页面代码
    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib.error as e:
            if hasattr(e, 'reason'):
                print('连接糗事百科失败，错误原因：', e.reason)
            return None

    # 传入页码，并存储不带图片的段子到列表
    def getpageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print('页面加载失败......')
            return None
        # re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。
        pattern = re.compile('<h2>(.*?)</h2>.*?class="content">(.*?)<!--.*?</div>(.*?)<div class="stats">', re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            haveImg = re.search('img', item[2])
            if not haveImg:
                text = re.sub('<br/>', '\n', item[1])
                pageStories.append([item[0].strip(), text.strip()])
        return pageStories

    # 加载并提取页面内容，到列表
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getpageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    # 调用方法，每次敲回车打印段子
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input_text = input()
            if input_text.lower() == 'q':
                self.enable = False
                return
            self.loadPage()
            print('第%s页-发布人：%s\n正文：\n%s' % (page, story[0], story[1]))

    # 开始方法
    def start(self):
        print('正在读取糗事百科段子，按回车继续，按q或Q退出。')
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStroies = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStroies, nowPage)


spider = QSBK()
spider.start()
