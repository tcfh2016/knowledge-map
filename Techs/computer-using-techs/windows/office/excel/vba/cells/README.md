## Worksheet.Cells

Worksheet.Cells返回一个range对象。

```
'将活动工作簿 Sheet1 中单元格 C5 的字号设定为 14 点。
Worksheets("Sheet1").Cells(5, 3).Font.Size = 14

'清除活动工作簿 Sheet1 上第一个单元格中的公式
Worksheets("Sheet1").Cells(1).ClearContents

'将 Sheet1 上每个单元格的字体和字号都设置为 8 个 Arial 点
With Worksheets("Sheet1").Cells.Font 
    .Name = "Arial" 
    .Size = 8 
End With
```

## 参考

- [Worksheet.Cells 属性](https://learn.microsoft.com/zh-cn/office/vba/api/excel.worksheet.cells)