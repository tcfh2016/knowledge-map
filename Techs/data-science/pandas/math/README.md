
## valueError: could not convert string to float


在使用`m = score['language'].iloc[0:10].mean()`求某列一些行的均值的时候，如果多个单元里面是字符串可能会提示“valueError: could not convert string to float”的错误。

解决方案：

```
m = score['language'].iloc[0:10].astype(float).mean()
```

## 统计某列的某个值有多少次

print(data['name'].value_counts()['sravan'])

参考：

- [](https://www.geeksforgeeks.org/how-to-count-occurrences-of-specific-value-in-pandas-column/)

## mean(), median(), min(), max()

通过`axis`参数来控制平均值操作：

```
drinks.mean(axis=0) # 求取每列的平均值，求值的方向为从上到下
drinks.mean(axis="index")

drinks.mean(axis=1) # 求取每行的平均值，求值的方向为从左至右
drinks.mean(axis="columns")
```

可以指定对应列来求取某列的最大值:

```
print(df["YY"].max())
```

求取均值的时候会自动过滤掉`np.nan`但不会过滤掉0，如果想过滤掉0那么需要提前使用`df.replace(0, np.NaN)`将0替换为np.nan。

参考：

- [mean calculation in pandas excluding zeros](https://stackoverflow.com/questions/33217636/mean-calculation-in-pandas-excluding-zeros)


## 求均值时长度超了怎么办？

比如某列的长度为10，但是求均值的范围选到了15？不会计算超出的部分。


## 统计DataFrame某列的和

`dataframe.sum()`默认对“行”进行求和，即以列为单位求每列对应所有行的和，可以指定坐标轴，
比如`dataframe.sum(axis=1)`对“列”进行求和，按行为单位求对应所有列的和。

对单一列进行求和可以使用`dataframe['column'].sum()`。


## 统计DataFrame某列相同值的个数

```
df["category"].value_counts()

df = pd.DataFrame({'a':list('abssbab')})
df.groupby('a').count()

输出：
b    3
a    2
s    2


print (df['col'] == 1).sum()
```

参考：

- [count the frequency that a value occurs in a dataframe column](https://stackoverflow.com/questions/22391433/count-the-frequency-that-a-value-occurs-in-a-dataframe-column)


## min()/max()


## idxmin()/idxmax()

`idxmax()`和`idxmin`这两个函数用来返回最大值、最小值的索引，先看这两个函数的释义：

- [pandas.DataFrame.idxmax](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmax.html)

> Return index of first occurrence of maximum over requested axis.

- [pandas.DataFrame.idxmin](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmin.html)

> Return index of first occurrence of minimum over requested axis.