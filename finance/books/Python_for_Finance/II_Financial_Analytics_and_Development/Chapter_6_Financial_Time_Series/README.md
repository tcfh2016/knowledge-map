## Chapter 6. Financial Time Series

金融领域最主要的数据之一是时间序列，Python里的pandas库，由Wes McKinney开发。本章主要介
绍pandas的基本使用方法、如何处理web, csv数据,以及高频次数据。

### pandas Basics

pandas是基于NumPy，因此NumPy的很多通用函数都可以应用在pandas对象上。

#### 1.First Steps with DataFrame Class

DataFrame 用来管理基于索引和标签的数据，它与SQL数据表和电子表格稍有区别。

```
import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])
print(df)            
```

如上代码对应如下输出：

```
λ python pandas_basic_use.py
   numbers
a       10
b       20
c       30
d       40
```

DataFrame按照Data, Labels和Index的方式来组织数据：

- Data，可以使用不同的类型，除了内建类型外，还支持list, tuple, ndarray, and dict。
- Labels，Data按照列进行组织，Label是不同列的标签。
- Index，用于索引每列的数据，可以支持numbers, strings, time几种类型。

相比ndarray，DataFrame在扩充已有对象时能够更便捷。比如，基于如上的代码再为df扩充两列数
据：

```
df['floats'] = (1.5, 2.5, 3.5, 4.5)
df['names1'] = ('Yves', 'Guido', 'Felix', 'Francesc')
df['names2'] = pd.DataFrame(['Yv', 'Gu', 'Fe', 'Fr'],
                            index=['d', 'a', 'b', 'c']) # 添加新的DataFrame对象。
```

在为一个DataFrame对象append数据的时候最好指定对应的index。对于指定的不匹配的index会被
直接忽略，并置为“NaN, Not a Number”，可以通过`how`来指定忽略形式。

```
ms = df.join(pd.DataFrame([1, 4, 9, 16],
                          index=['a', 'b', 'c', 'y'],
                          columns=['squares',]))

     numbers  floats   names1  names2  squares
a       10     1.5      Yves     Gu      1.0
b       20     2.5     Guido     Fe      4.0
c       30     3.5     Felix     Fr      9.0
d       40     4.5  Francesc     Yv      NaN

# 指定忽略形式为"outer"
ms = df.join(pd.DataFrame([1, 4, 9, 16],
                             index=['a', 'b', 'c', 'y'],
                             columns=['squares',]),
                             how='outer')

     numbers  floats    names1 names2  squares
a     10.0     1.5      Yves     Gu      1.0
b     20.0     2.5     Guido     Fe      4.0
c     30.0     3.5     Felix     Fr      9.0
d     40.0     4.5  Francesc     Yv      NaN
y      NaN     NaN       NaN    NaN     16.0
```

#### 2.Second Steps with DataFrame Class

可以使用ndarry对象来初始化DataFrame对象，这种方式非常方便，且pandas仅仅保留一些最基本的
元信息（比如index）。

```
a = np.random.standard_normal((9, 4)).round(6)
df = pd.DataFrame(a)

结果为：

          0         1         2         3
0 -2.132324 -0.005079  0.995203  0.814630
1 -0.817162  1.176926  1.583261  0.603301
2 -0.951167  0.578953  1.251287  0.804324
3 -0.459627 -0.443992 -0.737870 -0.335985
4 -0.337424  0.651669 -0.546803  0.031903
5  0.114778  0.935059 -0.566720  1.837108
6  1.042856  0.147600 -1.041701 -1.170012
7 -0.161261  0.431451  0.233302  1.682637
8 -1.279984  0.774751  0.896305  1.236388
```

注意DataFrame是以列为主来组织数据的，所以 df[2][3]表示的是第2列index为3的数据。可以通
过如下命令简单修改列名：

```
df.columns = ['No1', 'No2', 'No3', 'No4']
```

将行index索引更改为时间：

```
dates = pd.date_range('2015-1-1', periods=9, freq='M')
df.index = dates

得到如下结果：

               No1       No2       No3       No4
2015-01-31 -0.063067  0.607535  0.913365  0.689960
2015-02-28  0.108040 -0.370936 -0.456547 -0.711879
2015-03-31 -0.303201 -0.537440  0.355943  0.390217
2015-04-30 -0.329964  0.252640 -0.328935 -0.078254
2015-05-31  1.526843 -0.569415  0.010653 -0.009302
2015-06-30  0.931575  0.374084 -0.205578  2.435464
2015-07-31  1.634988  1.549978  0.760149  1.589570
2015-08-31  0.929297 -0.598846  1.017537 -1.398676
2015-09-30 -0.916506 -0.046066  1.123438 -0.658056
```

#### 3.Basic Analytics

