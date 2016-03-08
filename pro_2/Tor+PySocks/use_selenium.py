from selenium import webdriver

url = 'https://s.taobao.com/search?spm=a21bo.7724922.8452-fline.4.n8vjpE&q=%E5%A5%97%E8%A3%85%E8%A3%99&refpid=' \
      '420460_1006&source=tbsy&style=grid&tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f66'

# 假定9999端口开启tor服务
service_args = ['--proxy=localhost:9999', '--proxy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path="phantomjs.exe",service_args=service_args)
driver.get(url)
print(driver.page_source)
driver.close()
