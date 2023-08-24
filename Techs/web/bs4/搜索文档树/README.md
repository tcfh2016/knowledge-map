## [搜索文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id27)

Beautiful Soup定义了搜索文档树的方法，常用的是`find()`和`find_all()`，两者具有相同的参数：

```
find_all( name , attrs , recursive , string , **kwargs )
find( name , attrs , recursive , string , **kwargs )
```

区别在于，`find()`只会返回第一个匹配的记录，而`find_all()`相当于找到所有匹配的内容，因此`soup.find('title')`相当于`soup.find_all('title', limit=1)`。


通过点取属性的方式只能获得当前名字的第一个tag:要得到所有的<a>标签,或是通过名字得到比一个tag更多的内容的时候,就需要用到 Searching the tree 中描述的方法,比如: find_all()。find_all()搜索所有tag及其子节点并判断是否符合过滤器的条件，过滤器就是传入`find_all()`的参数。


*find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None。*


## 认识过滤器

使用搜索功能时需要先认识过滤器，“过滤器”是一种比较抽象的叫法，其实就相当于“过滤条件”。在搜索的时候我们可以将特定的过滤条件应用在“tag名称”、“节点的属性”、以及单纯的“字符串”上，换句话说，我们可以按照“tag名称”、“节点的属性”、或者单纯的“字符串”来进行搜索。

举几个例子：

1） 字符串搜索（`name`）

即传入字符串参数，比如`soup.find_all('b')`会查找所有的`<b>`标签。

2） 节点的属性搜索（`attrs`）

`data_soup.find_all(attrs={"data-foo": "value"})`会查找属性为"data-foo"值为"value"的所有节点。

3）方法

定义判断条件是否匹配的方法。


## `name`搜索

搜索时的默认参数是`name`，你可以直接传字符串开始搜索，此时仅进行完全匹配，你可以传入一个列表来进行多项匹配：

```
soup.find_all('b') # 查找所有的<b>标签：[<b>The Dormouse's story</b>]
soup.find_all(["a", "b"]) # 查找所有的<a><b>标签
soup.find_all(re.compile("^b")) #会找到所有以'b'开头的标签，那么`<body>`和`<b>`都会被找到。
```

调用`find_all`返回的类型是`'bs4.element.Tag'`。

使用时还可以使用[`limit`参数](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#limit)，用来控制返回结果的数量，比如`soup.find_all("a", limit=2)`。


## 属性搜索

*比如我想找到<h1 class="build-caption page-headline">...</h1>这个元素，可以使用:

```
soup.find_all(attrs={"class":"build-caption page-headline"}
```

或者使用：

```
soup.find_all(class_ = "build-caption page-headline"))
```

为什么上面在按照`class`搜索的时候需要使用到`class_`关键字呢？因为在Beautiful Soup支持[按CSS搜索tag](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#css)的功能，但因为`class`关键字是Python的保留字，如果使用这个搜索会有语法错误。



## string参数

指定搜索的字符串，比如使用`bs.find(string=re.compile('ZUUL_CHANGE'))`搜索第一个包含`ZUUL_CHANGE`的内容，返回的内容是`NavigableString`的类型。

如果想在Beautiful Soup之外使用 NavigableString 对象,需要调用 unicode() 方法,将该对象转换成普通的Unicode字符串,否则就算Beautiful Soup已方法已经执行结束,该对象的输出也会带有对象的引用地址，会浪费内存。

*注：在使用`unicode()`的时候碰到了`NameError: name 'unicode' is not defined`的错误，这是因为在python 3.8.2之后unicode()已经不再支持，直接使用`str()`就行了。*

下面的内容使用`bs.find_all(string=re.compile(".*\"https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/UPLANE/job/L2-LO/job/SCT.fuse.asib_abio/.*"))`来查找还找不到，但使用`bs.find_all(string=re.compile(".*https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/UPLANE/job/L2-LO/job/SCT.fuse.asib_abio/.*"))`就能够查找到内容，为什么呢？

```
 <span id="output" class="style-scope gr-linked-text"><a href="https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/UPLANE/job/L2-LO/job/SCT.fuse.asib_abio/37424/" target="_blank" rel="noopener" class="style-scope gr-linked-text">https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/UPLANE/job/L2-LO/job/SCT.fuse.asib_abio/37424/</a> : CANCELLED</span>
```

原因应该在于bs里面的搜索并不仅仅是包括tag的纯文本，而是除开tag之外的纯文本，所以我们可以使用`bs.find_all("a", string=re.compile(".*https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/UPLANE/job/L2-LO/job/SCT.fuse.asib_abio/.*"))`来达到目的。

参考：

- [Error NameError: name 'unicode' is not defined in Python](https://quizdeveloper.com/faq/error-nameerror-name-unicode-is-not-defined-in-python-aid2312)


## 父节点和先辈节点们

在[find_parents() 和 find_parent()](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#find-parents-find-parent)里面提到：`find_parent()`是查找当前节点的父节点，而`find_parents()`是一层一层往上查找。


## [兄弟节点](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#find-parents-find-parent)

