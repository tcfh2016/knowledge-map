# [塑型与数据透视表/Reshaping and pivot tables](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html)

## 使用DataFrame透视对象来塑型

数据在很多时候是按照“堆叠”的方式（stacked/record）存储，比如下面这种形式，对于data和variable
列来说它们都有重复的条目：

```
   date       variable     value
0  2000-01-03        A  0.469112
1  2000-01-04        A -0.282863
2  2000-01-05        A -1.509059
3  2000-01-03        B -1.135632
4  2000-01-04        B  1.212112
5  2000-01-05        B -0.173215
6  2000-01-03        C  0.119209
7  2000-01-04        C -1.044236
8  2000-01-05        C -0.861849
9  2000-01-03        D -2.104569
10 2000-01-04        D -0.494929
11 2000-01-05        D  1.071804
```

而DataFrame的`pivot()`可以基于这些数据形成新的视图，这个过程我们可以称为“数据透视”。比
如我们可以将`data列的内容`作为新的index，将`variable列的内容`作为新的columns，将`value
列的内容`作为新的值，可以这么做：

```
pivot = df.pivot(index='date', columns='variable', values='value')
print(pivot)

输出为：
variable           A         B         C         D
date                                              
2000-01-03  0.469112 -1.135632  0.119209 -2.104569
2000-01-04 -0.282863  1.212112 -1.044236 -0.494929
2000-01-05 -1.509059 -0.173215 -0.861849  1.071804
```

如果数据透视形成的新的对象的index/column不是唯一的，那么需要使用`pivot_table()`。比如
下面这些数据，如果我们以A内容作为新的index, C内容作为新的column，D内容作为新的值，那么
将会遇到重复的值，这个时候`pivot()`会报错。

```
     A    B      C  D  E
0  foo  one  small  1  2 # I-1
1  foo  one  large  2  4 # II-2
2  foo  one  large  2  5 # II-2 重复
3  foo  two  small  3  5 # I-3
4  foo  two  small  3  6 # I-3 重复
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9
```

参考：

- [pandas.DataFrame.pivot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot)
- [pandas.pivot_table](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html#pandas.pivot_table)

## 使用stacking/unstacking来塑型

## 使用melt来塑型
