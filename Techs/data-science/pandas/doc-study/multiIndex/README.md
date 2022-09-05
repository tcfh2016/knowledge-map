# [多重索引（高级索引）/MultiIndex(advanced indexing)](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced)

多重索引，也称为层次化索引（Hierarchical index），它可以支持对多维度数据的分析和操作。它通常用来进行grouping, selection,  reshaping操作，并且在从一些文件里面导入数据并且准备自己的数据集的时候你也通常需要使用多重索引来帮助操作。

## 创建多重索引对象

多重索引的创建可以从array列表、元组array、可迭代序列或者DataFrame里面创建，返回的是`MultiIndex `对象。

```
# 使用from_tuples
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
s = pd.Series(np.random.randn(8), index=index)

# 使用from_tuples
iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]
pd.MultiIndex.from_product(iterables, names=['first', 'second'])

# 使用from_frame
df = pd.DataFrame([['bar', 'one'], ['bar', 'two'],
                   ['foo', 'one'], ['foo', 'two']],
                  columns=['first', 'second'])
pd.MultiIndex.from_frame(df)
```

## 基于多重索引的选择

通过`xs`并且提供坐标轴参数来选中对应的行，比如`df2.xs('000905', level='SecuCode')`就
是选择指定level为“SecuCode”，值为“000905”的那些数据。

##
