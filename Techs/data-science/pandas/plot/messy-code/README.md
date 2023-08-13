## DataFrame.plot 时中文显示乱码

![](./basics/plot_chinese_messycode.png)

解决方法为通过`plt.rcParams['font.sans-serif'] = ['SimHei'] `将字体设置为黑体。

这种解决方案如果当前系统没有这个字体那么也无法显示。比如我在腾讯云服务器上画图的时候就提示“findfont: Generic family 'sans-serif' not found because none of the following families were found: SimHei”的错误。

解决方案在[这里](https://zhuanlan.zhihu.com/p/566430362)。我按照[这](https://blog.csdn.net/wtySama/article/details/105316240)里面的第一种方案是可行的。

step 1：找到字体位置

```
import matplotlib
print(matplotlib.matplotlib_fname())
```

得到字体配置文件`/home/lbc/.local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc`，而字体目录就在`/home/lbc/.local/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf`下面。

然后下载`SimHei`字体文件放到如上目录。


step 2：修改字体配置文件

```
/home/lbc/.local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc
```

将`#font.sans-serif: DejaVu Sans...`修改为`#font.sans-serif: simhei, DejaVu Sans...`。

step 3：删除`~/.cache/matplotlib`，这一步不删除不会生效。

参考：

- [python3用matplotlib绘图出现中文乱码的问题](https://www.cnblogs.com/Icarus-suixin/p/10641085.html)


## 如何显示负号？

使用`matplotlib`的时候可能导致语系变更导致无法正常显示负号，所以可以通过设置`matplotlib.rcParams['axes.unicode_minus'] = False`来调整，但是如果使用了dataframe自带的plot函数也出现这样的问题呢？调查发现也可以如上设定来显示负号。

那么问题来了：使用df.plot的时候与整个matplotlib设置的关系是啥？