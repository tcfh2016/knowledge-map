# Connect

## 配置代理

配置代理有两种方法：一、为任意请求提供proxies参数；二、通过环境变量设定HTTP_PROXY和HTTPS_PROXY配置代理。

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

另外还可以为特定的主机设置代理，比如如下为主机`10.20.1.128`设置代理，其中必须包含连接方式`http://`。

```
proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}
```


## `ValueError: check_hostname requires server_hostname`

get http的时候没有问题，但是https的时候提示`ValueError: check_hostname requires server_hostname`错误。

```
proxies = {
  "http": "http://10.1.1.10:8080",
  "https": "http://10.1.1.10:8080",
}
```

按照[ValueError: check_hostname requires server_hostname](https://stackoverflow.com/questions/67297278/valueerror-check-hostname-requires-server-hostname)里面的描述这个问题的原因在于proxy配置了http代理但是地址使用了https，解决方法是将如上代理修正为：

```
proxies = {
  "http": "https://10.144.1.10:8080",
}
```

参考

- [代理](https://2.python-requests.org//zh_CN/latest/user/advanced.html#proxies)


## `[SSL: CERTIFICATE_VERIFY_FAILED]`问题

使用requests访问https的时候提示`[SSL: CERTIFICATE_VERIFY_FAILED]`的错误，解决方法，传入`verify=False`参数：

```
res = requests.get(url, proxies=proxies, verify=False)
```

参考：

- [4 Ways to fix SSL: CERTIFICATE_VERIFY_FAILED in Python](https://www.howtouselinux.com/post/ssl-certificate_verify_failed-in-python)
- [Python Requests throwing SSLError](https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror)

# Response

## JSON 

```
res = requests.get(url, verify=False)

if res.status_code == 200:
    df = pd.DataFrame(res.json()['artifacts'])
```

## 参考

- [JSON Response Content](https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content)