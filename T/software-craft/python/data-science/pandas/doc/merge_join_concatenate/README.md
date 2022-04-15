# [合并，加入，拼接/Merge, join, and concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)

## 拼接对象

Pandas提供了`concat()`来完成拼接操作，它以包括多个同质对象的列表或者字典作为主要输入对
象，同时提供其他参数给其他功能：

- objs，对象列表。
- axis，拼接依赖的轴，默认为0,即按行进行拼接。
- join，拼接方式，outter表示取交集，inner表示取并集。
- keys，可以给对象列表里不同的对象指定键值，拼接完成之后依然可以使用key访问属于之前对象
的数据。

```
pd.concat(objs, axis=0, join='outer', ignore_index=False, keys=None,
          levels=None, names=None, verify_integrity=False, copy=True)

frames = [df1, df2, df3]
result = pd.concat(frames)
```

拼接之后我们可以使用`index`选择仅使用之前某些对象的index

```
concat_with_outer = pd.concat([df1, df4], axis=1, sort=False)
print(concat_with_outer.reindex(df1.index))

concat_with_inner = pd.concat([df1, df4], axis=1, join='inner')
print(concat_with_inner.reindex(df1.index))
```

也可以使用DataFrame自带的`append()`来完成拼接。

## 合并/merge

Pandas提供高效的类似于数据库join操作的服务函数：`merge()`。

```
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)
```

### 时间序列

`merge_ordered()`可以用来合并时间序列和其他有序的数据。同时支持`fill_method`参数来对
缺失数据做填充/插值处理。


## 加入/join

DataFrame自带的`join()`可以用来进行按列拼接。默认以调用DataFrame的index为基准，当指定
join方式时可以选择以拼接对象之间的并集或交集。

```
left.join(right)
left.join(right, how='outer')
left.join(right, how='inner')
```
