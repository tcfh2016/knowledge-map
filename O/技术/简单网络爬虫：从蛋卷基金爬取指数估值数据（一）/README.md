## 简单网络爬虫：从蛋卷基金爬取指数估值数据（一）

> 简单网络爬虫的学习笔记主要叙述三部分内容：1）学习如何从蛋卷基金爬取估值数据；2）将爬取的数据保存为本地可以查看的csv格式的数据；3）将本地的csv数据部署为定时邮件任务，每天自动发送。

先说下需求。

有一天我在逛蛋卷基金的时候看到了上面的“指数估值模块”，链接在这里：https://danjuanfunds.com/djmodule/value-center?channel=1300100141。打开对应的网页是下面这样：


我的想法很简单，就是把上面的这张数据表下载到本地，保存为方便查看的格式（比如csv），然后最好能够做成自动邮件发送的形式让我每天都可以收到估值邮件。

## 抓取，by调用`requests.get()`

先进行第一步：数据获取。首先，从网络上了解到用来爬取网页内容的常用工具是Python语言李的`requests`模块。于是就边学边用，爬取某个网页非常方便，只需要调用`requests.get()`方法，然后传入对应的URL即可。

```
r = requests.get('https://danjuanfunds.com/djmodule/value-center?channel=1300100141')
print(r.status_code ) # 403
```

让我感到奇怪的是，上面的调用返回的结果是一个错误码：403，这个错误码在[HTTP 状态码](https://www.runoob.com/http/http-status-codes.html)描述，它的意思是“Forbidden：服务器理解请求客户端的请求，但是拒绝执行此请求”。

这有点出人意料，本想搞个大计划，怎么第一步都没有迈出去。明明我手动在浏览器里面键入该URL可以访问但使用`requests.get()`却被拒绝呢？在按照该错误在网络上搜索一阵之后弄明白了，这是因为对方的服务器会对接收到的请求进行一些区分处理，对于那些能够很明白识别出的是爬虫或者一些软件程序发送的请求服务器会拒绝应答该请求。毕竟网站都是更喜欢真实人的访问，而非机器的访问来占用服务器的资源。

解决方案也简单，

```
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'host': 'danjuanfunds.com',
    'Referer': 'https://danjuanfunds.com/djmodule/value-center?channel=1300100141',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW 64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'
    }

    response = requests.get('https://danjuanfunds.com/djapi/index_eva/dj', headers=headers)
```

## 理解`requests.get()`的返回结果



参考：

- [Requests: 让 HTTP 服务人类](https://docs.python-requests.org/zh_CN/latest/)
- [HTTP 状态码](https://www.runoob.com/http/http-status-codes.html)
- [Python Requests.get访问网页403错误](https://zhuanlan.zhihu.com/p/35853860)
- [定制请求头](https://docs.python-requests.org/zh_CN/latest/user/quickstart.html#id6)
