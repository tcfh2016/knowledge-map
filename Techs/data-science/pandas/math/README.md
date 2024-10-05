# 常用统计

- 求和：`df.sum(axis=0, skipna=1)`，`df[col].sum(axis=0, skipna=1)`
- 求均值：`df.mean(axis=0, skipna=1)`
- 最大值：`df.max(axis=0, skipna=1)`，对应`idxmax()`返回最大值的索引
- 最小值：`df.min(axis=0, skipna=1)`，对应`idxmin()`返回最小值的索引
- 中位数：`df.median(axis=0, skipna=1)`
- 众数：`df.mode(axis=0, skipna=1)`，即出现最多的数

在使用`m = score['language'].iloc[0:10].mean()`求某列一些行的均值的时候，如果多个单元里面是字符串可能会提示“valueError: could not convert string to float”的错误。

解决方案：

```
m = score['language'].iloc[0:10].astype(float).mean()
```


注：

1. 默认对“行”进行运算，即以列为单位求每列对应所有行的和。`axis=1`代表逐列优先，按行为单位求对应所有列的和。
2. `skipna = 1`表示跳过缺失值的处理，并非将其替换为`0`来处理。


# 其他统计

## 方差、标准差

方差用于衡量一组数据的离散程度，即各组数据与它们平均数的差的平方。方差越小说明数据波动越小。

```
df.var(axis=None, skipna=True)
```

*注：pandas中计算的方差为无偏样本方差（方差和/样本数-1），numpy中的为样本方差（方差和/样本数）。*

标准差又称“均方差”，是方差的平方根。使得比较的量纲一致。


## 分位数

分位数也称“分位点”，以概率为依据将数据分割为几个等份，常用的有中位数（二分位）、四分位数、百分位数等。

```
df.quantile(q=0.5, axis=0)
```


## 某个值出现次数

print(data['name'].value_counts()['sravan'])

参考：

- [How to Count Occurrences of Specific Value in Pandas Column?](https://www.geeksforgeeks.org/how-to-count-occurrences-of-specific-value-in-pandas-column/)
- [count the frequency that a value occurs in a dataframe column](https://stackoverflow.com/questions/22391433/count-the-frequency-that-a-value-occurs-in-a-dataframe-column)


# 数据格式化

## 设置小数位数

使用`round()`函数来设置：

```
# 保留两位小数
df.round(decimals=2)`

# A1列保留一位小数，A2列保留两位小数
df.round({'A1':1, 'A2':2})
```

另外可以通过自定义函数，比如`df.applymap(lambda x : '%.2f'%x)`，这种方式处理后数据类型变为`object`，后续计算需要将数据类型转换过来。


## 设置百分比

通过自定义函数对数据进行格式处理：

```
df[col].apply(lambda x : format(x, '.2%'))

df[col].map(lambda x : format(x, '.2%'))
```


## 设置千分位

```
df[col].apply(lambda x:format(int(x), ','))
```