Pandas的两个主要数据结构为 Series 和 DataFrame，它们为大多数应用提供了一种可靠的、易于
使用的基础。

# Series

Series是一种类似于一维数组的对象，它由一组数据（各种NumPy数据类型）以及一组与之相关的数
据标签（即索引）组成。

## Series 创建

- 由一组数据产生简单的Series，未指定索引时默认创建一个0~N-1（N为数据的长度）的整数型索
引。

```
obj = Series([4, 7, 0, -3])
```

- 指定对各个数据点标记的索引。

```
obj = Series([4, 7, 0, -3], index=['d', 'b', 'a', 'c'])
```

- 通过字典创建

```
sdata = {'oli': 1000, 'tae': 2000, 'Oed': 500}
obj = Series(sdata)
```

## Series 读取

- values, index 获取

通过 Series的 values和 index属性来获取值和索引，注意在返回类型上值是以数组类型（array）
返回，而索引则由特定的索引对象（Int64Index）。

- 值选取

通过索引的方式选取单个或者多个值。

```
obj['a']
obj[['a', 'd']]
```

# DataFrame

DataFrame 是一个二维表式的数据结构，由data(数据)、rows(行)、columns(列)组成，数据基于
行列进行存储，因此它既有行索引也有列索引，可被看做是由Series组成的字典（共用同一个索引）。

![](dataframe.png)


## DataFrame创建

- 传入等长的列表来创建

如果不指定行/列索引，默认索引为0...N-1(行/列的长度)。

```
import pandas as pd
students = ['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry']
df = pd.DataFrame(students)
```

- 传入等长的字典来创建

基于dictionary创建的时候默认以key做为列索引：

```
import pandas as pd
data = {'Name':['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry'],
        'Age':[18, 21, 29, 18, 23]}
df = pd.DataFrame(data)
```

- 指定行列名

指定列序列时按照指定顺序进行排列。

```
import pandas as pd
data = {'Name':['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry'],
        'Age':[18, 21, 29, 18, 23]}
df = pd.DataFrame(data, columns=['Age', 'Name'],
                  index=['one', 'two', 'three', 'four', 'five'])
```

- 直接以SQL数据库、CSV、Excel文件做为数据源来创建它们

## DataFrame 获取

- columns / index 获取

通过`df.columns`选中所有列名。通过`df.index`选中所有行名。

- 列的获取

通过类似字典标记或属性的方式，可以将 DataFrame的列获取为一个 Series。

```
df.Age # 看起来似乎不可行。
df['Age']
df[['Age','Name']] # 注意选取多列和多行时候的不同形式
```

一次性指定多个列的名称可以同时选中两列，比如如上例子里面`df['Name', 'Age']`。

- 行的获取

选择行时需要使用`loc`方法，并且选择多行的时候在语法上与列有些不同。

```
df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])

print(df.loc['b'])  # 通过索引访问元素，之前是df.ix['b']，但已经不推荐使用旧的方法。
print(df.loc[['a', 'b']]) # 索引多个元素。
print(df['a':'c'])        # 索引'a', 'b', 'c'三行
print(df[0:1])            # 索引'a'一行数据
```

- 多行多列

```
df.loc[:, ['A', 'B']]
```

- 条件选择

```
 df[df.A > 0] # 以某列的数据做为标准选择数据
 df[df['A'] > 0]
 df[df > 0]   # 选择 df中大于0的数，其余置为 NaN
```

## DataFrame 修改

- 修改 index

直接将DataFrame的index修改为其中的某一列：

```
min_max_df.index = min_max_df['日期'] # 之前的'日期'列依然存在
min_max_df = min_max_df.set_index('日期', drop=True) #
```

*注：DataFrame的set_index函数会将一个或多个列转换为行索引，并创建心的DataFrame。*


- 修改行/列名

修改行/列名有两种方式：直接赋值和调用 rename方法：

```
df.index = [1, 2, 3, 4]
df.columns = ['price']
df.rename(columns=lambda x:x.replace('$',''), inplace=True)
df.rename(columns={'a':'b'}, inplace=True)
```

*注：Index 对象是不可修改的。因此df.index[1] = 'c'会提示错误。*

- 修改整列

直接通过赋值的方式修改（添加）：

```
df['numbers'] = 1.0
df.numbers = 1.0
```

将列表或数组赋值给某列时，其长度必须跟DataFrame的长度匹配：

```
val = Series([-1, -2, -3, -4], index=['b', 'a', 'c', 'd'])
df['newdata'] = val
df.newdata = val
```

- 删除列

删除列时必须通过索引的方式指定，不能通过属性的方式来指定。

```
del df['newdata']
del df.newdata # 会提示错误。
```

# 类型转换



# 操作方法

## reindex

DataFrame 最初的数据与创建时指定的 index顺序密切相关，通过 reindex方法可以进行重新排列。
在使用 reindex()方法时可以指定一些额外选项，比如 fill_value=0 表示对于其中的 NaN的值全
填写为 0。

```
obj = Series([4.2, 2.3, -1.3, 5.2], index=['d', 'b', 'c', 'a'])
obj1 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
```

## map(f)/applymap(f)

map作用于 Series，applymap作用于 DataFrame，表示对每个元素应用函数f。

# NaN (Not a Number)

pandas中缺失的数据项会被填写为 NaN，表示缺失或NA值。对于NA的处理包括如下几类：

- 使用 isnull()，notnull() 来检查某个值是否为 NA。
- 使用 fillna(), replace() 和 interpolate() 来替换 DataFrame 里面的所有 NA。
- 使用 dropna() 将包含有 NA的行和列删除。

## 滤除缺失数据：dropna(criteria)

对于一个 Series, dropna返回一个仅含非空数据和索引值的 Series:

```
from pandas import Series, DataFrame
import pandas as pd
import numpy as np # NaN 在numpy里定义，因此使用NaN需要先import numpy。

s = Series([1, np.NaN, 3.2, np.NaN, 7])
print(s.dropna())
```

然而，对于DataFrame调用 dropna的处理更复杂一些，因为它会默认丢弃所有包含缺失值的行。此
时有两种调整方法：

  - 传入`how = all`，丢弃全为NA的那些行；
  - 传入`thresh=3`来设定丢弃的标准，表示行超过多少个NA时丢弃；
  - 传入参数`axis=1`来指示对于列的操作。

## 填充缺失数据：fillna(new_value)

在大多数情况下，fillna方法是填充缺失数据的主要函数。

  - df.fillna(0)将所有NaN更改为0。
  - df.fillna({1:0.5, 2:-1})将对应列的NaN填充为对应的值，用`axis=1`来指示不同的轴。
  - 传入`inplace=True`在现有对象上进行修改。

# 参考

- [Python | Pandas DataFrame](https://www.geeksforgeeks.org/python-pandas-dataframe/)
- [pandas 修改 DataFrame 列名](https://www.cnblogs.com/hhh5460/p/5816774.html)
- 《利用Python进行数据分析》
- [object conversion](http://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics-object-conversion)
