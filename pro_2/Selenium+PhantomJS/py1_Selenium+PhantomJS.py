from selenium import webdriver
import time

url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

# webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
# 输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器
driver = webdriver.PhantomJS(executable_path='phantomjs.exe')

# 使用浏览器请求网页
driver.get(url)
# 等待3秒，等待全部加载完成
time.sleep(3)

# 通过id来定位元素，
# .text获取元素的文本数据
text = driver.find_element_by_id('content').text
print(text)

# 关闭浏览器
driver.close()
