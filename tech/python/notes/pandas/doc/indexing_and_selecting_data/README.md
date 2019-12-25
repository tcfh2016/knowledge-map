# [索引和选择数据/Indexing and selecting data]https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

Pandas里面常用的数据结构有Series, DataFrame，无论哪一种都定义了方便进行索引的标签，比
如：Series的index，DataFrame的index和columns，相当于对于每一个维度都拥有各自的索引标
记。

## 不同的索引方法

Pandas现在提供以下多维索引方法来进行数据的选择。

- `.loc`：基于标签的选择方法，当对应的条目找不到时会抛出KeyError错误，它接收的输入包括：
  - 单个标签，比如'a'。
  - 包含多个标签的列表或者数组，比如['a', 'b', 'c']。
  - 基于标签的切片，比如['a':'f']。*注：此时的切片是全闭区间*
- `iloc`：基于整数下表的选择方法，当对应的条目找不到时会抛出IndexError错误，它接收的输
入包括：
  - 单个整数下标，比如5。
  - 包含多个整数下标的列表或者数组，比如[4, 3, 0]。
  - 基于标签的切片，比如[1:7]。*注：此时的切片是半开半闭区间*


## 基础索引

`[]`是索引运算符，也是最基本的数据的选择方法。对于Series来说，series[label]表示获取标
签对应的值。对于DataFrame来说，dataframe[column_name]表示获取对应列名的列（对应类型为
Series），获取多列的时候要再写一个列表，比如dataframe[[c1, c2]]，不要写成[c1,c2]。

另外也可以通过基于属性的索引方法来选择Series的某个值或者DataFrame的某个列（Series）：

```
improt pandas as pd

s = pd.Series([4,2,1,0], index=['a', 'b', 'c', 'd'])
print(s['a'])
print(s.b)

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

print(df['A'])
print(df.A)
print(df[['A', 'B']])
```

但需要注意的是基于属性的索引选取的劣势：

- 当索引为整数时无效。
- 当索引包含多个单词时无效。

## 切片

在使用索引运算符`[]`时可以进行切片索引。需要注意的是对于DataFrame来说在进行切片时是以行
为单位，而不是在选择的时候以列为单位。在使用`loc`进行切片的时候必须要使用标签名称，而不
能使用整数索引，而使用`iloc`进行切片时必须使用整数索引。

```
import pandas as pd

s = pd.Series([4, 2, 1, 0], index=['a', 'b', 'c', 'd'])
print(s[:2])   # 选择0~2之间所有的值
print(s[::3])  # 隔断选择，从前往后选，即选择0，3，6...
print(s[::-1]) # 隔断选择，从后往前选，即选择3，2，1...

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df[1:2]) # 半闭半开区间
print(df.loc['2000-01-01':'2000-01-02']) # 全闭区间
print(df.iloc[0:1]) # 半闭半开区间
```

## 重新索引

Pandas的`reindex()`方法是创建一个新索引对应的新对象，也即将之前的数据按照新索引重新编排。
如果有的新索引在之前对象数据对象里面不存在，那么将引入NaN值。

如果需要过滤掉非法的index，可以使用`intersection()`。

```
import pandas as pd

s = pd.Series([4, 2, 1, 0], index=['a', 'b', 'c', 'd'])
print(s)

ns = s.reindex(['d', 'c', 'b', 'a', 'h'])
print(ns)

labels = ['d', 'c', 'b', 'a', 'h']
ns2 = s.loc[s.index.intersection(labels)]
print(ns2)
```

## 使用赋值的方式进行扩展

Series的扩展很简单，和字典类似，对不存在的索引进行赋值即添加新的值。对于DataFrame来说也
是一样，注意区别`dataframe[x]`和`dataframe.loc[x]`的不同（前者选择列，后者选择行，前者
和`dataframe.loc[:, x]`是等效的）。

```
import pandas as pd

s = pd.Series([4, 2, 1, 0], index=['a', 'b', 'c', 'd'])
print(s)
s['e'] = 100
print(s)

df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)

df['E'] = 10
print(df)
df.loc[:, 'E'] = 12
print(df)
```

## 布尔索引

使用布尔向量来过滤数据，比如`series > 0`会创建同等大小的布尔向量，那么`series[series>0]`
则是基于布尔向量进行值的选择。

```
import pandas as pd

s = pd.Series(range(-4, 3))

print(s[(s > -2) & (s < 2)]) # 1.
print(s[(s > -2) & (s < 2)])

print (s.isin([-1, 0, 1]))   # 与1.等效
print (s[s.isin([-1, 0, 1])])
```

除了使用逻辑运算符（| for or, & for and, ~ for not）和比较运算符（>, <, ==）来构建布
尔向量之外，使用`isin`是另外一种方法。
