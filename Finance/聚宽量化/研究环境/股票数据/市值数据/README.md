## 估值数据

聚宽提供了`valuation`的数据表，该数据表包含了股本、市值、市盈率、市净率、市销率、市现率等数据，可以有多种获取方式。

- pe_ratio 市盈率(PE, TTM)
- pe_ratio_lyr 市盈率(PE)
- pb_ratio 市净率(PB)
- ps_ratio 市销率(PS, TTM)
- pcf_ratio 市现率(PCF, 现金净流量TTM)

- code 股票代码
- turnover_ratio 换手率(%)
- capitalization 总股本(万股)
- market_cap 总市值(亿元)


## get_valuation

这个函数用来获取多个标的在指定交易日范围内的市值表数据，在`jqdata`模块里面实现，所以必须`from jqdata import *`。

```
from jqdata import *

get_valuation(security, start_date=None, end_date=None, fields=None, count=None)
```


## get_fundamentals

```
get_fundamentals(query_object, date=None, statDate=None)
```

date和statDate参数只能传入一个:

- 传入date时, 查询指定日期date所能看到的最近(对市值表来说, 最近一天, 对其他表来说, 最近一个季度)的数据, 我们会查找上市公司在这个日期之前(包括此日期)发布的数据, 不会有未来函数。格式为'2015-10-15'。
- 传入statDate时, 查询statDate指定的季度或者年份的财务数据。季度为‘2015q1’，年份为‘2015’。

```
from jqdata import *


# 获取多只股票在某一日期的市值, 利润
df = get_fundamentals(query(
        valuation, income
    ).filter(
        # 这里不能使用 in 操作, 要使用in_()函数
        valuation.code.in_(['000001.XSHE', '600000.XSHG'])
    ), date='2015-10-15')
```


## 本地数据：get_valuation

本地数据可以通过`get_valuation()`来获取

```
from jqdatasdk import *

get_valuation(security, start_date=None, end_date=None, fields=None, count=None)
```


## 参考

- [市值数据](https://www.joinquant.com/help/api/help#Stock:%E5%B8%82%E5%80%BC%E6%95%B0%E6%8D%AE)
- [数据获取函数](https://www.joinquant.com/help/api/help#api:%E6%95%B0%E6%8D%AE%E8%8E%B7%E5%8F%96%E5%87%BD%E6%95%B0)
- [本地数据：获取多个标的在指定交易日范围内的市值表数据](https://www.joinquant.com/help/api/doc?name=JQDatadoc&id=10325&keyword=get_valuation)

## 获取多天的市盈率

基于如上的理解，为了获取一段交易时间内所有交易日的市盈率，必须通过创建时间序列，并将其传入get_fundamentals()函数。

对于如何创建时间序列，在研究环境给定的新手教程《Pandas库使用示例》里面有个例子：

```
dates = pd.date_range('20130101',periods=6) # 从20130101开始的6天时间序列
```

从中可知pandas的`date_range`方法可以用来完成这项功能，查找资料发现geeksforgeeks的介绍更靠谱：

```
Syntax: pandas.date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs)

pd.date_range(start ='1-1-2018', end ='1-05-2018', freq ='5H') # H, 5H...
pd.date_range(start ='1-1-2018', end ='8-01-2018', freq ='D') # D, 5D...
pd.date_range(start ='1-1-2018', end ='8-01-2018', freq ='M') # M, 5M...
pd.date_range(start ='1-1-2018', periods = 13)
```

参考：

- [获取单季度/年度财务数据](https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)
- [Query对象的简单使用教程](https://www.joinquant.com/view/community/detail/16411)
- [Querying](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying)
- [Python | pandas.date_range() method](https://www.geeksforgeeks.org/python-pandas-date_range-method/)
