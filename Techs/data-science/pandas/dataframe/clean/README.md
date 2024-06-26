## 修改行名

直接赋值，如下将DataFrame的index修改为其中的某一列：

```
df.index = df['日期'] # 之前的'日期'列依然存在
df = df.set_index('日期', drop=True) #
```

*注1：DataFrame的set_index函数会将一个或多个列转换为行索引，并创建新的DataFrame。*
*注2：Index 对象是不可修改的。因此df.index[1] = 'c'会提示错误。*

参考：

- [Remove index name in pandas](https://stackoverflow.com/questions/29765548/remove-index-name-in-pandas)


## 修改列名

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

## 增加行列

在某个DataFrame里面添加一列必须使用`[]`操作符，`此时应保证Series和DataFrame具有相同的index`

```
df['numbers'] = series
```


## 删除行列

删除行或者列的时候可以调用`drop()`方法，删除时的`axis`用来指定坐标轴。默认为`axis=0`，删除行标签对应的行（行标签对应的所有列有效），如果设置为`axis=1`则删除列标签对应的列（列标签对应的所有行有效）。

```
df.drop([0,1], axis=0, inplace=True) # 删除index为0，1的行。
df.drop('column name', axis=1) # 指定axis=1说明删除列。
df.drop(['city', 'state'], axis=1) # 删除'city'和'state'两列。
```

删除多个行或者列时只需要将所有行/列以列表的形式传入，比如`df.drop(df[<some boolean condition>].index)`。更高效的方式是`df = df[df.score > 50]`。

另外还有一种方法，是使用`del`。删除列时必须通过索引的方式指定，不能通过属性的方式来指定。

```
del df['newdata']
del df.newdata # 会提示错误。n 
```

按照制定条件删除，比如删除值小于0所在的行？使用:

```
df = df[(df > 0).all(axis=1)]
```

参考：

- [How to delete rows from a pandas DataFrame based on a conditional expression](https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression)



## 修改行、列

修改整列直接通过赋值的方式修改（添加）：

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


## 替换/replace

最基本的替换功能是是使用`replace`函数，该函数并非默认的inplace函数，如果要对原来的dataframe生效，那么需要传入`inplace=True`参数。注意这个时候是全字匹配。

```
# 对特别列进行操作
df['colomn name'].replace(src, tar)

# 对整个dataframe进行操作
df.replace(src, tar)
```

1）Series

使用`Series.replace()`或者`Series.str.replace()`两者来进行替换，前者默认进行全匹配，后者默认进行子串匹配，不过我们可以使用`Series.replace()`里的正则功能，比如如下的代码将名为index的Series的值里包含'(万元)'替换为空。

```
index = index.replace(to_replace='\(万元\)', value=' ', regex=True)
```

*注：`Series.str.replace()`不能添加`inplace=True`。会报“replace() got an unexpected keyword argument 'inplace'”，这是因为使用的不是`pandas.DataFrame.replace()`而是`string.replace`。*

2) DataFrame

对DataFrme也是按照同样操作来进行替换，比如对于某列（对应Series）的操作：

```
df.column_name.str.replace('[', '').replace(']', '') # 将column_name列里的'[]'删除。
df.column_name.str.replace('[\[\]]', '') # 将column_name列里的'[]'删除，使用正则。
```

*注：在pandas里面使用字符串的功能，需要通过添加`.str`来完成字符串函数的调用。*


3）对多列进行替换

如果我现在的需求是将其中的某些项进行整体替换呢？比如对下面的DataFrame数据，我要将其中code列里面的负数项目都替换为0：

```
    code        003816.XSHE  600011.XSHG     ...       600795.XSHG  601991.XSHG
day           
2020-04-22      15.5246      60.4374     ...           21.2415      36.9854
2020-04-23      15.4712      60.7252     ...           21.1363      36.8118
2020-04-24      15.3645      60.1496     ...           21.0312      36.2909
2020-04-27      15.4179      60.4374     ...           21.0312      36.8118
2020-04-28      15.1511      59.4301     ...           20.8209      35.9436
2020-04-29      16.8520      59.5740     ...           20.8209      36.1172
2020-04-30      16.9711      60.7252     ...         -139.6440      29.5116
2020-05-06      17.0306      60.7252     ...         -138.9422      29.5116
2020-05-07      16.9711      62.4520     ...         -138.9422      29.3737
2020-05-08      17.3879      62.0203     ...         -138.9422      29.6495
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


## 按条件替换某列中的部分单元


参考：

- [How to Replace Values in Column Based on Condition in Pandas?](https://www.geeksforgeeks.org/how-to-replace-values-in-column-based-on-condition-in-pandas/)


## 转换某列的类型

使用`.astype(target_type)`来进行。另外可以通过自定义数据转换函数：

```
def close_convert_func(value: str) -> float:

    if "万元" in value:
        new_value = value.replace('万元', '0000')
    else:
        new_value = value.replace('元', '')
    return np.float64(new_value)

temp_df['close'] = temp_df['close'].apply(close_convert_func)
```

## SettingWithCopyWarning



