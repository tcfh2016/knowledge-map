## 搜索文档树

通过点取属性的方式只能获得当前名字的第一个tag:要得到所有的<a>标签,或是通过名字得到比一个tag更多的内容的时候,就需要用到 Searching the tree 中描述的方法,比如: find_all()。find_all()搜索所有tag及其子节点并判断是否符合过滤器的条件。

过滤器就是传入`find_all()`的参数，有以下几种类型：

- 字符串：即传入字符串参数，比如`find_all('b')`就是查找所有的`<b>`标签。
- 正则表达式：比如`find_all(re.compile("^b"))`会找到所有以'b'开头的标签，那么`<body>`和`<b>`都会被找到。
- 列表：比如`find_all(['a', 'b'])`会找到所有`<a>`和`<b>`标签。
- 方法


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

### find_all

find_all()的定义如下：

```
find_all( name , attrs , recursive , string , **kwargs )
```

在使用`find_all()`的过程中如果传入单纯的过滤器，比如名字，那么搜索的结果可能包含有过多的内容，此时可以通过其他参数来缩小搜索范围。比如，通过参数定义一个字典参数来搜索包含特殊属性的tag:

```
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]
```
