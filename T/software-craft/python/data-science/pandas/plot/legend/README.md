## 如何显示负号？

使用`matplotlib`的时候可能导致语系变更导致无法正常显示负号，所以可以通过设置`matplotlib.rcParams['axes.unicode_minus'] = False`来调整，但是如果使用了dataframe自带的plot函数也出现这样的问题呢？




### 去掉legend中显示的index名称

如果dataframe里面的index名称不为空，这在我们选取dataframe中某列做为index的时候是很常见的，但在画图时该index的名称也会展示出来。

![](legend_shown_index_name.PNG)

一种方法是在画图的时候指定显示的legend来提代默认的展示规则（展示dataframe中所有列名）

```
value_plot.legend(value_items.columns)
```

![](legend_shown_index_name_correct.PNG)

参考：

- [Modify the legend of pandas bar plot](https://stackoverflow.com/questions/33149428/modify-the-legend-of-pandas-bar-plot)
