## 如何标记？

matplotlib提供了`annotate()`来进行图形的标记，官方文档在[这里](https://matplotlib.org/stable/tutorials/text/annotations.html#id1)。

该接口可以指定要标记的点，箭头形状，标记文本等：

```
ax.annotate('max=' + str(y_max), xy=(x_max, y_max), xytext=(x_max, y_max+5),
            arrowprops=dict(arrowstyle="->", facecolor='black'),
            )
```

参考：

- [Annotating with Arrow](https://matplotlib.org/stable/tutorials/text/annotations.html#annotating-with-arrow)
