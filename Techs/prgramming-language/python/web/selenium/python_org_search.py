# webdriver提供了所有浏览器驱动的相关功能
from selenium import webdriver
# 类Keys提供了键盘上诸如RETURN, F1, ALT等按键功能。
from selenium.webdriver.common.keys import Keys

# 创建Firefox的驱动实例
driver = webdriver.Firefox()
# get函数会打开URL指定的页面，并且等到它加载完成
driver.get("http://www.python.org")
assert "Python" in driver.title
# 通过find_element_by*系列函数来找到对应的页面元素（这里是搜索框）
elem = driver.find_element_by_name("q")
# 键入“pycon”进行搜索
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
