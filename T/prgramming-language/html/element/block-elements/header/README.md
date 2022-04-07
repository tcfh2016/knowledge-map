## header

`<header>`元素是HTML5里面引入，使用在`<body>`开头用来定义一些介绍性的内容，通常包括：

- 一个或多个heading元素
- Logo/icon
- 作者

在一个文档里面可以有多个header元素，但header元素不能被放在footer, address或其他的header里面。浏览器大多将header元素展示为块状：

```
<article>
  <header>
    <h1>A heading here</h1>
    <p>Posted by John Doe</p>
    <p>Some additional information here</p>
  </header>
  <p>Lorem Ipsum dolor set amet....</p>
</article>
```

默认展示效果：

```
header {
  display: block;
}
```
