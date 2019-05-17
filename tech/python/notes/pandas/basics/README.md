# 概念和用法

## 定义

DataFrame 是一个二维表式的数据结构，由data(数据)、rows(行)、columns(列)组成，数据基于
行列进行存储。

![](dataframe.png)

## 创建一个DataFrame

可以通过list, dictionary来创建DataFrame，尽管真实项目当中通常直接以SQL数据库、CSV、
Excel文件做为数据源来创建它们。

```
import pandas as pd
students = ['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry']
df = pd.DataFrame(students)
```

如上的代码通过list创建了一列数据，默认行索引为0...len(students)，列索引为0。

基于dictionary创建的时候默认以key做为列索引，多个dictionary的键值需要相等：

```
import pandas as pd
data = {'Name':['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry'],
        'Age':[18, 21, 29, 18, 23]}
df = pd.DataFrame(data)
```

## 操作行与列

1.选择列

直接通过指定列的名称（可以一次性指定多个），比如如上例子里面`df['Name', 'Age']`即选中
两列。

2.选择行

选择行时需要使用`loc`方法，并且选择多行的时候在语法上与列有些不同。

```
df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])

print(df.loc['b']) # 通过索引访问元素，之前是df.ix['b']，但已经不推荐使用旧的方法。
print(df.loc[['a', 'b']]) # 索引多个元素。
```

3.删除操作


## 索引与数据选取

同时选择多个行或者多个列。

## 处理遗失数据

当某个项不包含任何数据的时候会被置为 NA (Not Available)，对于NA的处理包括如下几类：

- 使用 isnull()，notnull() 来检查某个值是否为 NA。
- 使用 fillna(), replace() 和 interpolate() 来替换 DataFrame 里面的所有 NA。
- 使用 dropna() 将包含有 NA的行和列删除。

参考：

- [Python | Pandas DataFrame](https://www.geeksforgeeks.org/python-pandas-dataframe/)

## DataFrame.plot / 画图

pandas 为 DataFrame 提供了专门的绘图函数`plot`，支持多种参数。

```
DataFrame.plot(x=None, y=None, kind='line', ax=None, subplots=False, sharex=None, sharey=False, layout=None, figsize=None, use_index=True, title=None, grid=None, legend=True, style=None, logx=False, logy=False, loglog=False, xticks=None, yticks=None, xlim=None, ylim=None, rot=None, fontsize=None, colormap=None, table=False, yerr=None, xerr=None, secondary_y=False, sort_columns=False, **kwds)[source]
```

- x,y 默认为None，取用的是DataFrame的数据
- kind 为图形形式，支持line, bar, barh, hist, box, pie, scatter
- subplots 是否为每一列数据单独做图
- sharex, sharey 当subplots为True的时候是否共享 axis label
- layout 部署subplot 的方式： tuple, rows, columns
- use_index 默认以 index作为 ticks for x axis
- title 放置在图形上方的标题，多个子图时传入列表
- grid 是否使能网格
- legend 防止图例： Ture/False/reverse
- secondary_y 是否使能/为那列数据使用辅坐标轴 boolean/sequence

参考：

- [pandas.DataFrame.plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)
