
## 设置Y轴为百分比样式

参考：

- [Format y axis as percent](https://stackoverflow.com/questions/31357611/format-y-axis-as-percent)

## 如何调整横坐标样式以显示更多项目

如下图，怎么调整横坐标标签显示样式，支持更多的显示。

![](low_x_item_number.png)

```
asset_plot = self.asset_df.plot()
asset_plot.set_xticks(range(len(self.asset_df.index)))
asset_plot.set_xticklabels(self.asset_df.index, rotation=90)
plt.show()
```

通过`set_xticks`设定所有的tick数，另外通过`set_xticklabels`设定标签的显示样式。

参考：

- [How to plot a pandas multiindex dataFrame with all xticks](https://stackoverflow.com/questions/21281322/how-to-plot-a-pandas-multiindex-dataframe-with-all-xticks)
- [Matplotlib:: Not Showing all x-axis data frame variable](https://stackoverflow.com/questions/32572419/matplotlib-not-showing-all-x-axis-data-frame-variable?rq=1)

## DataFrame.plot / 画图

pandas 为 DataFrame 提供了专门的绘图函数`plot`，支持多种参数。

```
DataFrame.plot(x=None, y=None, kind='line', ax=None, subplots=False, sharex=None, sharey=False, layout=None, figsize=None, use_index=True, title=None, grid=None, legend=True, style=None, logx=False, logy=False, loglog=False, xticks=None, yticks=None, xlim=None, ylim=None, rot=None, fontsize=None, colormap=None, table=False, yerr=None, xerr=None, secondary_y=False, sort_columns=False, **kwds)[source]
```

- x,y 默认为None，取用的是DataFrame的数据,y 指定列标签(label)或者位置(position)，可以
展示多列数据。
- kind 为图形形式，支持line, bar, barh, hist, box, pie, scatter
- subplots 是否为每一列数据单独做图
- sharex, sharey 当subplots为True的时候是否共享 axis label
- layout 部署subplot 的方式： tuple, rows, columns
- use_index 默认以 index作为 ticks for x axis
- title 放置在图形上方的标题，多个子图时传入列表
- grid 是否使能网格
- legend 防止图例： Ture/False/reverse
- secondary_y，默认False，指定哪些列数据采用辅坐标轴

画出图形时如果觉得周围留空过大的问题，查看接口当前不支持通过参数控制图形周围空白的大小。

参考：

- [pandas.DataFrame.plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)
