# HTML 样式

## `style`属性

用来给元素设置颜色、字体、大小等特征的。给一个HTML元素设定样式，可以使用`<tagname style="property:value;">`这种形式来完成。

这里面的`style`是HTML标签的属性，而`property`则是CSS的属性，`value`也是CSS的值。比如：

- CSS的`background-color`属性定义了HTML元素的背景色。比如`<body style="background-color:powderblue;">`。
- CSS的`color`属性定义了HTML元素的文本颜色。比如`<p style="color:red;">This is a paragraph.</p>`。
- CSS的`font-family`属性指定HTML元素的字体。比如`<p style="font-family:courier;">This is a paragraph.</p>`
- CSS的`font-size`属性设定了HTML元素的字体大小。比如`<h1 style="font-size:300%;">This is a heading</h1>`
- CSS的`text-align`属性设置了HTML元素在水平方向的对齐方式。比如`<p style="text-align:center;">Centered paragraph.</p>`。
- CSS的`border`可以设置边框，比如`<h1 style="border:2px solid Tomato;">Hello World</h1>`。
- CSS的`padding`定义了文本与边框间的空白。
- CSS的`margin`定义了边框外的空白。


## 文本格式化

HTML里面定义了专门的标签来对文本进行格式化，有下面几种：

- <b>：粗体
- <strong>：显示方式和粗体一样，但语义上有些区别。
- <i>：斜体
- <em>：强调文本，样式类似斜体
- <mark>：标记文本，会显示为黄色背景
- <small>：小号文字
- <del>：删除文字
- <ins>：插入文字
- <sub>：下标文字
- <sup>：上标文字

参考：

- [HTML 元素 <b> 和 <strong> 有什么区别？](https://www.zhihu.com/question/20961933)

## 引用元素

HTML引用元素包括`<q>`,`<blockquote>`,`<abbr>`,`<address>`,`<cite>`和`<bdo>`定义的元素。

- <q>定义短引用，通常显示在双引号内。
- <blockquote>定义块引用，里面的内容会进行缩进显示。
- <abbr>定义缩写。
- <address>定义地址信息，通常显示为斜体，并且在其前后插入分割线。
- <cite>定义著作的标题，通常显示为斜体。
- <bdo>双向复写，内容中的字母会从右至左显示。



## CSS

CSS全称为“Cascading Style Sheets，层叠样式表”，它可以给多个网页进行统一布局，因此可以省去很多重复性的工作。

CSS有三种使用方式：

- 使用style属性内嵌到HTML元素中。
- 在<head>部分使用<style>元素。*注：<style>元素和元素里面的style属性是不一样的。*
- 使用外部的CSS文件。

详见[CSS](./css/README.md)
