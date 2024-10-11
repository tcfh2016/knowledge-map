# 修改


## 修改列名

```
df.columns = ['price'] # 用等长的列表来覆盖之前的列名
df.rename(columns=lambda x:x.replace('$',''), inplace=True)
df.rename(columns={'a':'b'}, inplace=True) # 将'a'重命名为'b'，可以支持多列的重命名。
```


## 修改值

1）直接赋值

修改整列直接通过赋值的方式修改（添加），将列表或数组赋值给某列时，其长度必须跟DataFrame的长度匹配：

```
df['numbers'] = 1.0

val = Series([-1, -2, -3, -4], index=['b', 'a', 'c', 'd'])
df['newdata'] = val
```


## 替换/replace

1）全替换、部分替换

最基本的替换功能是是使用`replace`函数，该函数并非默认的inplace函数，如果要对原来的dataframe生效，那么需要传入`inplace=True`参数。注意这个时候是全字匹配。

```
# 对特别列进行操作
df['colomn name'].replace(src, tar)

# 对整个dataframe进行操作
df.replace(src, tar)

# 使用字典来定义需要修改的映射关系，然后使用`replace()`或者`map()`：
di = {0: "A", 2: "B"}
df.replace({"col1": di})
df['col1'].replace(di, inplace=True)
df['col1'].map(di)
```

如果要实现“部分文本匹配”，可以在pandas里面使用字符串的功能，需要通过添加`.str`来完成字符串函数的调用：

```
df.column_name.str.replace('[', '').replace(']', '') # 将column_name列里的'[]'删除。
df.column_name.str.replace('[\[\]]', '') # 将column_name列里的'[]'删除，使用正则。

index = index.replace(to_replace='\(万元\)', value=' ', regex=True)
```


*注：`Series.str.replace()`不能添加`inplace=True`。会报“replace() got an unexpected keyword argument 'inplace'”，这是因为使用的不是`pandas.DataFrame.replace()`而是`string.replace`。*


2）自定义替换

如果我现在的需求是将其中的某些项进行整体替换呢？比如对下面的DataFrame数据，我要将其中code列里面的负数项目都替换为0：

```
    code        003816.XSHE  600011.XSHG     ...       600795.XSHG  601991.XSHG
day           
2020-04-22      15.5246      60.4374     ...           21.2415      36.9854
2020-04-23      15.4712      60.7252     ...           21.1363      36.8118
2020-04-24      15.3645      60.1496     ...           21.0312      36.2909
2020-04-27      15.4179      60.4374     ...           21.0312      36.8118
```

一种方法是遍历每列数据，然后对其中的每个值应用map函数进行替换：

```
def func(value):
    if value < 0:
        return 0
    else:
        return value

for column in pivot.columns:
    pivot[column] = list(map(func, pivot[column]))
```

但最简单的方案却是`pivot[pivot < 0] = 0`。

参考：

