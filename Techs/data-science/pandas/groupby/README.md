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


## groupby

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