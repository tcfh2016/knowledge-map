## [DataFrame.plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)

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


## 设置第二坐标

```
ax = df.plot(secondary_y=['A', 'B'])
ax.right_ax.set_ylabel('AB scale')
```

参考：

- [Visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
- [xlabel and ylabel out of plot region, cannot show completely in the figure
](https://stackoverflow.com/questions/29767386/xlabel-and-ylabel-out-of-plot-region-cannot-show-completely-in-the-figure)
- [How do you change the size of figures drawn with matplotlib?](https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib)


## 如何保存图形

```
fig = df.plot(kind='hist', subplots=True, figsize=(6, 6))[0].get_figure()
plt.tight_layout()
fig.savefig('test.png')
```

参考：

- [Saving plots (AxesSubPlot) generated from python pandas with matplotlib's savefig](https://stackoverflow.com/questions/19555525/saving-plots-axessubplot-generated-from-python-pandas-with-matplotlibs-savefi)


## 图表标题

使用其中的`title`参数。


## Matplotlib中的“plt”和“ax”到底是什么?

参考：

- [What Are the “plt” and “ax” in Matplotlib Exactly?](https://towardsdatascience.com/what-are-the-plt-and-ax-in-matplotlib-exactly-d2cf4bf164a9)
- [Matplotlib中的“plt”和“ax”到底是什么?](https://zhuanlan.zhihu.com/p/221861683)


