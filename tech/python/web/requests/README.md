# rquests

requests 是基于Python的第三方HTTP库，用来请求网络资源。

## 代理

配置代理有两种方法：

- 为任意请求提供proxies参数
- 通过环境变量设定HTTP_PROXY和HTTPS_PROXY配置代理

```
# 方式一
import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

requests.get("http://example.org", proxies=proxies)

# 方式二
$ export HTTP_PROXY="http://10.10.1.10:3128"
$ export HTTPS_PROXY="http://10.10.1.10:1080"

$ python
>>> import requests
>>> requests.get("http://example.org")
```

另外还可以为特定的主机设置代理，比如如下为主机`10.20.1.128`设置代理，其中必须包含连接方
式`http://`。

```
proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}
```

## 参考

- [代理](https://2.python-requests.org//zh_CN/latest/user/advanced.html#proxies)
