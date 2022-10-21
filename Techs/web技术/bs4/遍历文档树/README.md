## 遍历文档树

示例代码：

```
html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```


## 通过tag名字来访问

操作文档树最简单的方法是指定对应的tag名字：

```
soup.head  # 获取<head>标签
soup.title # 获取<title>标签
soup.body.b # 获取<body>下第一个<b>标签
```


### .contents 和 .children

.contents属性是将tag的子节点以列表的方式输出。

```
head_tag = soup.head # <head><title>The Dormouse's story</title></head>
head_tag.contents    #[<title>The Dormouse's story</title>]
title_tag = head_tag.contents[0] # <title>The Dormouse's story</title>
title_tag.contents # [u'The Dormouse's story']
```

.children 可以对tag的子节点进行循环：

```
for child in title_tag.children:
  print(child)
```


### .text() / .string()

通过.string()来访问tag中的字符串。

