
import os
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'User-Agent':ua.random}
post_url = 'https://www.csindex.com.cn/csindex-home/index-list/query-index-item'
data_dict = { 'pageNum':3, 'pageSize':10}

r= requests.post(post_url, headers=header, data = data_dict)
print(r.text)
