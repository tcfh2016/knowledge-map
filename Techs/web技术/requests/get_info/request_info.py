import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import re

proxies = {
  "http": "https://10.1.1.10:8080",
}

'''
url = "..."
res = requests.get(url, proxies=proxies, verify=False)
#with open("text.txt", "w", encoding="utf-8") as f:
#    f.write(res.text)

bs = BeautifulSoup(res.text, 'html.parser')
#string = bs.find(attrs={"class":"build-caption page-headline"}).contents[-1]
s = bs.find(class_ = "build-caption page-headline").contents[-1]
date = pd.Timestamp(s[s.find('(')+1 : s.find(')')]).date()
print(date)
today = datetime.date.today()
print (today)
print (date < today)
'''
requests.packages.urllib3.disable_warnings()

url = "https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/UPLANE/job/L2-LO/job/SCT.fuse.asib_abio/32553/console"
res = requests.get(url, proxies=proxies, verify=False)
with open("text.txt", "w", encoding="utf-8") as f:
    f.write(res.text)

bs = BeautifulSoup(res.text, 'html.parser')
s = bs.find(string=re.compile("\'ZUUL_CHANGE\'"))
print(s)
gerrit_id = str(s).split(":")[1].split("'")[1]
print(gerrit_id)
