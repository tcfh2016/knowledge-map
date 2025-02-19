# Plots

## 组成

- Y-axis：一幅图可以有最多3个Y坐标
- X-axis：一幅图仅有1个X坐标，特别注意的是这里不能用`Series`，必须要`list`
- Series：数据序列
- Legend：可选的图例


## 绘图

首先创建x, y坐标轴，然后通过`add_line_series()`来绘图：

```
dpg.add_plot_axis(dpg.mvXAxis, label="x")
dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

# series belong to a y axis
dpg.add_line_series(sindatax, sindatay, label="0.5 + 0.5 * sin(x)", parent="y_axis")
```


## 更新

如果要更新已经绘制的图形，那么只需要重新设置对应的item：

```
dpg.set_value('series_tag', [cosdatax, cosdatay])
dpg.set_item_label('series_tag', "0.5 + 0.5 * cos(x)")
```

## 时间坐标

`Dear PyGui`不支持时间格式的X坐标，比如`dpg.add_line_series(x, y, label="test", parent="y_axis")`里面`x`是日期的格式，那么会提示`TypeError: must be real number, not Timestamp`。

解决方法就是创建对应的xticks的标签：

```
x = [v for v in range(0, 1000)]
xtime = pd.to_datetime(df['timeStamp'])[0:1000].to_list()
xtick_pairs = tuple((xtime[i], i) for i in x )

dpg.add_plot_axis(dpg.mvXAxis, label="x")
dpg.set_axis_ticks(dpg.last_item(), xtick_pairs)
```



## 参考

- [Plots](https://dearpygui.readthedocs.io/en/latest/documentation/plots.html)


