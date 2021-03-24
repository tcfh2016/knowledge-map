## DataFrame.plot / 画图

pandas 为 DataFrame 提供了专门的绘图函数`plot`，支持多种参数。

```
DataFrame.plot(x=None, y=None, kind='line', ax=None, subplots=False, sharex=None, sharey=False, layout=None, figsize=None, use_index=True, title=None, grid=None, legend=True, style=None, logx=False, logy=False, loglog=False, xticks=None, yticks=None, xlim=None, ylim=None, rot=None, fontsize=None, colormap=None, table=False, yerr=None, xerr=None, secondary_y=False, sort_columns=False, **kwds)[source]
```

- x,y 默认为None，取用的是DataFrame的数据,y 指定列标签(label)或者位置(position)，可以
展示多列数据。
- kind 为图形形式，支持line, bar, barh, hist, box, pie, scatter
- ax
- subplots 是否为每一列数据单独做图
- sharex, sharey 当subplots为True的时候是否共享 axis label
- layout 部署subplot 的方式： tuple, rows, columns
- figsize，(width, height)的元组用来指定图形的大小，以inch为单位，1inch约2.538cm
- use_index 默认以 index作为 ticks for x axis
- title 放置在图形上方的标题，多个子图时传入列表
- grid 是否使能网格
- legend 防止图例： Ture/False/reverse
- secondary_y，默认False，指定哪些列数据采用辅坐标轴

在新版本的plotting功能中DataFrame.plot已经被拆分为DataFrame.plot.line(), DataFrame.plot.area()
等单独的子函数。

## `figsize` 的使用

另外可以通过`figsize `来设置总的大小。

```
dp = df_for_plot.plot(figsize=(2,2))
plt.figure(figsize=(2,2))
```

## 第二坐标

```
ax = df.plot(secondary_y=['A', 'B'])
ax.right_ax.set_ylabel('AB scale')
```

参考：

- [Visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
- [xlabel and ylabel out of plot region, cannot show completely in the figure
](https://stackoverflow.com/questions/29767386/xlabel-and-ylabel-out-of-plot-region-cannot-show-completely-in-the-figure)
- [How do you change the size of figures drawn with matplotlib?](https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib)

## 图表标题

使用其中的`title`参数。

## 常见问题

- [x轴显示](./x_axis/README.md)
- [y轴显示](./y_axis/README.md)
- [legend显示](./legend/README.md)
- [subplot问题](./sub_plot/README.md)


### pandas保存图片以inch为单位，但网页中以像素为单位，如何处理？

参考：

- [Specifying and saving a figure with exact size in pixels](https://stackoverflow.com/questions/13714454/specifying-and-saving-a-figure-with-exact-size-in-pixels)
