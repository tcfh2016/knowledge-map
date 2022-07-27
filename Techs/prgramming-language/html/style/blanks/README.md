## 空格

在html页面展示空格，[Basic HTML: How do you create blank space in HTML?](https://crunchify.com/basic-html-how-do-you-create-blank-space-in-html/)里面给出了三种方法：

1）方法一：使用`&nbsp;`

`&nbsp;`是空格的编码。

2）方法二：使用`<pre>`元素

该元素会格式化文本，使用`<pre>`元素包含起来的文本会保持原有的格式。

3）方法三：使用style填充

```
<span style="padding-left:20px">test1    | test2  |   test3</span>
```


## 缩进

段落的缩进：

```
<p style="margin-left: 40px">
...
</p>
```
