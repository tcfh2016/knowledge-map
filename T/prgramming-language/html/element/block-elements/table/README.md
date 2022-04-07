## [Tables](https://www.w3schools.com/html/html_tables.asp)

Table(表格)是以行和列来组织并展示数据，html里面的表格包含了不同行列之间的数据单元，

- `td`定义数据单元，如果要某些数据单元作为标题行那么使用`th`
- `tr`定义行
- `table`定义整张表格

## Table Borders

表格可以具有不同样式和形状的边框，当为表格设置了边框，那么同时也为每个单元格设置了边框，此时每个单元格会有双边框，可以通过设置`border-collapse`样式来将其变成单边框：

```
table, th, td {
  border: 1px solid black;
  border-collapse: collapse; # 设置collapse将双边框更改为单边框
}
```

*注：在table里面table，th, td都是分开指定样式的。如果仅仅针对table设置那么只会显示外框。*


## Table Sizes

可以使用`style`属性设置`width`, `height`来指定行、列以及整个表格的大小。比如下面设置表格宽度的百分比是以它的父元素（一般是body），然后可以为特定的列设置宽度，可以百分位，可以像素值。

```
<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
</table>  
```

## Table Headers

表头可以位于第一行，也可以位于第一列，只是写法不同。表头的默认样式为居中、加粗。比如表头位于第一行：

```
<table>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
</table>  
```

表头位于第一列的写法：

```
<table>
  <tr>
    <th>Firstname</th>
    <td>Jill</td>
    <td>Eve</td>
  </tr>
  <tr>
    <th>Lastname</th>
    <td>Smith</td>
    <td>Jackson</td>
  </tr>
</table>
```

## Table Caption

给表格指定标题。

## Tab Padding&Spacing

单元格的padding表示的是单元格内容与单元格边框之间的空间（默认值为0），而spacing表示的是单元格与单元格之间的空间，默认为2像素。

```
th, td {
  padding: 15px; //四周的边
  padding-top: 10px;
  padding-bottom: 20px;
  padding-left: 30px;
  padding-right: 40px;

  border-spacing: 30px;
}
```


## Table Styling

可以指定表格、文本大小和对齐方式。

```
tr:nth-child(even) {
  background-color: #D6EEEE;  //设置行斑马条纹
}

td:nth-child(even), th:nth-child(even) {
  background-color: #D6EEEE; // 设置列斑马条纹
}

width: 1200px;
text-align:right;
font-size: 12px;
```
