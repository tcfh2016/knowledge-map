## [requests](https://requests.readthedocs.io/en/latest/)

requests 是基于Python的第三方HTTP库，用来请求网络资源。


## 安装

如果提示“ModuleNotFoundError: No module named 'requests'”，那么执行`pip install requests`安装该模块即可。


## 使用

最简单的使用就是如`r = requests.get('https://api.github.com/events')`，不过这里的返回结果保存在一个requests对象里面，我们就是从这个对象里面获取想要的信息。

- 通过`r.text`我们可以获取该对象的文本形式。
- 通过`r.content`可以获取到该对象的二进制形式。
- 通过`r.json()`可以获取到该对象的json形式。
- 通过`r.status_code`获得返回的错误码，整形表示。


当我们获得了整个页面的内容之后，还需要进一步解析，而这些解析工作就可以使用其他的python库来完成，比如`Beautiful Soup`。

## `requests`和`selenium`的区别？

`requests`只是简单第从一个给定的地址获取整个网页的数据，但是现在的网页数据越来越多的使用javascript，这些脚本会跟随网页浏览者的行为而自动加载，这就使得单纯使用`requests`无法获取到期望的整个网页的数据。而`selenium`用来模仿浏览者行为的函数库，你能够使用它来浏览和操作网页，就如真人一样。也就是说，使用`selenium`能够获取到的数据会比`requests`更全。

使用的时候，如果你能够直接从单个地址获取到整个网页的数据，那么毫无疑问使用`requests`就够了，如果不能那么就使用`selenium`。

参考：

- [Requests vs selenium](https://www.reddit.com/r/learnpython/comments/fa5ms5/requests_vs_selenium/)
- [请问下 python 中，selenium 请求网页和 request\.get 获取网页的区别？](https://youle.zhipin.com/questions/22a8917e926db5bbtnZ63NS7E1A~.html)
