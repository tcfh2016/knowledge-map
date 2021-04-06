import urllib.request as request

proxy = request.ProxyHandler({'http': '10.144.1.10:8080'})
opener = request.build_opener(proxy)
request.install_opener(opener)

j = request.urlopen('http://www.google.com')
print(j)
