import requests
from bs4 import BeautifulSoup

headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Connection': 'keep-alive',
'host': 'danjuanfunds.com',
'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW 64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'
}

proxies = {"http":"http://10.144.1.10:8080"}

r = requests.get("https://danjuanfunds.com/djapi/index_eva/dj", proxies=proxies, headers=headers)
#print(r.text)
t = r.text

with open('test.txt', mode='w', encoding='utf-8') as f:
    f.write(t)
#soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
