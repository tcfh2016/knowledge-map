## 基本概念

`Matplotlib`包含了如下绘图元素：

- `Figure`是`matplotlib`中的一个类型，翻译为“绘图窗口”或者“画布”，指的是比如操作系统中弹出的窗口，Jupyter widgets，其中可以放置多个`Axes`对象
- `Axes`这种对象指的是坐标轴区域，可以在其中展示具体的图形。
- `Axis`：x轴和y轴，代表水平和垂直的轴线。
    - 刻度：刻度标示坐标轴的分隔，包括最小刻度和最大刻度。
    - 刻度标签：表示特定坐标轴的值。

在调用`Matplotlib`函数库来绘图时有两种方式：

- 显示接口，通过OO的方式一步一步创建`Figure`，`Axes`等需要的绘图元素；
- 隐式接口，通过`Matplotlib.pyplot`一次性创建必须的绘图元素，并且自动跟踪上一次使用的`Figure`，`Axes`（解释了双坐标时候均只需要使用`plt.plot()`）。

比如，下面是一个例子展示两者的差别：

```
import matplotlib.pyplot as plt

# 显式调用，必须分三步
fig = plt.figure()
ax = fig.subplots()
ax.plot([1, 2, 3, 4], [0, 0.5, 1, 0.2])

# 隐式调用，仅需一步
plt.plot([1, 2, 3, 4], [0, 0.5, 1, 0.2])
```

参考：

- [The explicit and the implicit interfaces](https://matplotlib.org/stable/users/explain/quick_start.html#the-explicit-and-the-implicit-interfaces)
- [Matplotlib Application Interfaces (APIs)](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces)

## `Figure`

这是一个`Figure`的示意图，包括了多种绘图元素：

![](figure.png)

创建如上这样带有`Axes`的`Figure`的简单的方式是使用`plt.subplots()`，也可以直接创建不带有`Axes`的`Figure`：

```
import matplotlib.pyplot as plt

fig = plt.figure()             # an empty figure with no Axes
fig, ax = plt.subplots()       # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes  
```

## `plt.Figure`和`matplotlib.Figure`的区别

这里没有`plt.Figure`这个类型，只是`plt.figure()`这个接口。

`plt.figure()`用来更快速的创建或者激活已有的`matplotlib.Figure`，如果创建了多个窗口，尽可能使用`pyplot.close()`来关闭不用的窗口。

需要注意的是在GUI中必须直接使用`Matplotlib`的API，而非使用`pylab/pyplot`相关的接口。

参考：

- [Embedding in Tk](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html#embedding-in-tk)

## `Axes`和`Axis`

`Axes`指的是绘图窗口中的一个坐标轴区域，通常包括2个`Axis`对象。而`Axis`对象用来展示刻度、刻度标签。

- `Axes`：常见函数`set_title()`, `set_xlabel()`, `set_ylabel()`
- `Axis`：使用`Locator`和`Formatter`来控制刻度位置和标签

调用`plt.axis(xmin, xmax, ymin, ymax)`来设置坐标轴的范围。如果不设置，matploblib会自动使用能够容纳数据集的最小值。

```
matplotlib.rcParams['axes.unicode_minus']=False

l = [-1, 1, -10, 10]
plt.axis(l)
```

## `Axess`标签

```
x = np.linspace(0, 2, 100)  # Sample data.

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the Axes.

ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()  # Add a legend.


plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.

plt.xlabel('x label') #接口差别
plt.ylabel('y label') #接口差别
plt.title("Simple Plot") #接口差别
plt.legend()
```

## 

参考：

- [Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)
- [Introduction to Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html)