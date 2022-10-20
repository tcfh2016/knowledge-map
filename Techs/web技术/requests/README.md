## [requests](https://requests.readthedocs.io/en/latest/)

requests 是基于Python的第三方HTTP库，用来请求网络资源。


## 安装

如果提示“ModuleNotFoundError: No module named 'requests'”，那么执行`pip install requests`安装该模块即可。


## 使用

最简单的使用就是如`r = requests.get('https://api.github.com/events')`，不过这里的返回结果保存在一个requests对象里面，我们就是从这个对象里面获取想要的信息。

- 通过`r.text`我们可以获取该对象的文本形式。
- 通过`r.content`可以获取到该对象的二进制形式。
- 通过`r.json()`可以获取到该对象的json形式。

当我们获得了整个页面的内容之后，还需要进一步解析，而这些解析工作就可以使用其他的python库来完成，比如`Beautiful Soup`。


## `[SSL: CERTIFICATE_VERIFY_FAILED]`

使用requests访问https的时候提示`[SSL: CERTIFICATE_VERIFY_FAILED]`的错误，解决方法，传入`verify=False`参数：

```
res = requests.get(url, proxies=proxies, verify=False)
```

参考：

- [4 Ways to fix SSL: CERTIFICATE_VERIFY_FAILED in Python](https://www.howtouselinux.com/post/ssl-certificate_verify_failed-in-python)
- [Python Requests throwing SSLError](https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror)