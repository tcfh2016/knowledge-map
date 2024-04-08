## 下载分页的网页

[这篇文章](https://www.zenrows.com/blog/requests-pagination#next-page-link)讲得很清楚。其中使用了两种方法：

1. 从第一页找到下一页的链接，并递归获取；
2. 如果不同的页面对应不同的URL，那么通过`requests`访问不同的URL来完成。


## AJAX请求

一种更难的问题是上面两种方法都不可行，比如我想获取[中证指数列表](https://www.csindex.com.cn/#/indices/family/list)的数据表，发现不同页面的数据通过上面两种方式都获取不了，因为找不到不同页面的URL。

这是因为网页使用了JavaScript分页技术，你可以通过点击不同按钮来浏览不同的页面，同时网页的URL并不改变。这种比较复杂的网页推荐通过使用`selenium`来抓取：

> Scraping dynamic pagination with Python's Requests library is possible but requires advanced techniques, like intercepting the XHR requests. However, using a headless browser for advanced cases is better, especially if you're familiar with Selenium web scraping.

当然，一种方法是打开浏览器开发者模式，从"Network"->"Fetch/XHR"去查看点击按钮/滑动鼠标时候触发的AJAX请求，从请求头里面找到对应的URL。

有时候这种方式还是不行，因为比如有些请求的URL并没有规律，比如下面这两次请求：

```
https://www.csindex.com.cn/csindex-home/index-list/query-index-item?type__1773=GqUxuDgD07%3DWqGNPeeqh4m2OD9G5W3DnQroD

https://www.csindex.com.cn/csindex-home/index-list/query-index-item?type__1773=eqUxuDgiDQD%3Dd0KDsdOODmxWwx%2Bo8q8aq4D
```