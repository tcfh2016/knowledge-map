## [pandas.DataFrame.groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)

函数`groupby`是对DataFrame进行分组，这个分组的操作通常仅仅是一系列操作中的排头阵。也就是说，我们在应用`groupby`这个函数不仅是“为了分组而分组”，而是“为了更重要的目的不得不先进行分组”。

比如，下面的例子展示的是求取每组分组的均值。在这个例子里面我们分组不是目的，而求取每个分组才是目的。

```
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
df
   Animal  Max Speed
0  Falcon      380.0
1  Falcon      370.0
2  Parrot       24.0
3  Parrot       26.0

df.groupby(['Animal']).mean()
        Max Speed
Animal
Falcon      375.0
Parrot       25.0
```

参考：

- [Group By: split-apply-combine](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)


## groupby 之后的二维索引怎么访问？

比如下面这样的数据，我怎么能够访问到其中某个元素的值？

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