和NumPy类似，pandas DataFrame类也提供了许多内建的函数，比如你能够很方便的求取某列的sum,
mean, cumulative sum，并且可以调用`describe()`来得到常见的统计数据。

最为奇妙的是使用DataFrame只需要一行代码就可以绘制取统计图形，当然还需要附加一行`plt.show()`
来显示图形。

```
df.cumsum().plot(lw=2.0)
```

#### 4.Series Class

DataFrame里面的每一列以Series 类型进行组织，因此可以将适用于DataFrame类的方法应用自Series
对象上：

```
df['No1'].cumsum().plot(style='r', lw=2.)
plt.xlabel('date')
plt.ylabel('value')
```

#### 5.GroupBy Operations

pandas提供了类似SQL分组或者Excel里面数据透视（pivot）的功能，比如我们添加一列，然后根据
这列里面的值进行分组，我们甚至可以根据多列数据进行分组：

```
# 单列分组
df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
groups = df.groupby('Quarter')
print(groups.mean())
print(groups.max())

# 多列分组
df['Odd_Even'] = ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even',
                           'Odd', 'Even', 'Odd']
groups = df.groupby(['Quarter', 'Odd_Even'])
print(groups.size())
```

### Financial Data

诸如google, yahoo的公司免费提供了一些金融数据，通过pandas我们能够很好地从web上获取它们。
pandas当前支持的数据源有：

- Yahoo! Finance (yahoo)
- Google Finance (google)
- St. Louis FED (fred)
- Kenneth French’s data library (famafrench)
- World Bank (via pandas.io.wb)

比如我们可以从yahoo上获取德国DAX指数：

```
import pandas.io.data as web

DAX = web.DataReader(name='^GDAXI', data_source='yahoo',
                              start='2000-1-1')
         DAX.info()
```

尝试教材中多种获取方式，均未成功，失败原因为链接不稳定，以及网络超时等。

### Regression Analysis

普通最小二乘法回归的例子。原始文件部分显示如下：

```
Price Indices - EURO Currency
Date    ;Blue-Chip;Blue-Chip;Broad    ; Broad   ;Ex UK    ;Ex Euro Zone;Blue-Chip; Broad
        ;  Europe ;Euro-Zone;Europe   ;Euro-Zone;         ;            ; Nordic  ; Nordic
        ;  SX5P   ;  SX5E   ;SXXP     ;SXXE     ; SXXF    ;    SXXA    ;    DK5F ; DKXF
31.12.1986;775.00 ;  900.82 ;   82.76 ;   98.58 ;   98.06 ;   69.06 ;  645.26  ;  65.56
01.01.1987;775.00 ;  900.82 ;   82.76 ;   98.58 ;   98.06 ;   69.06 ;  645.26  ;  65.56
......
```

对于原始文件需要进行一些格式上的处理：

```
import numpy as np
import pandas as pd

lines = open('./data/es.txt', 'r').readlines()
lines = [line.replace(' ', '') for line in lines]

# 新建一个文件，并且将原始文件第4行进行完善写入新文件。  
new_file = open('./data/es50.txt', 'w')
new_file.writelines('date' + lines[3][:-1] + ';DEL' + lines[3][-1])

# 将原始文件从第5行开始余下行转写入新的文件。
new_file.writelines(lines[4:])             
new_file.close()

es = pd.read_csv('./data/es50.txt', index_col=0, parse_dates=True, sep=';', dayfirst=True)
del es[DEL]
```

上面的这些处理过程可以通过更为简单的接口调用完成：

```
cols = ['SX5P', 'SX5E', 'SXXP', 'SXXE', 'SXXF', 'SXXA', 'DK5F', 'DKXF']
es = pd.read_csv(es_url, index_col=0, parse_dates=True, sep=';', dayfirst=True,       
                 header=None, skiprows=4, names=cols)
```

### High-Frequency Data

一个处理高频数据的例子：分析苹果某周的交易数据。

```
import numpy as np
import pandas as pd
import datetime as dt
from urllib import urlretrieve

url1 = 'http://hopey.netfonds.no/posdump.php?'
url2 = 'date=%s%s%s&paper=AAPL.O&csv_format=csv'
url = url1 + url2

year = '2014'
month = '09'
days = ['22', '23', '24', '25']

AAPL = pd.DataFrame()
for day in days:
  AAPL = AAPL.append(pd.read_csv(url % (year, month, day), index_col=0, header=0, parse_dates=True))
AAPL.columns = ['bid', 'bdepth', 'bdeptht', 'offer', 'odepth', 'odeptht']

AAPL['bid'].plot()
```

### Conclusions

pandas 是处理金融交易数据非常方便的工具，你或许可以使用NumPy/matplotlib完成相同的功能，
但pandas能够更快地完成它。另外，pandas还能够从web上直接获取交易数据。
