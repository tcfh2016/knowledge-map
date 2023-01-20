# 层次化索引

层次化索引使你可以在一个轴上拥有多个（两个以上）索引级别，让你能够以低纬度形式处理高维度数据。

## DataFrame的列

DataFrame的 set_index方法会将其一个或多个列转换为索引，并创建一个新的 DataFrame。默认情况下那些列会从 DataFrame中移除，但也可以将其保留下来。

reset_index方法的作用与 set_index相反，层次化索引被转话为具体列，新的索引默认以0~N的整数索引替代。

## reindex

DataFrame 最初的数据与创建时指定的 index顺序密切相关，通过 reindex方法可以进行重新排列。在使用 reindex()方法时可以指定一些额外选项，比如 fill_value=0 表示对于其中的 NaN的值全填写为 0。

```
obj = Series([4.2, 2.3, -1.3, 5.2], index=['d', 'b', 'c', 'a'])
obj1 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
```

## set_index

将如下数据的day作为新的index如何处理？

```
   code         day          pe_ratio  pb_ratio
4  601318.XSHG  2019-12-23    9.7785    2.4031
3  601318.XSHG  2019-12-24    9.7982    2.4079
2  601318.XSHG  2019-12-25    9.7368    2.3928
1  601318.XSHG  2019-12-26    9.7948    2.4071
0  601318.XSHG  2019-12-27    9.8284    2.4153
```

直接使用`set_index`重设索引之后并不会在原来的DataFrame里面改动生效。

```
df.set_index('day')
```

## reset_index

可以使用`reset_index`重设DataFrame的索引。

参考：

- [How to reset index in a pandas dataframe?](https://stackoverflow.com/questions/20490274/how-to-reset-index-in-a-pandas-dataframe)

## 获取索引为 list

在[Get row-index values of Pandas DataFrame as list? [duplicate]](https://stackoverflow.com/questions/18358938/get-row-index-values-of-pandas-dataframe-as-list)找到了答案：

```
df.index.values.tolist() #ndarray
list(df.index.values)
```

##

参考：https://www.statology.org/pandas-get-index-of-row/
