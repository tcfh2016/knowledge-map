## 图形（figure）和子区（subplots）

图形对应到现实生活中类似于“画板”，在这个“画板”上可以分割为多个“子区”来画不同的图形。

- 调用`subplot()`就是指定所有子区的行数和列数以及要操作的`plot`的序号。
- 调用`figure()`会显式地创建一个图形，表示一个图形用户界面窗口。

使用`plot()`或类似的方法会隐式地创建图形。这对于简单的图表没有问题，但是对于更高级的应用，能显示创建图形并得到实例的引用是非常有用的。

一个图形包括一个或多个子区。子区能以规则网格的方式排列 plot。我们已经

如果需要更多的控制，我们需要使用 matplotlib.axes.Axes 类的坐标轴实例。这样可以把 plot 放置在图形窗口中的任意位置，例如可以把一个小的 plot 放在一个大的 plot 中。


## 画多副图

```
plt.figure()
plt.plot(x) # 画第一幅图

plt.figure()
plt.plot(y) # 画第二幅图
```

上面的`plt.figure()`相当于创建了画布，如果我只调该函数一次，调用`plt.plot()`两次，那么就会在同一副图中画两条线。

## 画多子图

使用`subplot()`在一幅图里画多个子图。该函数的原型为：

```
matplotlib.pyplot.subplot(*args, **kwargs)
```

其中`args`为`(a, b, c)`，分别代表numrows, numcols, and fignum，分别用来指定一幅图里面有多少个子图，fignum是标记子图的序号，从1开始。这里的numrows/numcols实际上确定了子图的布置方式：横向或者纵向。


默认为`(1, 1, 1)`也就是有1行1列个子图，index为1。如果我要将两个子图画在同一副图里，就用：

```
plt.subplot(1, 2, 1)
plt.plot(x) # 画第一幅子图

plt.subplot(1, 2, 2)
plt.plot(y) # 画第二幅子图
```

参考：

- [matplotlib.pyplot.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot)


## 如何移除某个subplot

可以使用`delaxes`函数：

```
# 创建2行3列共6个subplots
fig, axes = plt.subplots(2, 3, sharex=True, sharey='row')

# 移除最后一个subplots
fig.delaxes(axes[1][2])
```

参考：

- [Delete a subplot](https://stackoverflow.com/questions/14694501/delete-a-subplot)

## subplots之间共享x/y轴坐标

```
# 如果所有的subplots共享y轴坐标，但是x轴坐标按列共享可以这么做
import matplotlib.pyplot as plt
fig, ax = plt.subplots(3, 2, sharey=True, sharex='col')
```

参考：

- [Share axes in matplotlib for only part of the subplots](https://stackoverflow.com/questions/23528477/share-axes-in-matplotlib-for-only-part-of-the-subplots)


## 不显示X轴坐标

```
axs[1, 1].axis("off")
axs[0, 0].xaxis.set_visible(False)
```

参考：

- [Turn off axes in subplots](https://stackoverflow.com/questions/25862026/turn-off-axes-in-subplots)


## 刻度

刻度是图形的一部分，由刻度定位器（tick locator，指定刻度所在的位置）和刻度格式器（tick formatter，指定刻度显示的样式）组成。

刻度有主刻度（major ticks）和次刻度（minor ticks），默认不显示次刻度。主刻度和次刻度可以被独立地指定位置和格式化。

```
ax = plt.gca() # 获取当前的坐标轴
ax.locator_params(tight=True, nbins = 10) # 将视图设置为紧密，并将最大刻度间隔数设置为10
```

## 日期刻度

```
import matplotlib as mpl

ax = gca() # 获取当前得坐标轴
ax.plot_date(dates, values, linestyle='-', marker='') # 用时间数据来绘制图像

date_format = mpl.dates.DateFormatter('%Y-%m-%d') # 指定时间的格式
ax.xaxis.set_major_formatter(date_format) # 应用时间的格式

# 自动设置日期标签格式，默认情况下，将标签旋转30度，使用rotate这个参数指定不同的旋转度，使用bottom 这个参数为日期标签提供更多空间
fig.autofmt_xdate()
```