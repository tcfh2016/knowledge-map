# [pandas.DataFrame.groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)

函数`groupby`是对DataFrame进行分组，这个分组的操作通常仅仅是一系列操作中的排头阵。也就是说，我们在应用`groupby`这个函数不仅是“为了分组而分组”，而是“为了更重要的目的不得不先进行分组”。

```
df.groupby(by=None, axis=0)
```

调用`groupby()`之后的返回值是`groupby`对象，不能直接打印，而是需要调用针对每个分组的计算函数，比如：

- `df.groupby(col).sum()`：每个分组的和


## 多列分组

如果要根据多列来分组，使用`df.groupby([col1, col2]).sum()`即可，那groupby 之后的二维索引怎么访问？

```
               No1       No2       No3       No4
Quarter Week                                        
Q1      W1   -3.267340 -1.043383  1.401451 -0.319191
        W2   -0.087608 -0.265051  0.690872  1.269642
Q2      W1   -1.837899  0.407558 -1.876288 -1.196136
        W2    1.251406 -0.362495 -0.845820 -1.403688
```

以上的数据是按照两列的数据进行groupby之后的结果，这个时候可以通过元组来作为行标签，比如：

```
# 进行group分类，并求和
df.groupby(["Quarter", "Week"]).sum()

# 访问其中“No1”求和后的最大值
groups_sum.loc[groups_sum["No1"].idxmax()]["No1"]

# 或者直接指定也可以
groups_sum.loc[('Q2', 'W1')]["No1"]
```


## 用字典来定义分组

有时候想将多个列的数据统计在一起，那么可以用字典来定义好对应关系：

```
my_dict = {
        A : I
        B : I
        C : J
}

df.groupby(my_dict, axis=1).sum()
df.T.groupby(my_dict).sum()
```

该操作

## 使用聚合函数`agg`

聚合函数可以一次性统计不同组的不同统计项：

```
# 进行group分类，并求和
df.groupby(["Quarter", "Week"]).sum()

# 进行group分类，并求取每列、每个group的均值和合
df.groupby(["Quarter", "Week"]).agg(['mean', 'sum'])

# 进行group分类，并求取列col1每个group的均值和合，以及列col2每个group的均值
df.groupby(["Quarter", "Week"]).agg({col1:['mean', 'sum'], col2:['mean']})
```


# 转换

## 将`GroupBy`对象转换为`DataFrame`

```
df1.groupby([ "Name", "City"] ).count().reset_index()
```

参考：

- [Converting a Pandas GroupBy multiindex output from Series back to DataFrame](https://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-multiindex-output-from-series-back-to-dataframe)

## `transform`的作用

下面的数据记录了什么时候（sfn/slot）消息进来的时间（in）和处理完成的时间（out），它们的值都是相对于当前slot的偏移。现在的需求是要求每个slot里面消息处理的总时间：

```
sfn,slot,in,out
697,3,533,546
697,4,165,176
697,4,634,645
697,5,165,171
697,5,184,208
```

最直接的思路就是按照sfn/slot进行分组，但是分组之后需要计算每组中最后一条消息的`out`减去第一条消息的`in`。这个怎么计算？因为常规下分组之后都是求一些统计值，但是现在需要的是求分组个别元素计算得到的值。

在Series/DataFrame上使用`transform`是对所有的元素来运用特定的函数，不过我们也可以针对`GroupBy`对象来使用，这时候可以使用比如`sum`, `first`, `last`, `count`等方法。这个时候我们就可以在`GroupBy`上面使用`first`和`last`来获得分组之后的值：

```
groups = df.groupby(['sfn', 'slot'])
df['cost'] = groups['out'].transform('last') - groups['in'].transform('first')
```

当然上面的还需要进一步去重的操作，可以用如下方式代替：

```
groups = df.groupby(['sfn', 'slot'])
new_df = groups.count()
new_df['cost'] = groups['out'].last() - groups['in'].first()
new_df = new_df.reset_index()
```

参考：

- [pandas.DataFrame.transform](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html)
- [Group by: split-apply-combine](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)

## 将不同的`groupby`结果对齐到坐标轴