- [Update pandas DataFrame with .str.replace() vs .replace()](https://stackoverflow.com/questions/38117016/update-pandas-dataframe-with-str-replace-vs-replace)
- [pandas.Series.replace](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.replace.html)
- [pandas.Series.str](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.html#pandas.Series.str)
- [How to replace negative numbers in Pandas Data Frame by zero](https://stackoverflow.com/questions/27759084/)how-to-replace-negative-numbers-in-pandas-data-frame-by-zero)
- [How to replace a value in pandas, with NaN?](https://stackoverflow.com/questions/29247712/how-to-replace-a-value-in-pandas-with-nan)
- [How to use the replace() method with keyword arguments to replace empty strings](https://stackoverflow.com/questions/50843263/how-to-use-the-replace-method-with-keyword-arguments-to-replace-empty-strings)
- [How to Replace Values in Column Based on Condition in Pandas?](https://www.geeksforgeeks.org/how-to-replace-values-in-column-based-on-condition-in-pandas/)



## 使用`apply()`：

```
def square(x):
   return x ** 2

df.col1 = df.col1.apply(square)
```

参考：

- [Remap values in pandas column with a dict, preserve NaNs](https://stackoverflow.com/questions/20250771/remap-values-in-pandas-column-with-a-dict-preserve-nans)
- [How to Replace Values on Specific Columns in Pandas](https://saturncloud.io/blog/how-to-replace-values-on-specific-columns-in-pandas/)


# 组合

## 合并：`df.merge()`

类似数据库中的`join`操作，是将两个df在“行的方向”上进行合并，合并的时候要指定相同的参考索引。

```
df.merge(right, on=None, how='inner', left_index=False, right_index=False)
```

- `on=[col]`：指定合并时参考列
- `how=left`：左连接，默认并集
- `left_index=True`：让df保持所有行列数据


## 连接：`pd.concat`

```
pandas.concat(objs, axis=0, join='outer', ignore_index=False)
```

使用`pd.concat()`函数来完成多个DataFrame的连接操作，主要的参数为`axis`, `join`和`ignore_index`：

- `axis`决定在纵向（`axis=0`）还是横向（`axis=1`）连接, 默认为纵向连接。
- `join`决定连接时候的方式，`join='inner'`表示内部合并，`outer`表示外部合并，默认为外部合并。
- `ignore_index`确定是否需要重排合并之后的DataFrame。


这里对于`axis`的理解需要辨析一下，也就是要能够快速的反映出`axis=0/1`的含义。当`axis=0`指定的是“X轴”，相当于是“不同行以X轴进行纵向连接”，当`axis=1`指定的是`Y轴`，相当于是“不同列以Y轴进行横向连接”。

理解清楚两者之间的差别之后，就能够理解`join`参数通常是在`axis=0`既以X轴进行纵向连接的时候使用，横向连接因为轴是纵轴，通常是相等的，所以不需要。

### 纵向连接

比如我有下面三个DataFrame数据，怎么把它们在列的方向上进行连接：

```
    a   b   c
0  91  45  18
1  67  73   4
    a   b   c
0  56  70  37
1  92  34  68
    a   b   c
0  33  91   7
1  40  38  37
```

执行`pd.concat([df1, df2, df3])`之后的结果为（如果不需要保留之前的index，只需要设置`ignore_index=True`即可）：

```
a	b	c
0	91	45	18
1	67	73	4
0	56	70	37
1	92	34	68
0	33	91	7
1	40	38	37
```


## 横向连接

同样，使用`pd.concat()`也可以进行横向连接，此时需要将`axis`参数设置为`1`。横向连接之后列的数量会增加，

```
pd.concat([df1, df2], axis=1)
```


# 转换

## 类型转换

pandas会根据输入的数据来确定每个列的数据类型，比如一列的数据全是int，那么该列的类型就是int，哪怕其中的一个为float，那么该列为float。可以通过`print(df.dtypes)`打印DataFrame各列的类型。

将特定列进行类型转换：

```
# convert column "a" to int64 dtype and "b" to complex type
df = df.astype({"a": int, "b": complex})
```

想将整个 DataFrame的值转换为float类型进行计算，尝试`pd.to_numeric(m)`发现只能够转换单维的数据。如果要转换所有列，那么需要使用循环，然而这种方式会返回新的对象，不是在原对象基础上进行转换，使用起来不方便。

*注：调用`to_numeric()`时根据原有数据决定转换为`int64`还是`float64`。*

```
for col in float_df:
    print(pd.to_numeric(float_df[col]))
```

另外可以通过自定义数据转换函数：

```
def close_convert_func(value: str) -> float:
    if "万元" in value:
        new_value = value.replace('万元', '0000')
    else:
        new_value = value.replace('元', '')
    return np.float64(new_value)

temp_df['close'] = temp_df['close'].apply(close_convert_func)
```

参考：

- [Change column type in pandas](https://stackoverflow.com/questions/15891038/change-column-type-in-pandas)


## 一列转换为多列：`split()`和`join()`

```
# expand参数代表分割后是否转换为DataFrame，默认False
series = df['地址'].str.split(' ', expand = Ture)
df['省'] = series[0]
df['市'] = series[1]
df['区'] = series[2]

# 与join()结合
df = df.join(df['地址'].str.split(' ', expand = Ture))
```


## 行列转换

用pandas处理数据时，经常需要对行列进行转换或重拍，主要使用stack, unstack和pivot方法：

- `df.stack(level=-1, dropna=True)`：将原来的列索引转换为内层的行索引
- `df.unstack(level=-1, fill_value=None)`：stack的逆操作
- `df.pivot(index=None, columns=None, values=None)`：指定行、列、和值


## DataFrame转换为字典

```
DataFrame.to_dict(orient='dict', *, into=<class 'dict'>, index=True)
```

`orient`常用的选项：

- `dict`默认项，转换为` {column -> {index -> value}}`
- `list`，转换为` {column -> [values]}`
- `records`，转换为`[{column -> value}, … , {column -> value}]`


参考：

- [pandas.DataFrame.to_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html)