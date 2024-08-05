## 类型转换

pandas会根据输入的数据来确定每个列的数据类型，比如一列的数据全是int，那么该列的类型就是int，哪怕其中的一个为float，那么该列为float。

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

通过`print(df.dtypes)`打印DataFrame各列的类型。


参考：

- [Change column type in pandas](https://stackoverflow.com/questions/15891038/change-column-type-in-pandas)

## 重命名

1）修改行名

直接赋值，如下将DataFrame的index修改为其中的某一列：

```
df.index = df['日期'] # 之前的'日期'列依然存在
df = df.set_index('日期', drop=True) #
```

*注1：DataFrame的set_index函数会将一个或多个列转换为行索引，并创建新的DataFrame。*
*注2：Index 对象是不可修改的。因此df.index[1] = 'c'会提示错误。*

参考：

- [Remove index name in pandas](https://stackoverflow.com/questions/29765548/remove-index-name-in-pandas)


2）修改列名

两种方式：直接赋值和调用 rename方法：

```
df.columns = ['price'] # 用等长的列表来覆盖之前的列名
df.rename(columns=lambda x:x.replace('$',''), inplace=True)
df.rename(columns={'a':'b'}, inplace=True) # 将'a'重命名为'b'，可以支持多列的重命名。
```

另外在read_csv()的时候可以修改读取数据的列名：

```
ufo = pd.read_csv(name_file, names=ufo_cols, header=0) # 不指定header，直接使用自
定义ufo_cols作为列名。
```


## 修改值



## 合并操作

使用`pd.concat()`函数来完成多个DataFrame的连接操作，主要的参数为`axis`, `join`和`ignore_index`：

- `axis`决定在纵向（`axis=0`）还是横向（`axis=1`）连接, 默认为纵向连接。
- `join`决定连接时候的方式，`join='inner'`表示内部合并，`outer`表示外部合并，默认为外部合并。
- `ignore_index`确定是否需要重排合并之后的DataFrame。


这里对于`axis`的理解需要辨析一下，也就是要能够快速的反映出`axis=0/1`的含义。当`axis=0`指定的是“X轴”，相当于是“不同行以X轴进行纵向连接”，当`axis=1`指定的是`Y轴`，相当于是“不同列以Y轴进行横向连接”。

理解清楚两者之间的差别之后，就能够理解`join`参数通常是在`axis=0`既以X轴进行纵向连接的时候使用，横向连接因为轴是纵轴，通常是相等的，所以不需要。

## 纵向连接

```
pd.concat([df3, df4], axis=0, join='inner', ignore_index=True)
```

比如我有下面三个DataFrame数据，怎么把它们合并在一起：

```
# 2010年
total_operating_revenue  total_operating_cost  total_profit  np_parent_company_owners
0              444756672.0           216138608.0   217983440.0               163337936.0

# 2011年
   total_operating_revenue  total_operating_cost  total_profit  np_parent_company_owners
0              504532160.0           223844592.0   297411680.0               222218576.0

# 2012年
   total_operating_revenue  total_operating_cost  total_profit  np_parent_company_owners
0              586157056.0           286812384.0   341199296.0               256545872.0
```

上面这种方式的“合并”实际上是需要在列的方向上进行连接，可以使用`concat()`函数。由于每个DataFrame的行标签都是“0”，所以需要在连接之前或者连接之后进行更改。

## 横向连接

同样，使用`pd.concat()`也可以进行横向连接，此时需要将`axis`参数设置为`1`。横向连接之后列的数量会增加，

```
pd.concat([df1, df2], axis=1)
```


## pd.merge()，类似数据库中的`join`操作

怎样在行方向上进行合并：

使用`pd.merge(df1, df2, on=['column'])`。


## 怎样往已有DataFrame里面添加一行？

```
df.loc[len(df.index)] = ['Amy', 89, 93] 

# 先构造Series
s = pd.Series(['new2', 2, 2], index=df.columns)
df_new = df.append(s, ignore_index=True)
```

- [How to add one row in an existing Pandas DataFrame?](https://www.geeksforgeeks.org/how-to-add-one-row-in-an-existing-pandas-dataframe/)