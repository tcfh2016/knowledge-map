## 研究环境

聚宽提供的研究环境方便量化爱好者方便在里面进行一些数据的查询和获取，这个“研究环境”和“策略环境”是有区别的。简单来说，“研究环境”里面有一些聚宽平台提供的函数模块，方便你查询证券数据，而“策略环境”则是用来跑你的交易策略的。打个比方，你是拳击爱好者，研究环境相当于“你在家里练习拳击的个人模式”，“策略环境”相当于“你在擂台上比赛的多人模式”。

在研究环境里面进行研究，我们可以很方便的查询一些股票数据，比如：


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
