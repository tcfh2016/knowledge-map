# 第二周周记：获取多只股票市盈率

## 一、笔记代码解释

```
import pandas as pd

stock_list = ['贵州茅台', '五粮液', '洋河股份', '泸州老窖', '古井贡酒']
stocks_df = get_all_securities()
stock_code_list = [stocks_df[stocks_df['display_name'] == stock].index.item() for stock in stock_list]

days = pd.date_range(start = '2018-12-05', end = '2019-12-05')
multi_pe_ratio = {}
for i in range(len(stock_list)):
    stock_code = stock_code_list[i]
    stock_name = stock_list[i]
    q = query(valuation.day, valuation.code, valuation.pe_ratio).filter(valuation.code == stock_code)
    pe_ratio = [get_fundamentals(q, date = day).loc[0, 'pe_ratio'] for day in days]
    multi_pe_ratio[stock_name] = pe_ratio

df = pd.DataFrame(multi_pe_ratio)
df.index = days
df.plot(figsize = (20, 10))
```

效果图如下：

![]()

**代码片段一：**

```
import pandas as pd

stock_list = ['贵州茅台', '五粮液', '洋河股份', '泸州老窖', '古井贡酒']
stocks_df = get_all_securities()
stock_code_list = [stocks_df[stocks_df['display_name'] == stock].index.item() for stock in stock_list]
```

上面这部分代码在[上周的周记](xxx)已经讲过，简而言之第一句是Python编程里面的准备工作，把程序里需要使用的模块包含进来；剩下的部分是将股票名称转换为对应的股票代码，因为聚宽提供的服务函数只接收股票代码。


**代码片段二：**

```
days = pd.date_range(start = '2018-12-05', end = '2019-12-05')
multi_pe_ratio = {}
for i in range(len(stock_list)):
    stock_code = stock_code_list[i]
    stock_name = stock_list[i]
    q = query(valuation.day, valuation.code, valuation.pe_ratio).filter(valuation.code == stock_code)
    pe_ratio = [get_fundamentals(q, date = day).loc[0, 'pe_ratio'] for day in days]
    multi_pe_ratio[stock_name] = pe_ratio
```

代码里面有关字典`multi_pe_ratio`的存在和上周周记里面的一样，是为了把不同的股票市盈率按照股票名称作为键值保存下来，这样便于之后直接通过字典来创建DataFrame。剩下的部分有两个地方需要详解：1，query对象；2，get_fundamentals函数。

1.query对象

要认识query对象先必须要认识SQLAlchemy ORM，因为query对象是SQLAlchemy ORM的操作对象，但是在这之前必须要先将SQLAlchemy ORM拆分为两段进行解释：



参考：

- [Constructing Database Queries with SQLAlchemy](https://hackersandslackers.com/database-queries-sqlalchemy-orm/)
- [The Query Object](https://docs.sqlalchemy.org/en/13/orm/query.html#the-query-object)

2.get_fundamentals函数



**代码片段三：**

```
df = pd.DataFrame(multi_pe_ratio)
df.index = days
df.plot(figsize = (20, 10))
```

## 二、上周遗留问题

### 1.如何处理获取多只股票行情数据时返回的经过"堆叠"的DataFrame（stacked data）

> 上周提到的使用`get_price()`时传入股票列表所返回的Pandas中的三维数据类型Panel在Pandas 0.20.0之后就过时了，所以不建议继续使用。在调用该函数的时候也可以直接设定`panel=Fase`，这个时候获取到的结果也是DataFrame，但我们需要将其进行进一步处理来满足需求，这个主题我会在下周学习。


当我们设定`panel=True`的时候，通过指定索引返回结果的坐标轴0的索引close即`p[close]`我们可以得到多只股票对应的收盘价，如下：

```
p = get_price(stock_code_list, start_date, end_date, 'daily', 'close', panel=True)
p['close']

# 输出：

```

但当我们设定`panel=False`的时候这个时候它返回的结果是DataFrame的类型，然而可以看到这些
数据是以`code`列堆叠形成的：

```
p = get_price(stock_code_list, start_date, end_date, 'daily', 'close', panel=False)
```

### 2.Pandas中的pivot table

> 宽友 @jqz1226 在[《再谈获取多只股票的市盈率—极速版》](https://www.joinquant.com/view/community/detail/24517)改进过我另外一篇[价值研究笔记之获取多只股票的市盈率](https://www.joinquant.com/view/community/detail/97ac84a17f7e9da63be455ac8df30971)，迭代出两个新的版本，其中使用到了新的`get_fundamentals_continuously()`, `get_valuation`以及Padans的数据透视表，这些都是我还没有学习到的内容，因此将进一步学习。


## 三、本周学习到的知识点

### 1.什么是SQLAlchemy ？以及它与query对象的关系

SQLAlchemy 是一个用来支持Python与数据库之间进行交互的工具包，它包括两个部分：SQLAlchemy ORM 和SQLAlchemy Core。



参考：

- [SQLAlchemy Overview](https://docs.sqlalchemy.org/en/13/intro.html)


### 1.Pandas中的Panel类型[Panel](https://pandas.pydata.org/pandas-docs/version/0.24/reference/panel.html)简介

在Pandas的数据类型中`Series`是一维的，`DataFrame`是二维的，即数据表的形式，而`Panel`则是一种三维的数据类型。这种三维的数据类型使用3个坐标轴来支持数据的索引：

- items，坐标轴0，每个条目对应不同的DataFrame。
- major_axis，坐标轴1，每个条目对应DataFrame的行（index）。
- minor_axis，坐标轴2，每个条目对应DataFrame的列（column）。

它同时提供一些列的方法来帮助操作数据，但这种类型从Pandas 0.25.0版本之后已经被正式移除，所以不再进一步学习和关注。

### 2.聚宽服务函数`get_fundamentals_continuously()`, `get_valuation`


### 3.基金数据的获取

## 下周主题

### 1.比较基金数据

### 2.


## 参考文档

- [Panel(面板)数据结构](https://www.cnblogs.com/JeremyTin/p/5324536.html)
- [Panel](https://pandas.pydata.org/pandas-docs/version/0.24/reference/panel.html)
- [Reshaping and pivot tables](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html)
