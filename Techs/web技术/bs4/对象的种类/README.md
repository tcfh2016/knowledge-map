## 对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment。

## BeautifulSoup

BeautifulSoup对象即代表所读取的整个文档。

```
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
```


## Tag

Tag对象与XML或HTML原生文档中的tag相同，它有很多方法和属性，常见的是`name`和`attributes`，一个Tag对象只有唯一的名字，但可能有多个属性，属性的操作方法与字典相同。

```
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
t = soup.b
t.name     # 对象的name = 'b'
t['class'] # 对象的attribute class, 值为'boldest'
t.attrs    # 对象的所有attribute
```

1）`Name`

每个Tag都有自己的名字，通过`tag.name`来获取。


2）`Attributes`

一个Tag可以有多个属性，它的操作方法与字典相同：

```
tag['class']
# u'boldest'

tag.attrs
# {u'class': u'boldest'}
```

3）`.contents`

tag的.contents属性可以将该tag的子节点以列表的形式输出。


## Attributes

即对应标签的属性，或许属性的方法和字典相同，比如要获取tag中的class属性通过`tag['class']`，如果要获取所有属性，那么通过点来取`tag.attrs`。

比如下面是获取的一个`td`tag的内容，我想要取出其中的`href`属性那么就可以通过`t.a['href']`，这个过程有两步：首先是通过点号定位到tag：`a`，然后通过字典的方式取出其中的`href`属性。

```
<td data="4">
	<a class="build-status-link" href="38361/console">
		<span class="build-status-icon__wrapper icon-blue">
			<span class="build-status-icon__outer">
				<svg class="svg-icon" viewbox="0 0 24 24"><use href="/static/dc9cb1a9/images/build-status/build-status-sprite.svg#build-status-static"></use></svg>
			</span>
			<svg class="svg-icon icon-blue icon-sm" viewbox="0 0 24 24"><use href="/static/dc9cb1a9/images/build-status/build-status-sprite.svg#last-successful"></use></svg>
		</span>
	</a>
</td>
```


## NavigableString

字符串通常被包含在tag内，BS用NavigableString来包装字符串。

```
t.string       # u'Extremely bold'
type(t.string) # <class 'bs4.element.NavigableString'>
```

## Comment

Comment 对象是一个特殊类型的 NavigableString 对象，用来表示文档的注释部分：

```
c = soup.b.string
```
