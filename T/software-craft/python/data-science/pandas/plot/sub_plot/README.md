## subplot问题


### Subplot

DataFrame.plot()里的`subplots`参数是对每列的数据分开展示，不属于不同DataFrame的展示方法。

```
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=2, ncols=2)

df1.plot(ax=axes[0,0])
df2.plot(ax=axes[0,1])
...
```

如果仅绘制1X2, 或者2X1的子图，那么索引ax的方式不一样：

```
fig, axes = plt.subplots(nrows=1, ncols=2)

df1.plot(ax=axes[0])
df2.plot(ax=axes[1])
```

参考：

- [How can I plot separate Pandas DataFrames as subplots?](https://stackoverflow.com/questions/22483588/how-can-i-plot-separate-pandas-dataframes-as-subplots)
- [Stuffing a pandas DataFrame.plot into a matplotlib subplot](https://stackoverflow.com/questions/21962508/stuffing-a-pandas-dataframe-plot-into-a-matplotlib-subplot/21967899#21967899)
