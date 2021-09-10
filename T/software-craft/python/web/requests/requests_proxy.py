import requests

proxies = {"http":"http://1.1.1.1:8080"}

r = requests.get("http://baidu.com", proxies=proxies)
print(r)
