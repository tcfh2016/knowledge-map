# plt.legend

plt.legend()用来为图例添加说明，比如默认的图例是没有说明文字的，尽管我们在绘制图形的时候
设定了`label`属性。

![](use_legend_ex_random100_no_legend.png)

如果要将图例说明显示出来，需要默认调用`legen()`将其展示出来。比如调用`plt.legend(loc=0)`
将说明显示在最佳的位置，loc参数为location code，0代表`best`, 1代表`upper right`...

![](use_legend_ex_random100_best_legend.png)

# 参考

- [matplotlib.pyplot.legend](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.legend.html )
- [Matplotlib 系列之「Legend 图例」](https://zhuanlan.zhihu.com/p/41781440)
