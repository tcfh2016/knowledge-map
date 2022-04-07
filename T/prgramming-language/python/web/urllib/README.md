## urllib

与`requests`是什么关系？

## 安装

在working pc上面安装的时候提示“No matching distribution found for urllib”错误：

```
ERROR: Could not find a version that satisfies the requirement urllib (from versions: none)

ERROR: No matching distribution found for urllib
```

查找[Cannot import urllib in Python](https://stackoverflow.com/questions/40050630/cannot-import-urllib-in-python)之后才发现`urllib`是标准的python库，本身不需要再额外安装，直接使用就好了。


## urlretrieve 的作用

urlretrieve()方法直接将远程数据下载到本地：

```
urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)
```

url指示远程文件，filename指示本地存储文件位置，reporthook是在连接建立或者每个数据块传输
完成之后进行调用，可以用来显示下载进度。

参考：

- [urllib.request.urlretrieve](https://docs.python.org/3.3/library/urllib.request.html)

## urlopen 的作用

使用用urllib.request模块的urlopen()获取页面。


参考：

- [urllib模块的使用](https://www.cnblogs.com/Lands-ljk/p/5447127.html)

## 使用urlretrieve出现"WinError 10060"错误

```
urllib.error.URLError: <urlopen error [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond>
```

网络链接的问题，尝试设置代理可以解决问题。这里需要注意的是如果是为http设置了代理，那么只
能访问http的URL，对于https的URL依然会失败。

```
import urllib.request as request

proxy = request.ProxyHandler({'http': '10.144.1.10:8080'})
opener = request.build_opener(proxy)
request.install_opener(opener)

j = request.urlopen('http://www.google.com')
print(j)
```

参考：

- [Python: URLError: <urlopen error [Errno 10060]](https://stackoverflow.com/questions/15820739/python-urlerror-urlopen-error-errno-10060)
- [Proxy with urllib2](https://stackoverflow.com/questions/1450132/proxy-with-urllib2)

## ImportError: cannot import name 'urlretrieve' from 'urllib'

在Python 3.7.2中使用 `from urllib import urlretrieve`提示错误，之后查询得知该用法在
Python 2.x，在Python 3.x中需要使用`from urllib.request import urlretrieve`。

参考：

- [urllib.urlretrieve file python 3.3](https://stackoverflow.com/questions/21171718/urllib-urlretrieve-file-python-3-3)
