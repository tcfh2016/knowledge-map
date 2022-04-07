# webdriver提供了所有浏览器驱动的相关功能
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# 类Keys提供了键盘上诸如RETURN, F1, ALT等按键功能。
from selenium.webdriver.common.keys import Keys

# 创建Firefox的驱动实例，会打开浏览器窗口
driver = webdriver.Firefox()
driver.maximize_window()
# get函数会打开URL指定的页面，并且等到它加载完成。加载完成
driver.get("https://app.powerbi.com/groups/me/apps/dcf059b0-fa4c-4e42-a97c-1a052ed659ce/reports/9e95a8fe-2750-4c00-ae31-b664ac2b041d/ReportSection?ctid=5d471751-9675-428d-917b-70f44f9630b0")
element = WebDriverWait(driver, 20).until(lambda x: x.find_element_by_xpath('/html/body/main/section[1]/div[3]/div/a'))
element.click()
