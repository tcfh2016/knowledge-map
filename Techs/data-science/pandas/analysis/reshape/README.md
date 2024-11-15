# 行列转换/塑形

用pandas处理数据时，经常需要对行列进行转换或重排，主要使用stack, unstack和pivot方法：

- `df.stack(level=-1, dropna=True)`/`df.unstack(level=-1, fill_value=None)`：将列、行索引互相转换
- `df.pivot(index=None, columns=None, values=None)`：将某列的值分散到一个或多个类别

一点思考：

1. 有时候一个数据表包含有很多列的数据，而数据透视能够更好地比较三列之间的关系。因此可以将两列分别对应到行、列、和值这样的三维关系。
2. 但对于数据可视化而言，输入的数据大多只需要两列，所以很多时候要将多列的数据堆叠为单列（`stack()`/`melt()`），以便将所有需要可视化的数据整理称两列。


## 使用透视对象来塑型

1）`pivot()`

数据在很多时候是按照“堆叠”的方式（stacked/record）存储，比如下面这种形式，对于`date`和`variable`列来说它们都有重复的数据：

```
   date       variable     value
0  2000-01-03        A  0.469112
1  2000-01-04        A -0.282863
2  2000-01-05        A -1.509059
3  2000-01-03        B -1.135632
```

而DataFrame的`pivot()`可以基于这些数据形成新的视图，这个过程我们可以称为“数据透视”。比如我们可以将`date列的内容`作为新的index，将`variable列的内容`作为新的columns，将`value列的内容`作为新的值，可以这么做：

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


2）`pivot_table()`

如果数据透视形成的新的对象的index/column不是唯一的，那么需要使用`pivot_table()`，需要指定聚合函数，默认`aggfunc=mean`。

```
pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=<no_default>, sort=True)
```

比如下面这些数据，如果我们以A内容作为新的index, C内容作为新的column，D内容作为新的值，那么将会遇到重复的值，这个时候`pivot()`会报错。

```
     A    B      C  D  E
0  foo  one  small  1  2 # I-1
1  foo  one  large  2  4 # II-2
2  foo  one  large  2  5 # II-2 重复
3  foo  two  small  3  5 # I-3
4  foo  two  small  3  6 # I-3 重复
5  bar  one  large  4  6
```

对于`aggfunc`其他可选的还有`sum`, `min`, `max`。但这些是基于数值类型的，如果要统计次数，可以使用`size`（使用`count`对于超过3列的dataframe会多出更多的统计项）。


参考：

- [pandas.DataFrame.pivot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot)
- [pandas.pivot_table](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html#pandas.pivot_table)


## 使用stacking/unstacking来塑型

与`pivot()`相关的两个函数是Series和DataFrame都支持的`stack()/unstack()`，它们主要用来支持MultiIndex。

1.`stack()`：将列标签"压缩"为行标签。

如果列标签只有单一的index，那么压缩为Series。如果列标签是MultiIndex，那么压缩为DataFrame。你也可以选择压缩哪个level，那么这个level列标签堆叠为当前DataFrame的MultiIndex。

比如：

```
                     A         B
first second
bar   one     0.721555 -0.706771
      two    -1.039575  0.271860
baz   one    -0.424972  0.567020
      two     0.276232 -1.087401

如上DataFrame由MultiIndex索引，A, B属于同一level的列标签，在stack之后这一level的所有列全部被压缩/stack为MultiIndex的新的level做为last level（之前的last level是second,现是一个未命名的last level）。

first  second
bar    one     A    0.721555
               B   -0.706771
       two     A   -1.039575
               B    0.271860
baz    one     A   -0.424972
               B    0.567020
       two     A    0.276232
               B   -1.087401
```


2.`unstack()`：将行标签（默认last level）透视为列标签，你可以选择将MultiIndex中的哪一层进行透视，可以填写下表（比如0，1..），也可以是名称（比如'first', 'second'...）。

比如：

```
将如上stack之后的DataFrame的MultiIndex的第0层进行unstack：unstack(0)/unstack('first')：

first          bar       baz
second
one    A  0.721555 -0.424972
       B -0.706771  0.567020
two    A -1.039575  0.276232
       B  0.271860 -1.087401
```


## 使用melt来塑型

```
DataFrame.melt(id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)
```

`melt()`将DataFrame从“宽格式”转换为“长格式”，有点类似数据透视的逆操作，将列变成行。

`id_vars`指定标记符对应的列。而`value_vars`对应那些要逆透视的那些列，这些列的值会合并到同一列。



## 参考：

- [塑型与数据透视表/Reshaping and pivot tables](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html)