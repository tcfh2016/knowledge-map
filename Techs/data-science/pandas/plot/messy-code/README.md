## DataFrame.plot 时中文显示乱码

![](./basics/plot_chinese_messycode.png)

解决方法为通过`plt.rcParams['font.sans-serif'] = ['SimHei'] `将字体设置为黑体。

参考：

- [python3用matplotlib绘图出现中文乱码的问题](https://www.cnblogs.com/Icarus-suixin/p/10641085.html)


## 如何显示负号？

使用`matplotlib`的时候可能导致语系变更导致无法正常显示负号，所以可以通过设置`matplotlib.rcParams['axes.unicode_minus'] = False`来调整，但是如果使用了dataframe自带的plot函数也出现这样的问题呢？调查发现也可以如上设定来显示负号。

那么问题来了：使用df.plot的时候与整个matplotlib设置的关系是啥？