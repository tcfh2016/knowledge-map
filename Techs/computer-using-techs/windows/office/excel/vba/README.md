## VBA开发界面

在菜单栏邮件点击“自定义功能区”，从里面选择“开发工具”就可以调出开发工具的菜单，然后在“设计模式”下点击按钮就能够打开VB界面。


## VBA调试

在VB界面可以看到代码，为了方便调试可以在“视图”中选择“立即窗口”，我们可以使用Debug对象的`Print`方法来把字符串输出到立即窗口。打印字符串：

```
Dim MyVar
MyVar = "Come see me in the Immediate pane."
Debug.Print MyVar
```

打印变量：

```
SeriesNum = cto.Chart.SeriesCollection.Count
Debug.Print "count = " & SeriesNum

'打印多个变量
Debug.Print "Series.Name="; Series.Name; "located cell="; SeriesNameCell.Row; ","; SeriesNameCell.Column
```

## 编译错误：找不到工程或库

调试某个函数的时候总是提示“编译错误：找不到工程或库”，按照[Excel执行VBA提示“编译错误：找不到工程或库”](https://www.jianshu.com/p/a648408bf4dc)中的方法将“引用”去掉。


## 查找特定单元格

查找功能常用的是`find`函数，但这个函数是range对象才有的。

```
Set StartDateCell = ThisWorkbook.Sheets(SheetName).Columns("A:A").Find(What:=StartDate, LookAt:=xlWhole)

Set StartDateCell = Sheets(SheetName).Range("A1").EntireColumn.Find(StartDate, , , xlWhole)
If StartDateCell Is Nothing Then
    Debug.Print "Not in range."
Else
    Debug.Print "Found at row: " & StartDateCell.Row
End If
```

- [使用 Excel VBA 在列中查找值](https://www.delftstack.com/zh/howto/vba/find-for-a-string-in-a-column-on-vba/)
- [Range 对象 (Excel)](https://learn.microsoft.com/zh-cn/office/vba/api/excel.range(object))


## VBA注释

使用单引号`'`来注释。



参考：

- [VBA 注释教程和实例](https://www.lanrenexcel.com/vba-comment/#)
- [Debug 对象](https://learn.microsoft.com/zh-cn/office/vba/language/reference/user-interface-help/debug-object)
- [VBA Guide For Charts and Graphs](https://www.automateexcel.com/vba/charts-graphs/)