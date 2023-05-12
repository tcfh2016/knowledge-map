##

- MOD 经常出现的数


## 点线图坐标轴逆序

比如横坐标是从2022,2021...2010这样显示，怎么调整到2010,2011...2022这样？

图标右键选择“坐标轴格式”，勾选“逆序类别”。


## 设置单元格按“亿”显示

在邮件设置格式里面选择“自定义”，然后输入`0"."00,,亿`即可。

按万显示可以设置为 `0!.0,!0`。

参考：

- [Excel元、万元保留两位小数单位显示如何设置？](https://jingyan.baidu.com/article/9158e0009d6409e254122893.html)

## PivotTable

创建了透视表，但是删除了原来sheet里面的数据，透视表里面的不会自动更新，这个时候需要点击“data”里面的“refresh”按钮去主动刷新。

## 常见公式

- 保持公式不变

在拖曳去应用公式到多个单元格的时候，有些时候需要让一些单元格保持不动，这个时候在公式输入框中光标移动至对应单元格，然后使用快捷键F4（Windows）或者cmd + t（MAC），这样该单元格的格式会更新，比如`E12`会变更为`$E$12`。


## EXCEL 无法处理数据

左上角有绿色标签，那么选中对应单元格，然后点击弹出的标签-> "Convert to Number"
https://support.office.com/en-ie/article/fix-text-formatted-numbers-by-applying-a-number-format-6599c03a-954d-4d83-b78a-23af2c8845d0
没有绿色标签的转换，特别对于 From Text/CSV 的数据，则需要“Data" -> "Text to Columns" -> 选择”Delimited“ -> "Finish"

https://www.ablebits.com/office-addins-blog/2018/07/18/excel-convert-text-to-number/



## Excel公式保持某个变量不变

https://blog.csdn.net/zhezhebie/article/details/81332977
正常我们套用一个公式，例如C2=A2*B2，那么拖动公式时必然C3=A3*B3，如果我们希望A2这个值固定不变，只有B列在随着公式变化而变化，那就可以开始时把C2=A2*B2写成C2=$A$2*B2。


## Excel的列显示

2018年10月22日17:22:29
将列显示为ABCD

https://jingyan.baidu.com/article/a378c960d77615b3282830bd.html

【文件】 - 【公式】 - 【R1C1引用样式】

## Excel智能拷贝

2018年7月4日10:00:12
怎样进行智能拷贝：不拷贝隐藏部分的内容？

按ctrl + g 弹出【定位】对话框，在【定位条件】中选择“可见单元格”再进行复制拷贝。


## EXCEL的列号

2019年4月30日10点53分
在四万行应用某个公式：最常见的方法是拖，但太慢。另一种操作：

名称框（左上角）输入范围 D2：D44533
公式编辑框输入公式
再 CTRL + Enter 应用

2017年6月17日10:51:23
今天突然发现EXCEL的列号由之前的字母变为了数字，导致有些计算公式里面的应用不能及时理解，之后查询搜索，可以在【文件】-->【选项】-->【公式】里面将“R1C1引用样式”取消掉就可以恢复正常。


## EXCEL使用

2016年9月2日10:27:15
1. 数据分析的时候如果数据行太多，那么需要快速删除某些行，怎么操作？
使用ctrl + shift + 向下箭头，一下就可以选中到末尾了，方便、实用。

## 将`m/d/y`转换为`y-m-d`

如果仅仅选中进行格式转换无法搬到，查找后可以通过【数据】-> 【拆分】里面来进行转换。

参考：

- [excel录入技巧：如何进行日期格式的转换](https://zhuanlan.zhihu.com/p/85613944)
- [如何在Excel中将日期转换为yYYY-MM-DD格式？](https://zh-cn.extendoffice.com/documents/excel/3289-excel-convert-date-to-yyyy-mm-dd-format.html)