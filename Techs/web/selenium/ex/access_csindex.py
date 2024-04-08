from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os

service = Service(executable_path="/snap/bin/geckodriver")
opts = webdriver.FirefoxOptions()
opts.add_argument("--headless")

driver = webdriver.Firefox(options=opts, service=service)
driver.implicitly_wait(5)


driver.get('https://www.csindex.com.cn/#/indices/family/list')
with open('page_source.txt', 'w') as f:
    f.write(driver.page_source)

export_button = driver.find_elements(By.TAG_NAME, 'button')
print(export_button)

for button in export_button:
    if button.text == '导出列表':
        button.click()
    print(button)