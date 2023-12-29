## 图例

`plt.legend()`用来添加图例，比如默认的图例是没有说明文字的，尽管我们在绘制图形的时候
设定了`label`属性。

![](use_legend_ex_random100_no_legend.png)

如果要将图例说明显示出来，需要默认调用`legend()`将其展示出来。比如调用`plt.legend(loc=0)`
将说明显示在最佳的位置，loc参数为location code，0代表`best`, 1代表`upper right`...

![](use_legend_ex_random100_best_legend.png)


plt.legend接收不同的位置参数，0表示最佳显示位置（尽可能不阻挡数据的显示），参数列表如下：

|Loc|Description|
|-|-|
|Empty|Automatic|
|0|Best possible|
|1|Upper right|
|2|Upper left|
|3|Lower left|
|4|Lower right|
|5|Right|
|6|Center left|
|7|Center right|
|8|Lower center|
|9|Upper center|
|10|Center|

```
plt.plot(y[:, 0], lw=1.5, label='1st') # 设置第0列数据集的标签为1st。
plt.plot(y[:, 1], lw=1.5, label='2nd') # 设置第1列数据集的标签为2nd。
plt.legend(loc=0) # 使用legend, loc设置位置
```

参考

- [matplotlib.pyplot.legend](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.legend.html )
- [Matplotlib 系列之「Legend 图例」](https://zhuanlan.zhihu.com/p/41781440)

##  坐标轴标签

```
plt.xlabel('radians')
plt.ylabel('amplitude', fontsize='large') # 设置字体大小
plt.title('Sin(x)')
plt.grid() # 显示网格
```


## 坐标轴标签上显示负号(minus sign)

matplotlib默认以Unicode的形式来展示“-”，但是当你将有些图示的语系变更之后可能导致无法在坐标轴上显示出“-”，比如如下为了在图形中显示中文添加了`matplotlib.rcParams['font.sans-serif'] = ['SimHei']`从而导致无法正常显示"-"，添加如下代码关闭默认的显示形式之后可以正常显示：

```
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
```

![](./pyplot/can_show_minus_sign.PNG)

参考：

- [Unicode minus](https://matplotlib.org/gallery/api/unicode_minus.html)

## 坐标轴显示乱码(支持中文)？

使用如下命令打印出matplotlib能够支持的系统字体：

```
fonts = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in fonts:
    print(i)
```

再设定图形使用的字体：

```
plt.rcParams['font.family']=['STFangsong']
```