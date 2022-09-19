## 如何标记？

matplotlib提供了`annotate()`来进行图形的标记，官方文档在[这里](https://matplotlib.org/stable/tutorials/text/annotations.html#id1)。

该接口可以指定要标记的点，箭头形状，标记文本等：

```
ax.annotate('max=' + str(y_max), xy=(x_max, y_max), xytext=(x_max, y_max+5),
            arrowprops=dict(arrowstyle="->", facecolor='black'),
            )
```

一个问题：如何获取对应的坐标呢？y轴的坐标相对好获取，但是x轴的坐标如果index并非数值类型怎么办？

比如如果刚好DataFrame的index是字符串类型，那么在标注时出现“ConversionError: Failed to convert value(s) to axis units: '2021-02-18'”的错误。需要先将`str`转换为`Timestamp`。


参考：

- [Annotating with Arrow](https://matplotlib.org/stable/tutorials/text/annotations.html#annotating-with-arrow)
- [ConversionError: Failed to convert value(s) to axis units: '2015-01-01'](https://stackoverflow.com/questions/71082435/conversionerror-failed-to-convert-values-to-axis-units-2015-01-01)



