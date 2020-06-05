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
