## 估值数据

聚宽提供了`valuation`的数据表，该数据表包含了股本、市值、市盈率、市净率、市销率、市现率等数据，可以有多种获取方式。


## get_valuation

这个函数用来获取多个标的在指定交易日范围内的市值表数据，在`jqdata`模块里面实现，所以必须`from jqdata import *`。

```
from jqdata import *

get_valuation(security, start_date=None, end_date=None, fields=None, count=None)
```


## get_fundamentals



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