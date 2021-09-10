## 数据结构

Pandas的两个主要数据结构为 Series 和 DataFrame，它们为大多数应用提供了一种可靠的、易于
使用的基础。

- [数据结构](./datastructure/README.md)

## 绘图

- [绘图](./plot/README.md)

## 其他

- [csv处理](./csv/README.md)
- [web相关](./web/README.md)


# 学习材料

- [10 Minutes to pandas](http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
- [Data School](https://www.youtube.com/channel/UCnVzApLJE2ljPZSeQylSEyg)

# 常用属性及函数

## 属性

- DataFrame.shape ：显示行、列信息。
- DataFrame.dtypes ：显示行的类型。

## 方法

- DataFrame.head() ：默认显示前面5行的数据。
- DataFrame.describe() ：显示对应数据对应里面“数据列”的统计信息，包括count, min, max...
- DataFrame.describe(include=['object']) ：显示非数据列的统计信息，包括count, uniq, top, freq

# 常见问题


# NaN (Not a Number) 处理

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
print(s.dropna()) # 删除含有NaN的全部行
print(s.dropna(axis=1)) # 删除含有NaN的全部行
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

## 一、排序

1.如何将如下的数据按照时间顺序颠倒过来？

```
   code         day  pe_ratio  pb_ratio
0  601318.XSHG  2019-12-27    9.8284    2.4153
1  601318.XSHG  2019-12-26    9.7948    2.4071
2  601318.XSHG  2019-12-25    9.7368    2.3928
3  601318.XSHG  2019-12-24    9.7982    2.4079
4  601318.XSHG  2019-12-23    9.7785    2.4031
```

DataFrame提供了`sort_index()`和`sort_value`分别按照索引和值排序：

```
df1 = frame.sort_values(axis=0, by="clumn_name",ascending=False)
```

2.`rank()`

参考：

- [关于pandas的rank()函数的一点认识](https://zhuanlan.zhihu.com/p/87593543)


## 三、遍历

1.简单遍历

对于Series, Dataframe的遍历操作如下：

```
for c in ufo.city:
  print(c)

for index, row in ufo.interrows():
  print(index, row.City, row.State) # 打印City, State

```

2.通过多列的值来进行行选取操作

比如如下数据，我要将“所有列内容都小于某个值”的那些行删除掉，改如何操作？

```
                               002352     600233
报告日期
货币资金(万元)               1613112.0   406144.0
结算备付金(万元)                   0.0        0.0
拆出资金(万元)                     0.0        0.0
交易性金融资产(万元)               1444.0       79.0
衍生金融资产(万元)                  0.0        0.0
```

学习了DataSchool的一个视频，知道通过条件选择的原理来自于构建一个bolean的Series，因此可以
对这两列的内容进行求与操作来构建这样的series：

```
filter_condition = [True] * len(self.balance_df[0]['2018-12-31'])
for i in range(len(self.args.stock)):
    s = self.args.stock[i]
    self.multi_stocks_asset_df[s] = self.balance_df[i]['2018-12-31']
    filter_condition &= self.multi_stocks_asset_df[s] > 0

df_for_plot = self.multi_stocks_asset_df[filter_condition]
```

学习了另外一个视频之后，才知道通过多列来进行选择需要使用`&`或者`|`将条件进行逻辑计算，即
便如此，如要根据多列（事前未知）来进行选取依然需要使用如上代码实例里的方式。

```
df_for_plot = self.multi_stocks_asset_df[condition1 & condition2]
```

而对于单列多条件的选取，可以使用简便的方式:

```
movies[(movies.genre=='Crime') | (movies.genre=='Drama') | (movies.genre=='Action')]
movies[movies.genre.isin(['Crime', 'Drama', 'Action'])]
```

参考：

- [How do I filter rows of a pandas DataFrame by column value?](https://www.youtube.com/watch?v=2AFGPdNn4FM)
- [How do I apply multiple filter criteria to a pandas DataFrame?](https://www.youtube.com/watch?v=YPItfQ87qjM)


## 四、展现

1.变更某一列内容的展现形式

比如现在有一列"日期"是按照“年-月-日”的形式展示的，现在需要让其展现为“年-月”的形式展示，
该如何操作？

```
df['month_year'] = df['date_column'].dt.to_period('M')
```

参考：

- [Extracting just Month and Year from Pandas Datetime column](https://stackoverflow.com/questions/25146121/extracting-just-month-and-year-from-pandas-datetime-column)
- [Series.dt ](http://pandas.pydata.org/pandas-docs/stable/reference/series.html#api-series-dt)


2.输出排版

打印DataFrame输出的格式有些时候并不友好，比如：

![](print_not_aligned.png)


3.DataFrame.plot 时中文显示乱码

![](./basics/plot_chinese_messycode.png)

解决方法为通过`plt.rcParams['font.sans-serif'] = ['SimHei'] `将字体设置为黑体。

参考：

- [python3用matplotlib绘图出现中文乱码的问题](https://www.cnblogs.com/Icarus-suixin/p/10641085.html)

4.print的时候如何显示更多列或者行？

```
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
```

5.print的时候数值太大无法全部展示？

比如下面的time，其实暗含了日期和时间，但是由于是float格式默认按照科学计数法显示了，如何
将其全部显示出来？

```
           time  current   high    low       volume         money
0  2.020021e+13    1.987  2.022  1.965  338313044.0  6.753016e+08
0  2.020022e+13    2.071  2.071  2.004  689679516.0  1.411302e+09
0  2.020022e+13    2.090  2.090  2.050  704272926.0  1.461049e+09
0  2.020022e+13    2.054  2.087  2.052  572403776.0  1.184645e+09
```

可以通过`pd.set_option('display.float_format', lambda x: '%.2f' % x)`取消默认的科学
计数法，另外可以通过`pd.set_option(‘precision’, n)`显示小数点。

参考：

- [How do I expand the output display to see more columns of a pandas DataFrame?](https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe)

## 五、其他

1.DataFrame 类型转换

想将整个 DataFrame的值转换为float类型进行计算，尝试`pd.to_numeric(m)`发现只能够转换单
维的数据。如果要转换所有列，那么需要使用循环，然而这种方式会返回新的对象，不是在原对象基
础上进行转换，使用起来不方便。

*注：调用`to_numeric()`时根据原有数据决定转换为`int64`还是`float64`。*

```
for col in float_df:    
    print(pd.to_numeric(float_df[col]))
```

通过`print(df.dtypes)`打印DataFrame各列的类型。

2.pandas.io.data 不可用

从0.19.0开始，pandas不再支持pandas.io.data or pandas.io.wb, 替代品为pandas_datareader。

参考：

- [Importing pandas.io.data(https://stackoverflow.com/questions/47972667/importing-pandas-io-data)
- [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/#)

3.将index转换为list

```
list(obj.index.values)
```

参考：

- [Get row-index values of Pandas DataFrame as list?](https://stackoverflow.com/questions/18358938/get-row-index-values-of-pandas-dataframe-as-list)
