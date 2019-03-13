## ModuleNotFoundError: No module named 'pandas' 错误

使用 `pip3 install pandas`先安装。如果提示网络问题，比如：

```
 Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ConnectTimeoutError(<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x0000013C8C6942B0>, 'Connection to pypi.org timed out. (connect timeout=15)')': /simple/pandas/
```

就可以在安装时使用代理`pip3 --proxy 127.0.0.1:6152 install pandas`。

参考：

- [让 pip 走代理](https://www.logcg.com/archives/1914.html)
