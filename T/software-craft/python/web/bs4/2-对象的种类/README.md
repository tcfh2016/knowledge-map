## 对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可
以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment。

### BeautifulSoup

BeautifulSoup对象即代表所读取的整个文档。

```
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
```


### Tag

Tag对象与XML或HTML原生文档中的tag相同，它有很多方法和属性，常见的是`name`和`attributes`，一个Tag对象只有唯一的名字，但可能有多个属性，属性的操作方法与字典相同。

```
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
t = soup.b
t.name     # 对象的name = 'b'
t['class'] # 对象的attribute class, 值为'boldest'
t.attrs    # 对象的所有attribute
```

*tag的.contents属性可以讲该tag的子节点以列表的形式输出。*

### Name

每个Tag都有自己的名字，通过`tag.name`来获取。


### Attributes

一个Tag可以有多个属性，它的操作方法与字典相同：

```
tag['class']
# u'boldest'

tag.attrs
# {u'class': u'boldest'}
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
