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


## 样式

- 指定表格、文本大小和对齐方式

```
width: 1200px;
text-align:right;
font-size: 12px;
```

- 指定最外层边框

在table里面table，th, td都是分开指定样式的。如果仅仅针对table设置那么只会显示外框：

```
border-style: solid;
border-width: 1px;
```
