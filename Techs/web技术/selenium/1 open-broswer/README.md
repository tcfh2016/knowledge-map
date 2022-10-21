## [打开浏览器]()

最简单的方式就是通过get()函数来打开页面：

```
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.google.com")
```

在API文档[7.20. Remote WebDriver](https://selenium-python.readthedocs.io/api.html?highlight=maximize_window#module-selenium.webdriver.remote.webdriver)可以找到driver可以使用的很多功能。比如：

```
close() #关闭当前窗口
find_element_by_xpath() #查找元素
fullscreen_window() #全屏
get(url) #在当前窗口里面加载某个页面
get_screenshot_as_file(filename) #截图
get_window_position(windowHandle='current') #获取当前窗口坐标
get_window_size(windowHandle='current') #获取当前窗口尺寸
maximize_window() #最大化窗口
set_page_load_timeout(time_to_wait) #设置页面最大的加载时间
switch_to_active_element()
switch_to_alert()
```

使用driver.get()加载某个页面时，该函数尽管返回了（"onload"事件已处理）但是内容可能还没有加载完全（使用了很多AJAX就无法准确得知状态）。这个时候需要等待的话一种方式是使用python的时间模块提供的sleep功能，其实在[7.35. Wait Support](https://selenium-python.readthedocs.io/api.html?highlight=maximize_window#module-selenium.webdriver.support.wait)里面找到了对应的等待功能，亲测可用：

```
#将等待时间设定为10秒，10秒没有找到那么超时。
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(“someId”))
```

## options参数

options参数用来配置浏览器启动时的属性：

- 设置 chrome 二进制文件位置 (binary_location)
- 添加启动参数 (add_argument)，`options.add_argument('--headless')`是让浏览器不提供可视化页面
- 添加扩展应用 (add_extension, add_encoded_extension)
- 添加实验性质的设置参数 (add_experimental_option)
- 设置调试器地址 (debugger_address)

参考：

- [python+selenium+Chrome options参数](https://www.cnblogs.com/guapitomjoy/p/12150416.html)
- [Class: Selenium::WebDriver::Firefox::Options](https://www.selenium.dev/selenium/docs/api/rb/Selenium/WebDriver/Firefox/Options.html)
