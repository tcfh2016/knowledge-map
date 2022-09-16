## [搜索文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id27)

通过点取属性的方式只能获得当前名字的第一个tag:要得到所有的<a>标签,或是通过名字得到比一个tag更多的内容的时候,就需要用到 Searching the tree 中描述的方法,比如: find_all()。find_all()搜索所有tag及其子节点并判断是否符合过滤器的条件。

过滤器就是传入`find_all()`的参数，有以下几种类型：

- 字符串：即传入字符串参数，比如`find_all('b')`就是查找所有的`<b>`标签。
- 正则表达式：比如`find_all(re.compile("^b"))`会找到所有以'b'开头的标签，那么`<body>`和`<b>`都会被找到。
- 列表：比如`find_all(['a', 'b'])`会找到所有`<a>`和`<b>`标签。
- 方法


## 字符串搜索

字符串搜索仅进行完全匹配，你可以传入一个列表来进行多项匹配：

```
soup.find_all('b') # 查找所有的<b>标签：[<b>The Dormouse's story</b>]
soup.find_all(["a", "b"]) # 查找所有的<a><b>标签
```

调用`find_all`返回的类型是`'bs4.element.Tag'`。如果要获取


## 正则表达式搜索

正则表达式作为参数则按照正则的`match()`来匹配，下面的代码搜索所有以`b`开头的标签，即会找到`<body>`和`<b>`:

```
for tag in soup.find_all(re.compile("^b")):
  print(tag.name)
```

## find_all

find_all()的定义如下：

```
find_all( name , attrs , recursive , string , **kwargs )
```

在使用`find_all()`的过程中如果传入单纯的过滤器，比如名字，那么搜索的结果可能包含有过多的内容，此时可以通过其他参数来缩小搜索范围。比如，通过参数定义一个字典参数来搜索包含特殊属性的tag:

```
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]
```

*比如我想找到<h1 class="build-caption page-headline">...</h1>这个元素，可以使用soup.find_all(attrs={"class":"build-caption page-headline"}，或者使用soup.find_all(class_ = "build-caption page-headline"))*

使用时还可以使用[`limit`参数](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#limit)，用来控制返回结果的数量，比如`soup.find_all("a", limit=2)`。


## string参数

指定搜索的字符串，比如使用`bs.rind(string=re.compile('ZUUL_CHANGE'))`搜索第一个包含`ZUUL_CHANGE`的内容，返回的内容是`NavigableString`的类型。

如果想在Beautiful Soup之外使用 NavigableString 对象,需要调用 unicode() 方法,将该对象转换成普通的Unicode字符串,否则就算Beautiful Soup已方法已经执行结束,该对象的输出也会带有对象的引用地址.这样会浪费内存。

在使用`unicode()`的时候碰到了`NameError: name 'unicode' is not defined`的错误，这是因为在python 3.8.2之后unicode()已经不再支持，直接使用`str()`就行了。

参考：

- [Error NameError: name 'unicode' is not defined in Python](https://quizdeveloper.com/faq/error-nameerror-name-unicode-is-not-defined-in-python-aid2312)
