## 柱状图 / 直方图

柱状图有着很多的参数：

```
plt.hist(x, bins=10, range=None, normed=False, weights=None, cumulative=False,bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None,log=False, color=None, label=None, stacked=False, hold=None, **kwargs)
```

|Parameter|Description|
|-|-|
|x|list object(s), ndarray object|
|bins|Number of bins|
|range|Lower and upper range of bins|
|normed|Norming such that integral value is 1|
|weights|Weights for every value in x|
|cumulative|Every bin contains the counts of the lower bins|
|histtype|Options (strings): bar, barstacked, step, stepfilled|
|align|Options (strings): left, mid, right|
|orientation|Options (strings): horizontal, vertical|
|rwidth|Relative width of the bars|
|log|Log scale|
|color|Color per data set (array-like)|
|label|String or sequence of strings for labels|
|stacked|Stacks multiple data sets|


## 散点图

可以用`pyplot.scatter`来画散点图，效果和使用`pyplot.plot`指定`o`的样式一样。该函数的正式声明如下：

```
matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)
```

其中`s`表示大小，默认单位1的大小为1/72英寸的平方，`c`表示颜色深浅的标记值。散点图可以表示三维的信息

```
plt.scatter(x, y, size, color)
plt.colorbar(); # 显示颜色条
```

参考：

- [matplotlib.pyplot.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)

## 饼图

```
matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, normalize=True, hatch=None, data=None)[source]
```

主要的几个参数：

- `autopct`，使用'%.2f%%'按百分比显示
