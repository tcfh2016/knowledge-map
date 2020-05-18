# HTML 基础

HTML使用不同的标签来定义组成HTML网页的各种元素，这些元素同时拥有多种属性来丰富它的展示形式，比如：

- 用标签<a>定义的超链接里面就需要使用`href`属性来指定链接的URL。
- 用标签<img>定义的图片需要使用`src`属性来指定图片的地址，同时也需要`width`和`height`来指定图片的宽度和高度（单位均为像素），`alt`来指定备用文字。
- `style`属性用来表示元素的样式，比如颜色、字体、大小等。比如` <p style="color:red">This is a red paragraph.</p> `。
- `lang`属性用来定义语言，通常声明在<html>标签里，比如`<html lang="en-US">`。
- `title`属性在段落中使用，当你把鼠标移动到该段落时会现实它，比如`<p title="I'm a tooltip">`。
- `id`属性用来为某个元素指定唯一的标记。


## 标题

使用标签<h1>~<h6>来定义标题。标题是重要的因为搜索引擎使用标题来索引网页的结构和内容。不要对正文中的文本使用标题的标签。

标题都有默认的大小，但可以通过`style`属性，结合CSS的`font-size`属性来重新设定它们的大小，比如：

```
<h1 style="font-size:60px;">Heading 1</h1>
```

## 段落

使用标签<p>来定义段落。

## 链接

使用标签<a>来定义，比如` <a href="https://www.w3schools.com">This is a link</a> `定义了一个链接。

## 图片

使用<img>来定义，同时需要用`src`, `alt`, `width`, `height`等关键字来定义属性：

```
 <img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
```

## 按钮

使用<button>来定义。

## 列表

使用<ul>和<ol>来定义，前者定义无序列表，后者定义有序列表。
