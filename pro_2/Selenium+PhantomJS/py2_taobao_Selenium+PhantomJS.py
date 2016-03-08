from selenium import webdriver
import time

url = 'https://s.taobao.com/search?spm=a21bo.7724922.8452-fline.4.n8vjpE&q=%E5%A5%97%E8%A3%85%E8%A3%99&refpid=' \
      '420460_1006&source=tbsy&style=grid&tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f66'

# webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
# 输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器
driver = webdriver.PhantomJS(executable_path='phantomjs.exe')

# 使用浏览器请求网页
driver.get(url)
# 等待3秒，等待全部加载完成
time.sleep(10)

# 获取整个页面的html
html = driver.page_source.encode('gbk','ignore')
print(html.decode('gbk'))
# 截图
# driver.get_screenshot_as_file('shangpin.jpg')

print('Success!')

# 关闭浏览器
driver.close()
