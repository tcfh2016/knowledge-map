## head

`<head>`是放置于`<html>`和`<body>`之间的metadata容器，可以囊括`<title>`, `<style>`, `<meta>`, `<link>`, `<script>`和`base`这些元素。

什么是“metadata”呢？就是所谓的元数据，用来描述HTML文档本身，它们并不像其他元素会被展示在页面上，这些元素据包括HTML文档的标题、字符集、脚本和其他数据。

## 内容元素

1）`<title>`

定义文档的标题，必须是文本，展示在浏览器的标题栏。它是必须要指定的，并且也会显示在搜索引擎的结果页里面。

2）`<style>`

为单个网页定义样式信息。

3）`<link>`

定义外部资源的链接，比如CSS：`<link rel="stylesheet" href="mystyle.css">`。

4）`<meta>`

指定字符集、页面描述、关键词、文档作者、以及viewport设置。这些信息不会被显示出来，但会被浏览器和搜索引擎使用。

5）`<viewport>`

设定用户的可视区域，告诉浏览器如何控制页面的尺寸和缩放比例。比如`<meta name="viewport" content="width=device-width, initial-scale=1.0">`里面的`width=device-width`只是显示的内容根据浏览设备进行调整，`initial-scale`设定缩放比例为1在第一次载入的时候。

6）`<script>`

自定义JavaScript脚本。

7）`<base>`

给整个网页指定一个URL或者target的base，也就是其他地方的链接可以基于base URL进行拼接，以及使用base指定的默认target打开方式。


## 常见问题

1）`<head>`和`<header>`之间的区别是什么？

`<head>`元素用来给网页文档提供metadata，描述网页标题、脚本定义和链接以及样式表。而`<header>`是HTML5才引入的新元素，用来包括多个描述性的元素，比如标题、logo等，常用在`<body>`里面开头的导航部分，可以替代一些场景下的`<div>`元素。

参考：

- [What is the Difference Between Head and Header?](https://www.daniweb.com/digital-media/ui-ux-design/threads/521782/what-is-the-difference-between-head-and-header)
- [What is the real difference between the “head” and “header” tag? ](https://stackoverflow.com/questions/33919706/what-is-the-real-difference-between-the-head-and-header-tag)
- [<header> vs. <head>](https://stackoverflow.com/questions/3434950/header-vs-head)
