# HTML

HTML，全称“Hyper Text Markup Language”，是用来制作网页的标准标记语言。HTML由一系列由特定标签组成的元素构成，这些元素组成了整个网页的结构，也决定了浏览器以何种形式来展示它。

## 基本语法

### tag / 标签

HTML标签用来定义组成网页的元素的名字，浏览器会根据这些标签来渲染展示它们的效果。标签的使用语法如下：

```
<标签名称>元素内容</标签名称>
```

### HTML 网页结构

一个最简单的HTML网页的结构如下：

```
<html>
  <head>
    <title>Page title</title>
  </head>
  <body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
    <p>This is another paragraph.</p>
  </body>
</html>
```

它由三部分组成：

- html元素，最基本的元素。
- head元素，包含html文件的元信息。除了已经提到的标题，还可以通过`<meta charset="UTF-8">`指定编码方式。
- body元素，包含可以展示的具体内容。

由于HTML更迭了好多版本，目前需要使用`<!DOCTYPE> `来声明文档的html类型，以便于网页能够正常的展示。比如使用`<!DOCTYPE html>`便是指定了网页支持html5。

## 其他知识点
