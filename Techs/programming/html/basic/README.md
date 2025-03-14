## HTML 基础

HTML使用不同的标签来定义组成HTML网页的各种元素，这些元素同时拥有多种属性来丰富它的展示形式，比如：

- 用标签<a>定义的超链接里面就需要使用`href`属性来指定链接的URL。
- 用标签<img>定义的图片需要使用`src`属性来指定图片的地址，同时也需要`width`和`height`来指定图片的宽度和高度（单位均为像素），`alt`来指定备用文字。
- `style`属性用来表示元素的样式，比如颜色、字体、大小等。比如` <p style="color:red">This is a red paragraph.</p> `。
- `lang`属性用来定义语言，通常声明在<html>标签里，比如`<html lang="en-US">`。
- `title`属性在段落中使用，当你把鼠标移动到该段落时会现实它，比如`<p title="I'm a tooltip">`。
- `id`属性用来为某个元素指定唯一的标记。

可以使用`<!-- Write your comments here -->`来添加注释，支持多行注释。

## HTML 网页结构

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


## 标题

使用标签<h1>~<h6>来定义标题。标题是重要的因为搜索引擎使用标题来索引网页的结构和内容。不要对正文中的文本使用标题的标签。

标题都有默认的大小，但可以通过`style`属性，结合CSS的`font-size`属性来重新设定它们的大小，比如：

```
<h1 style="font-size:60px;">Heading 1</h1>
```

## body

当设定了body为固定的size的时候，可以使用`body{ margin:0 auto; }`来将它居中显示。

参考：

- [How to align entire html body to the center?](https://stackoverflow.com/questions/6464592/how-to-align-entire-html-body-to-the-center/29166036)

## 段落

使用标签<p>来定义段落。

## 链接

使用标签<a>来定义，比如` <a href="https://www.w3schools.com">This is a link</a> `定义了一个链接。链接并不限于文本，而是对包括图片等所有的HTML元素都有效。

`href`属性用来指定地址，地址可以指向本页面的内容，也可以指向其他页面。`target`属性指定在哪里打开新的页面，有如下几种值：

- `_blank`：在新的窗口或标签页打开新的页面
- `_self`：在当前窗口/标签打开新的页面（默认值）
- `_parent`：在父边框打开（没理解）
- `_top`：在整个窗口打开新的页面

链接在访问前后以及是否处于激活状态都可以显示不同的颜色，默认访问前为“蓝色带下划线”，访问后为“紫色带下划线”，处于激活状态的默认为“红色带下划线”。可以使用CSS来改变默认的配置，如下：

```
<style>
a:link {
  color: green;
  background-color: transparent;
  text-decoration: none;
}

a:visited {
  color: pink;
  background-color: transparent;
  text-decoration: none;
}

a:hover {
  color: red;
  background-color: transparent;
  text-decoration: underline;
}

a:active {
  color: yellow;
  background-color: transparent;
  text-decoration: underline;
}
</style>
```


## 图片

使用<img>来定义，同时需要用`src`, `alt`, `width`, `height`等关键字来定义属性：

```
<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
```

当然，也可以直接使用CSS的style特性来进行修饰，这是推荐的用法，因为上面的这种方式可能被网页里面定义的CSS样式表覆写，从而导致使用`width`和`height`关键字定义的属性失效。

```
<img src="img_girl.jpg" alt="Girl in a jacket" style="width:500px;height:600px;">
```

## 按钮

使用<button>来定义。

## 列表

使用<ul>和<ol>来定义，前者定义无序列表，后者定义有序列表。
