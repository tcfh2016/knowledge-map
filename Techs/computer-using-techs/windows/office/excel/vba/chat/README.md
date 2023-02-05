## ChartObject

ChartObject 对象充当 Chart 对象的容器。 ChartObject 对象的属性和方法控制工作表上嵌入图表的外观和大小。

ChartObject 对象是 ChartObjects 集合的成员。 ChartObjects 集合包含单一工作表上的所有嵌入图表。

`ChartObject.Chart`返回一个`Chart`对象，该对象代表对象中包含的图表，为只读属性。


## Chart.SeriesCollection 方法

返回一个对象，该对象 (Series 对象) 或图表组中 SeriesCollection (集合) 的所有系列的集合。Series 对象是 SeriesCollection 集合的成员。表示图表上的系列。
 
SeriesCollection(1) 是第一个添加到图表中的系列，而 SeriesCollection(SeriesCollection.Count) 是后一个添加到图表中的系列。


## Series

创建第一个参数为名称，第二个参数为x轴数据，第三个参数为y轴数据。

```
SERIES(ChinaMicro!$T$3,MicroChart!$A$4:$A$86,ChinaMicro!$T$4:$T$63,1)
```

Series有多个属性：

- Series.Name 名称
- Series.XValues x值，XValues 属性可以设置为工作表上的区域或值数组。
- Series.Values y值


```
Series.XValues = Worksheets(SheetName).Range(Worksheets(SheetName).Cells(EndDateCell.Row, 1), Worksheets(SheetName).Cells(StartDateCell.Row, 1))
                
' 重设y值
Series.Values = Sheets(SheetName).Range(Sheets(SheetName).Cells(EndDateCell.Row, SeriesNameCell.Column), Sheets(SheetName).Cells(StartDateCell.Row, SeriesNameCell.Column))
```




## 参考

- [ChartObject 对象](https://learn.microsoft.com/zh-cn/office/vba/api/excel.chartobject)
- [Chart.SeriesCollection 方法](https://learn.microsoft.com/zh-cn/office/vba/api/excel.chart.seriescollection)
- [Series.XValues 属性 (Excel)](https://learn.microsoft.com/zh-cn/office/vba/api/excel.series.xvalues)