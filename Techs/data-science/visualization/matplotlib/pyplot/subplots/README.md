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

