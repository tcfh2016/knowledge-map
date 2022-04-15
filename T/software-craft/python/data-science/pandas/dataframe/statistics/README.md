
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

## DataFrame统计

**1.如何统计DataFrame某列的和？**

`dataframe.sum()`默认对“行”进行求和，即以列为单位求每列对应所有行的和，可以指定坐标轴，
比如`dataframe.sum(axis=1)`对“列”进行求和，按行为单位求对应所有列的和。

对单一列进行求和可以使用`dataframe['column'].sum()`。

**2.如何统计DataFrame某列相同值的个数？**

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
