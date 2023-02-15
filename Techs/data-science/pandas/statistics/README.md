
## valueError: could not convert string to float


在使用`m = score['language'].iloc[0:10].mean()`求某列一些行的均值的时候，如果多个单元里面是字符串可能会提示“valueError: could not convert string to float”的错误。

解决方案：

```
m = score['language'].iloc[0:10].astype(float).mean()
```


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


## pandas.read_csv 分行统计

按照每个月份、年份进行统计。

```
df = pd.read_csv("000898.csv", encoding="gb2312", dayfirst=True, usecols = ["日期", "总市值"])
df["日期"] = pd.to_datetime(df["日期"])
df["年"] = df["日期"].dt.year
df["月"] = df["日期"].dt.month

groups = df.groupby(["年", "月"])
```

- [python pandas extract year from datetime](https://stackoverflow.com/questions/30405413/python-pandas-extract-year-from-datetime-dfyear-dfdate-year-is-not)
- [Python: Datetime to season](https://stackoverflow.com/questions/44124436/python-datetime-to-season)
