import pandas as pd
from urllib import request
from urllib.request import urlretrieve

proxy = request.ProxyHandler({'https': '10.144.1.10:8080'})
opener = request.build_opener(proxy)
request.install_opener(opener)

es_url = 'https://www.stoxx.com/download/historical_values/hbrbcpe.txt'
vs_url = 'https://www.stoxx.com/download/historical_values/h_vstoxx.txt'
urlretrieve(es_url, './data/es.txt')
urlretrieve(vs_url, './data/vs.txt')
