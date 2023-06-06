## 使用query

使用query必须使用`from jqdata import *`，因为query对象定义在里面。


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
