## 书签 / 锚点

“书签”（或者“锚点”）用来让用户可以在页面的不同位置进行跳转，当一个网页很长的时候，无疑是方便的。创建它们有两种方法：`id属性`或`a元素`。

1）`id属性`

我们用元素的`id`属性来创建书签，然后为它添加链接：

```
<h2 id="C4">Chapter 4</h2>

<a href="#C4">Jump to Chapter 4</a>  <!-- 链接至本页的书签 -->
<a href="html_demo.html#C4">Jump to Chapter 4</a>  <!-- 链接至其他页面的书签 -->
```

*注：测试发现，这个ID只能够应用在header上。*

2）[`a元素`](https://www.w3schools.com/tags/tag_a.asp)

`a元素`是用来定义超链接的，它最重要的属性就是`href`，使用它就能够定义一个指向对应地址的超链接。当没有`href`属性的时候，它就摇身一变为超链接的占位符，也就是一个“锚点”。

可以为这个“锚点”指定一个名字，那么它就是一个“[命名锚点](https://www.tagindex.net/html/link/a_name.html)”，可以完成页面内的跳转：

```
<a href="#Anchorname">linked text</a>

(Target point)
<a name="Anchorname">a named anchor</a>
```

*注：即便命名锚点修饰的文本是空的，同样能够实现链接的跳转。*


220613：今天测试outlook的html邮件，发现两者有些差别，因为outlook可能不支持id属性，但是能支持命名锚点。
