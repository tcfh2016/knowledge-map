# Beautiful Soup 4

Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库,它能够通过你喜欢的转换器
实现惯用的文档导航、查找、修改文档的方式。BS支出如下四种解析器：

- Python标准库：`BeautifulSoup(markup, "html.parser")`
- lxml HTML 解析器：`BeautifulSoup(markup, "lxml")`
- lxml XML 解析器：`BeautifulSoup(markup, ["lxml-xml"])`/`BeautifulSoup(markup, "xml")`
- html5lib：`BeautifulSoup(markup, "html5lib")`

## 使用方法

将一段文档传给 BeautifulSoup 的构造方法，便得到了一个文档对象，可以传入字符串或者文件句
柄。文档会首先被转换成Unicode再选择合适的解析器进行解释。

```
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup("<html>data</html>")
```

## 对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可
以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment。

### BeautifulSoup

BeautifulSoup对象即代表所读取的整个文档。

```
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
```

### Tag

Tag对象与XML或HTML原生文档中的tag相同，它有很多方法和属性，常见的是`name`和`attributes`，
一个Tag对象只有唯一的名字，但可能有多个属性，属性的操作方法与字典相同。

```
t = soup.b
t.name     # 对象的name = 'b'
t['class'] # 对象的attribute class, 值为'boldest'
t.attrs    # 对象的所有attribute
```

### NavigableString

字符串通常被包含在tag内，BS用NavigableString来包装字符串。

```
t.string       # u'Extremely bold'
type(t.string) # <class 'bs4.element.NavigableString'>
```

### Comment

Comment 对象是一个特殊类型的 NavigableString 对象，用来表示文档的注释部分：

```
c = soup.b.string
```

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

### 通过tag名字来访问

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

### .text() / .sring()

通过.string()来访问tag中的字符串。

## 搜索文档树

通过点取属性的方式只能获得当前名字的第一个tag:要得到所有的<a>标签,或是通过名字得到比一个
tag更多的内容的时候,就需要用到 Searching the tree 中描述的方法,比如: find_all()。

find_all()搜索所有tag及其子节点并判断是否符合过滤器的条件。

### 字符串搜索

字符串搜索仅进行完全匹配，你可以传入一个列表来进行多项匹配：

```
soup.find_all('b') # 查找所有的<b>标签：[<b>The Dormouse's story</b>]
soup.find_all(["a", "b"]) # 查找所有的<a><b>标签
```

### 正则表达式搜索

正则表达式作为参数则按照正则的`match()`来匹配，下面的代码搜索所有以`b`开头的标签，即会
找到`<body>`和`<b>`:

```
for tag in soup.find_all(re.compile("^b")):
  print(tag.name)
```

## 参考

- [Beautiful Soup 4.4.0 文档](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)
