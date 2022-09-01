## Cleaning Empty Cells

在分析数据时，空值可能给与你错误的结果，所以我们要移除它。这在数据集非常大的时候是可行的。

移除空值很简单，直接使用`dropna()`函数即可，这里有两个需要注意的地方：

1. `dropna()`移除的是包含空值的行，不是列。且移除后每行的索引不会变
2. 移除操作不会影响原始的DataFrame，而是返回一个新的DataFrame。如果你想将修改直接应用在原始DataFrame上，那么使用`inplace = True`即可。

## 另一种方法

另一种方法是使用`fillna()`替换掉空值，比如`df.fillna(130, inplace = True)`是将df里面的空值填充为130。

当然如上的方法是替换掉df中所有的空值，我们可以针对特定列的空值进行替换，下面的例子只替换掉Calories这一列：

```
df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)
```

这里130是随便选的，更合适的做法是求取对应列的统计值。常用的是`mean()`, `median()`和`mode()`，分别指代平均值、中值、频次最高的值。

```
df = pd.read_csv('data.csv')

x = df["Calories"].mean()
y = df["Calories"].mean()
z = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
df["Calories"].fillna(y, inplace = True)
df["Calories"].fillna(z, inplace = True)
```
