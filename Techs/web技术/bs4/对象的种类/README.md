## 对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment。

## BeautifulSoup

BeautifulSoup对象即代表所读取的整个文档。

```
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
```


## Tag

Tag对象与XML或HTML原生文档中的tag相同，它有很多方法和属性，常见的是`name`和`attributes`，一个Tag对象只有唯一的名字，但可能有多个属性，属性的操作方法与字典相同。

比如我获取了下一面一个tag，命名为d：

```
<div class="total-stats style-scope gr-file-list">
	<span aria-label="264 lines added" class="added style-scope gr-file-list" tabindex="0">  +264 </span>
	<span aria-label="57 lines removed" class="removed style-scope gr-file-list" tabindex="0">  -57 </span>
</div>
```

那么`d.name`为：

```
div
```

那么`d.attrs`为：

```
{'class': ['total-stats', 'style-scope', 'gr-file-list']}
```

*注：HTML 4定义了一系列可以包含多个值的属性，在Beautiful Soup中多值属性的返回类型是list。*


那么`d['class']`为：

```
['total-stats', 'style-scope', 'gr-file-list']
```

那么`d.contents`（tag的.contents属性可以将该tag的子节点以列表的形式输出）为：

```
['\n', <span aria-label="264 lines added" class="added style-scope gr-file-list" tabindex="0"> +264 </span>, '\n', <span aria-label="57 lines removed" class="removed style-scope gr-file-list" tabindex="0"> -57 </span>, '\n']
```



## tag下的tag

上面的举例里面我们可以看到在`<div>`下面还有两个`<span>`，那么我如何取得下面的`<span>`呢？

直接通过“点取属性”就可以了，比如：

```
d.span  # 点取属性，获取<div>下面的<span>
```

但点取属性有个缺点，那就是只能获取第一个span。这个时候怎么办？

1) 可以使用`find_all()`来搜索。

```
d.find_all("span")
```

2）可以使用`children`方法。

```
for child in d.children:
	print(child)
```



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
