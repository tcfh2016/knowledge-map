## [Annotations](https://matplotlib.org/stable/tutorials/text/annotations.html#id1)

使用`annotate()`会在坐标系中画出两点之间的箭头：

```
ax.annotate("Annotation",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='offset points',
            )
```

上面的`xy`是注释点坐标，`xytext`是注释文本的坐标，它通过相对于xy的偏移来指定。然后注释文本与注释点之间用箭头连接起来，可以指定箭头的形状。


使用注解时：

- 可以选择不同的坐标系统，默认为整体数据构建的坐标系
- 指定箭头的形状
