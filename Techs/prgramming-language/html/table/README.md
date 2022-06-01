## table

HTML页面里面的表格是使用`<table>`标签来定义的，其中的每行使用`<tr>`标签，表格头使用`<th>`定义每个单元格，默认以加粗、居中显示。其他的各行的单元格使用`<td>`进行定义。

表格展示的时候默认没有边框，如果要使用边框那么需要使用CSS的`border`属性。

## 表格样式

表格的标题使用`caption`标签进行定义。

### 表格宽度

通过`<table style="width:100%">`指定展示百分比的相对宽度。

### 表格边框

表格默认以无边框的形式展现，如果要指定边框需要使用CSS属性：

```
table, th, td {
  border: 1px solid black;
}
```

然而单纯使用边框属性的时候看起来会很怪异，因为每个单元格看起来都被双线边框包围着，这个时候我们需要使用collapsed border，在上面的代码里加上`border-collapse: collapse;`。

### 单元格修饰

首先可以使用CSS的padding属性来设定单元格内容与边框之间的空白；其次可以使用text-align属性来对齐单元格内容；还可以使用border-spacing属性来设置单元格之间的空间。

```
th, td {
  padding: 15px;
  text-align: left;
  border-spacing: 15px;
}
```

### 跨行/跨列的单元格

当一个单元格需要跨越多个列时使用`colspan`，而需要跨越多行时使用`rowspan`:

```
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th colspan="2">Telephone</th>
  </tr>
  <tr>
    <th rowspan="2">Telephone:</th>
    <td>55577854</td>
  </tr>
  <tr>
    <td>55577855</td>
  </tr>
</table>
```

参考：

- [HTML Tables](https://www.w3schools.com/html/html_tables.asp)

## 常见问题

### 如何让表格在页面居中？

已知的`text-align: left;`都是让表格里面的文字如何在单元格里面对齐，但如何让表格在页面显示的时候居中呢？

```
margin-left: auto;
margin-right: auto;
```

参考：

- [Center-align a HTML table](https://stackoverflow.com/questions/14073188/center-align-a-html-table)


### 如何让其他元素，比如article在页面居中显示呢？

也可以像上面表格那样设置。

参考：

- [Centering an article tag](https://stackoverflow.com/questions/32042449/centering-an-article-tag/32042656)
