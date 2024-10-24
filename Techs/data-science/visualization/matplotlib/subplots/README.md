## 显式和隐式的方式

用显式的方式画多个子区的时候需要单独访问不同的`Axes`对象，比如下面代码里面的`axs[0]`, `axs[1]`：

```
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2)
axs[0].plot([1, 2, 3], [0, 0.5, 0.2])
axs[1].plot([3, 2, 1], [0, 0.5, 0.2])
```

用隐式的方式画子区的时候使用`pyplot.plot()`会自动跟踪上一次的绘图元素，所以看起来代码相同：

```
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [0, 0.5, 0.2]) #第一次调用plt.plot()
plt.subplot(1, 2, 2)
plt.plot([3, 2, 1], [0, 0.5, 0.2]) #第二次调用plt.plot()，相同的语句
```

参考：

- [Why be explicit?](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#why-be-explicit)


## 图形（figure）和子区（subplots）

图形对应到现实生活中类似于“画板”，在这个“画板”上可以分割为多个“子区”来画不同的图形。

- 调用`subplot()`就是指定所有子区的行数和列数以及要操作的`plot`的序号。
- 调用`figure()`会显式地创建一个图形，表示一个图形用户界面窗口。

使用`plot()`或类似的方法会隐式地创建图形。这对于简单的图表没有问题，但是对于更高级的应用，能显示创建图形并得到实例的引用是非常有用的。

如果需要更多的控制，我们需要使用 matplotlib.axes.Axes 类的坐标轴实例。这样可以把 plot 放置在图形窗口中的任意位置，例如可以把一个小的 plot 放在一个大的 plot 中。


## 画多子图/`subplot()`

使用`subplot()`在一幅图里画多个子图。每绘制一个子图都需要调用一次该函数，有些麻烦。该函数的原型为：

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


## 画多子图/`subplots()`

使用`subplots()`可以提前布局好子图，然后通过调用不同的坐标轴对象`axes`来画子图。该函数原型为：

```
matplotlib.pyplot.subplots(nrows, ncols, sharex, sharey)
```

可以直接调用坐标轴对象来绘图，也可以通过DataFrame传入指定的坐标轴对象来绘图：

```
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=2, ncols=2)

df1.plot(ax=axes[0,0])
df2.plot(ax=axes[0,1])
```

参考：

- [How to plot multiple dataframes in subplots](https://stackoverflow.com/questions/22483588/how-to-plot-multiple-dataframes-in-subplots)


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



