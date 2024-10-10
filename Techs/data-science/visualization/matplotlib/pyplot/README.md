# matplotlib.pyplot

`matplotlib.pyplot`是一组使用`matplotlib`的函数集合，它提供了隐式的、类似于MATLAB的绘图函数。常见设置：

```
plt.title("Matplotlib demo")
plt.grid(True) # 添加网格
plt.axis('tight') # 调整坐标宽度
plt.xlim(-1, 20)  # 设置x轴值显示范围
plt.ylim(-5, 5) # 设置y轴值显示范围
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,"ob") # o表示“圆标记”，b表示“蓝色”。
plt.show()
```

直接使用`matplotlib.pyplot`很便捷，但是它同样隐藏了不少`matplotlib`相关的细节，比如你在使用plt.xxx系列函数的时候不会看到“画布”、“绘图区域”、“坐标系”之类的概念，因为它已经隐藏起来，并多采用默认值。

但有时候为了一些需要自定义的效果，是需要做些更多的设置，比如设置`RcParams`，设置画布。


参考：

- [matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)


## 设置`RcParams`

平常对于`RcParams`的设置是通过`plt.rcParams['font.sans-serif'] = ['SimHei']`这种快捷的方式来设置的。

```
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False`
```

更完整的方式是：

```
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False`
```

参考：

- [matplotlib.RcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams)
- [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html)


## 设置画布

```
matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
```

- `num`：图形编号或名称
- `figsize`：设置画布宽高，尺寸单位为“英寸”
- `dpi`：绘图对象的分辨率，默认为80
- `facecolor`：背景颜色
- `edgecolor`：边框颜色
- `frameon`：是否显示边框

比如在绘制图形之前调用`fig = plt.figure(figsize=(10, 5), facecolor='yellow', edgecolor='r')`来设置画布。


## 设置坐标轴刻度

画图像时有时候默认的坐标轴显示可能达不到需求，需要借助`xticks`和`yticks`函数：

```
xticks(locs, [labels], **kwargs)
yticks(locs, [labels], **kwargs)
```


## 设置坐标轴范围

```
plt.xlim(left, right)   # set the xlim to left, right
plt.ylim(bottom, top)   # set the ylim to bottom, top
```

参考:

- [matplotlib.pyplot.ylim - 2.1.0](https://matplotlib.org/2.1.0/api/_as_gen/matplotlib.pyplot.ylim.html)


## 设置网格线

```
matplotlib.pyplot.grid(visible=None, which='major', axis='both', **kwargs)
```

使用`plt.grid(color='0.6', linestyle='--', linewidth=1, axis='x')`设置虚线格式的网格线，且仅仅显示y轴。

参考：

- [matplotlib.pyplot.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)


# 使用`pyplot.plot()`

该函数的原型为：

```
matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
```

- `plt.plot(y)`：如果仅仅给plot传递单个列表或者数组，那么`y`默认为Y轴的数据，并自动生成X轴的数据
- `plt.plot(x, y)`：如果给plot传递两个列表或者数组，那么`x`默认为X轴的数据，`y`默认为Y轴的数据
- `plt.plot(x, y, format)`：`format`为图形格式
- `plt.plot(x1, y1, format1, x2, y2, format2)`：画两条线

如果要画多条线那么需要多次调用`plt.plot(x, y)`，如果要使用第二坐标那么设置也不同：

```
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')
```


## 线条样式

通过`plt.plot(x, y, color='r', linestyle='--')`设置线条的样式和颜色。

颜色：

|Character|Color|
|-|-|
|b|Blue|
|g|Green|
|r|Red|
|c|Cyan|
|m|Magenta|
|y|Yellow|
|k|Black|
|w|White|

样式：
|Character|Symbol|
||-|-|
|-|Solid line style|
|--|Dashed line style|
|-.|Dash-dot line style|
|:|Dotted line style|
|.|Point marker|
|,|Pixel marker|
|o|Circle marker|
|v|Triangle_down marker|
|^|Triangle_up marker|
|<|Triangle_left marker|
|>|Triangle_right marker|
|1|Tri_down marker|
|2|Tri_up marker|
|3|Tri_left marker|
|4|Tri_right marker|
|s|Square marker|
|p|Pentagon marker|
|*|Star marker|
|h|Hexagon1 marker|
|H|Hexagon2 marker|
|+|Plus marker|
|x|X marker|
|D|Diamond marker|
|d|Thin diamond marker|
|||Vline marker|


通过给定参数的方式：`plot(x, y, linewidth=1.5)`，或者先返回一个plot对象`line = plot(x, y)`，再给该对象设置`line.set_linewidth(1.5)`。


参考：

- [matplotlib.pyplot.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
- [Plot multiple line graphs from a dataframe using Matplotlib](https://stackoverflow.com/questions/70995638/plot-multiple-line-graphs-from-a-dataframe-using-matplotlib)
- [Adding a y-axis label to secondary y-axis in matplotlib](https://stackoverflow.com/questions/14762181/adding-a-y-axis-label-to-secondary-y-axis-in-matplotlib)


## 标记样式

“标记”就是线条上面的数据点，可以通过`plt.plot(x, y, marker='r', mfc='b')`设置线条的样式和颜色。标记形状：

- `.`：点标记
- `,`：像素标记
- `o`：实心圆标记
- `v`：倒山角标记
...


## 文本标签

```
matplotlib.pyplot.text(x, y, s, fontdict=None, withdash=False, **kwargs)
```

这个函数需要为每个数据点调用一次，比如下面的代码，是以水平居中，垂直居下的方式来显示每个标签：

```
for a, b in zip(x, y):
    plt.text(a, b+3, b, ha='center', va='bottom', fontsize=9)
```


## 标题

```
matplotlib.pyplot.title(label, fontdict=None, loc='center', pad=None, **kwargs)
```


## 图例

```
matplotlib.pyplot.legend(*args, **kwargs)
```

手动添加图例的时候可能文本显示不全，这个时候使用`legend(('title',)`这样的格式可以显示全。

使用`plt.legend(('title',), loc='center', fontsize=10)`设置图例居中显示，使用`plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)`将图例显示在图表外面。

参考：

- [matplotlib.pyplot.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)


## 使用两个y坐标轴来显示两个数量级数据集的展示

```
fig = plt.figure(figsize=(7, 4)) # 设置图形大小

ax1 = fig.subplots()
np.random.seed(2000)
y = np.random.standard_normal((20, 2))
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro') # 设置颜色为红色，样式为圆形。
plt.legend(loc=8)

ax2 = ax1.twinx()
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro') # 设置颜色为红色，样式为圆形。
plt.legend(loc=0) # 使用legend, loc设置位置
plt.ylabel('value 2nd') # 第二个y坐标

plt.grid(True) # 添加网格
plt.axis('tight') # 调整坐标宽度
```

## 曲线间填充

matplotlib库允许我们对曲线间或者曲线下面的区域填充颜色，这样就可以显示那部分区域的值。

```
ax.plot(x, y1, x, y2, color='black')
ax.fill_between(x, y1, y2, where=y2>=y1, facecolor='darkblue', interpolate=True)
ax.fill_between(x, y1, y2, where=y2<=y1, facecolor='deeppink', interpolate=True)
```