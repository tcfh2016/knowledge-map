import requests
from bs4 import BeautifulSoup

proxies = {
  "http": "https://10.144.1.10:8080",
}

url = "https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/UPLANE/job/L2-LO/job/SCT.fuse.asib_abio/32196/"
res = requests.get(url, proxies=proxies, verify=False)
with open("text.txt", "w", encoding="utf-8") as f:
    f.write(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
#res = soup.find(attrs={"class":"build-caption page-headline"})
res = soup.find(class_ = "build-caption page-headline")
str = res.contents[-1]
date = str[str.find('(')+1 : str.find(')')].split(' ')[0]
print(date)
