## 柱状图 / 直方图

直方图通常被用于可视化数据的分布，谈论直方图的时候会涉及一些术语，比如`bin`代表一定间隔下数据点频率的垂直矩形，`bin`以固定的间隔创建。

直方图经常被用在图像处理软件中作为可视化图像属性（如给定颜色通道上光的分布）的一种方式，还可以应用在计算机视觉算法来检测峰值，用来辅助进行边缘检测、图像分割等。

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

散点图能够标记出两个变量之间的相关关系（ correlation ），尤其是对于非线性关系的数据。

可以用`pyplot.scatter`来画散点图，效果和使用`pyplot.plot`指定`o`的样式一样。该函数的正式声明如下：

```
matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)
```

其中`s`表示大小，默认单位1的大小为1/72英寸的平方，`c`表示颜色深浅的标记值。散点图可以可以作为更高级的多维数据可视化的基础，比如绘制散点图矩阵（ scatter plot matrix ）。

```
plt.scatter(x, y, size, color)
plt.colorbar(); # 显示颜色条
```

参考：

- [matplotlib.pyplot.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)

## 饼图

饼图描述数值的比例关系，每个扇区的弧长大小为其所表示的数量的比例。饼图很紧凑，看上去很有美感，但有两个不足：

- 难以对数量进行比较。
- 以特定角度（视角）的方式和一定颜色的扇形展示数据，会使我们的感觉有倾向性，从而影响对于所呈现数据得出的结论。

```
matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, normalize=True, hatch=None, data=None)[source]
```

主要的几个参数：

- `autopct`，使用'%.2f%%'按百分比显示

## 误差条形图

误差条可以很容易地表示误差偏离数据集合的情况，通常用来可视化数据集合中的测量不确定度（ uncertainty of measurement ）或者指出错误。实验科学（ experimental sciences ）领域的大多数论文都应该在描述数据精度的时候包含误差条。

不过这在表示上没有统一标准，可以显示一个标准差（ standard deviation ）、一个标准误差（ standard error ）或者 95% 的置信区间（ confidence interval ）。


```
x = np.arange(0, 10, 1) # 从高斯分布中生成度量值
y = np.log(x) # 从度量值中计算出 y 值
xe = 0.1 * np.abs(np.random.randn(len(y))) # 从标准正太分布中生成一些误差

plt.bar(x, y, yerr=xe, width=0.4, align='center', ecolor='r', color='cyan',
                                                    label='experiment #1');
plt.xlabel('# measurement')
plt.ylabel('Measured values')
plt.title('Measurements')
plt.legend(loc='upper left')
```
