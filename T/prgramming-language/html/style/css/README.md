# CSS

CSS全称为“Cascading Style Sheets，层叠样式表”，它可以给多个网页进行统一布局，因此可以省去很多重复性的工作。

CSS有三种使用方式：

- 使用style属性内嵌到HTML元素中。
- 在<head>部分使用<style>元素。*注：<style>元素和元素里面的style属性是不一样的。*
- 使用外部的CSS文件。

## 内嵌的CSS

内嵌的CSS用来给单个HTML元素应用某种样式，比如：

```
<h1 style="color:blue;">This is a Blue Heading</h1>
```

## 内部的CSS

内部的CSS用来给单个HTML网页应用某种样式，比如：

```
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {background-color: powderblue;}
      h1   {color: blue;}
      p    {color: red;}
    </style>
  </head>

  <body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

## 外部的CSS

外部的CSS是用来给多个HTML网页定义样式的，所以你通常能够通过修改一个文件（CSS）来改变整个网站的样式。

使用外部CSS文件时你需要在<head>区域添加CSS文件的链接，链接有两种：一、完整的URL地址；二、相对于当前页面的路径：

```
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="styles.css">
  </head>

  <body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

而CSS文件专门用来定义样式，且以.css后缀名结尾：

```
body {
  background-color: powderblue;
}
h1 {
  color: blue;
}
p {
  color: red;
}
```

## CSS的其他特征

### id：为不同元素定义特定样式时使用，用来标记元素。

id属性是用来给某个HTML元素指定唯一的标识，它通常是在CSS和Javascript中用来对特定的元素执行特定的操作。在CSS里面访问某个id使用`#`符号。

```
<p id="p01">I am different</p>
```

为该标识定义特定的样式：

```
#p01 {
  color: blue;
}
```

### class: 为特定类型的元素定义特定样式时使用，用来标记元素类型。

下面是一个简单的例子介绍它的用法：

```
<p class="error">I am different</p>

p.error {
  color: red;
}
```

实际使用中它是结合div/span来一起使用，这样就可以很方便地为多个元素进行样式定义。

```
<!DOCTYPE html>
<html>
<head>
<style>
.cities {
  background-color: black;
  color: white;
  margin: 20px;
  padding: 20px;
}
</style>
</head>
<body>

<div class="cities">
  <h2>London</h2>
  <p>London is the capital of England.</p>
</div>

<div class="cities">
  <h2>Paris</h2>
  <p>Paris is the capital of France.</p>
</div>

<div class="cities">
  <h2>Tokyo</h2>
  <p>Tokyo is the capital of Japan.</p>
</div>

</body>
</html>
```

一个HTML元素也可以拥有多个class名称，只需要将它们用空格分隔：

```
<h2 class="city main">London</h2>
```
