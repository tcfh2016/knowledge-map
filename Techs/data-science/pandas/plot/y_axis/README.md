## y轴显示问题


## 怎么设置y轴值的范围

使用`df.plot(ylim=(0,200))`就可以。

参考：

- [Setting Yaxis in Matplotlib using Pandas](https://stackoverflow.com/questions/17787366/setting-yaxis-in-matplotlib-using-pandas)


## 设置Y轴为百分比样式

```
vals = ax.get_yticks()
ax.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
```

参考：

- [Format y axis as percent](https://stackoverflow.com/questions/31357611/format-y-axis-as-percent)

## 设置Y轴刻度

```
ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
```