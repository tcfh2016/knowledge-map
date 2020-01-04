# 聚宽学习第三周周记：财务数据中的市盈率和市净率

## 一、市盈率和市净率的理解

### 1.市盈率

市盈率也称“PE”、“股价收益比率”或“市价盈利比率”，由股价除以每股收益得出，也可用公司市值除以净利润得出。由于市值/股价每个交易日都在改变，所以市盈率也在变化。

根据计算时候分母的不同，市盈率本身也有许多版本，比如LYR市盈率、TTM市盈率、动态市盈率。LYR市盈率就是静态市盈率，TTM市盈率是当下的市盈率，动态市盈率又有两种情况，一种是年化市盈率、一种是预期市盈率：

- LYR市盈率=当前总市值/上一年度净利润
- TTM市盈率=当前总市值/最近 4 个季度的净利润总额
- 年化市盈率=当前总市值/当前报告期年化净利润 （180409 注：可能季报，可能半年报。）
- 预期市盈率=当前总市值/当年预测净利润

使用市盈率进行估值有它合理的地方，也有他不合理的地方，我经常使用这个指标来发现、排除、选择企业。并不是说这种方法一定好，只是觉得适合自己，毕竟亏过钱，加上比较认同格雷厄姆的证券投资理念，行事倾向于稳妥。

### 2.市净率

市净率也称“PB”，由股价（Price）除以每股净资产（Book Value）得出，也可用公司股票市值除以公司净资产。当市净率小于1时也就是所谓的“破净股”，目前国内市场上破净股在银行、钢铁行业比较多。

我进入证券市场的四年多偏爱破净股，在对钢铁企业股票的持有当中逐渐意识到其中的一些不足，比如钢铁属于重资产企业，企业的资产基本都属于固定资产，固定资产所带来的继续投入和维护以及折旧对于企业来说都是一项极大的挑战，尤其在整个行业处于周期低估的时候。另外，这个指标对于互联网等新兴技术性的以轻资产经营的企业来说不是很合适。


## 二、`同时获取单只股票市盈率、市净率和股价`代码解释

原版代码2019年12月19日发布在社区的[《价值研究笔记之单只股票市盈率、市净率和股价变化》](https://www.joinquant.com/view/community/detail/f268c17f91e89040d0ca012f9d07d549)。

```
import pandas as pd
from jqdata import *

stock = '中国建筑'
stocks_df = get_all_securities()
stock_code = stocks_df[stocks_df['display_name'] == stock].index.item()


start_date = '2012-12-05'
end_date = '2019-12-05'
df = get_price(stock_code, start_date, end_date, 'daily', 'close', skip_paused=True)
df.columns = ['股价']

days = get_trade_days(start_date, end_date)
q = query(valuation.day, valuation.code, valuation.pe_ratio, valuation.pb_ratio).filter(valuation.code == stock_code)
pe = [get_fundamentals(q, date = day).loc[0, 'pe_ratio'] for day in days]
pb = [get_fundamentals(q, date = day).loc[0, 'pb_ratio'] for day in days]

df['市盈率'] = pe
df['市净率'] = pb
df.plot(figsize=(20, 10), secondary_y=['股价'], title = '市盈率、市净率与股价走势')
```

效果图如下：

![]()

**代码片段一：**

```
import pandas as pd
from jqdata import *

stock = '中国建筑'
stocks_df = get_all_securities()
stock_code = stocks_df[stocks_df['display_name'] == stock].index.item()
```

这段代码在前面两周的周记（[周记一](https://www.joinquant.com/view/community/detail/4298dffa265ff07fd52aa2dbcd9fe577)和[周记二](https://www.joinquant.com/view/community/detail/3cc22ef4218363686917d718ba90f4f8)里面都有解释，这里不再重复说明了，唯一需要提示的是这段代码里面多了一句`from jqdata import *`，其原因在于我们要使用聚宽服务中的`get_trade_days()`。

那为什么我们之前使用的聚宽服务函数`get_price()`和`get_fundamentals()`都没有包含这条语句，同为聚宽服务函数的`get_trade_days()`就需要平添这句import语句？我的理解是聚宽平台提供的服务函数有很多种，有一些比较通用，另一些则是专用的，它们放置在不同的模块中，比如`jqdata`。在聚宽研究/策略环境启动时会默认导入一些聚宽服务函数，但默认并不导入所有相关的服务函数，这是设计上的考虑。我们要使用的`get_trade_days()`恰好就放置在`jqdata`模块里，所以需要另外导入，至于这个函数什么意思在后面说。

**代码片段二：**

```
start_date = '2012-12-05'
end_date = '2019-12-05'
df = get_price(stock_code, start_date, end_date, 'daily', 'close', skip_paused=True)
df.columns = ['股价']
```

指定起始日期和结束日期，然后调用`get_price()`获取这段时间内的股价，`daily`表示按天为单位，需要注意的是这个函数会自动过滤非交易日（周末），API文档里面提到了“该函数默认不跳过停牌, 未上市或者退市后的日期”，注意这些日期是不包括周末的。比如你可以在策略平台上做如下测试：

```
df = get_price(stock_code, '2019-12-23', '2019-12-29', 'daily', 'close', skip_paused=False)

输出不包含周末非交易日，如下：

close
2019-12-23  84.29
2019-12-24  84.46
2019-12-25  83.93
2019-12-26  84.43
2019-12-27  84.72
```

**代码片段三：**

```
days = get_trade_days(start_date, end_date)
q = query(valuation.day, valuation.code, valuation.pe_ratio, valuation.pb_ratio).filter(valuation.code == stock_code)
pe = [get_fundamentals(q, date = day).loc[0, 'pe_ratio'] for day in days]
pb = [get_fundamentals(q, date = day).loc[0, 'pb_ratio'] for day in days]
```

首先是调用jqdata里面定义的`get_trade_days()`获取指定日期内的所有交易日，这个函数会自动去除起止日期和结束日期中间的非交易日。然后，我们创建query()对象，再调用`get_fundamentals()`获取每天的市盈率，这两个知识点我们在[周记二](https://www.joinquant.com/view/community/detail/3cc22ef4218363686917d718ba90f4f8)已经详细讲过了，并且这部分代码有两个优化点：

- 创建query对象的时候我们可以仅仅指定`valuation.pe_ratio`和`valuation.pb_ratio`，因为我们仅对市盈率和市净率感兴趣。
- 我们可以使用`get_valuation()`来获取市盈率数据，甚至可以省略掉query对象的创建。

优化后的代码只需要下面一行，有关市盈率和市净率的数据都可以从调用`get_valuation()`结果里面获取。

```
valuation_df = get_valuation(stock_code, start_date, end_date, fields=['pe_ratio', 'pb_ratio'])
```

**代码片段四：**

```
df['市盈率'] = pe
df['市净率'] = pb
df.plot(figsize=(20, 10), secondary_y=['股价'], title = '市盈率、市净率与股价走势')
```

最后这部分的很好理解，就是将市盈率和市净率的列拼接到之前已经包含有股价的DataFrame里，以方便最后的绘图函数调用。

## 三、上周计划任务

### 1.比较基金数据

>尝试对获取到的基金数据进行整理，大致思路是获取到市场上一段时间内所有ETF基金的净值数据，从中选出表现最优异的三只ETF基金。目前基金数据的整理可能不是难点，难点在于如何根据`基金单位净值`和`基金累计净值`去评判一直基金的好坏。

该任务已经完成，简单笔记见[价值研究笔记之获取处于历史地位TOP10的ETF基金](https://www.joinquant.com/view/community/detail/b7f2d084d39662b0b21295fe4db25211)，这个过程中花了好几个小时弄清楚`基金单位净值`和`基金累计净值`的区别，按照基本的定义：

- 单位净值是当前的交易价格，对应当前时间点的净值，可能随着基金的拆分而变更。
- 累计净值表示基金从成立到现在获取的回报总计，累计净值 = 单位净值 + 历史上每单位基金分红。

按照如上的理解，理论上“累计净值”一定大于“单位净值”，为通过聚宽获取基金历史净值时发现`基金累计净值`的累计净值有时候大于，有时候小于`基金单位净值`，比如159901。

之后翻看159901的公告才发现，原来基金份额不仅可以拆分还可以进行合并，所以存在回报相同，但单位净值可能因为折算拆分/合并小于或者大于累计净值的情况。也就是此时的累计净值的算法依据的是最初发行的基金份额，而没有随着基金的拆分/折算而变化（有待进一步求证）。


### 2.开始了解聚宽因子

>虽然我当前主要是从价值投资的角度来分析股票，对于量化投资并未开始涉猎。但本周逛社区的时候，看到宽友建议先了解下因子，我看了下相关的学习链接，发现内容不少，只能先逐步投入时间了解，但估计目前不会太深入学习，时间不够用呀。

本周还没有开始学习。

## 四、本周新学知识

暂无。

## 五、下周预定主题

### 1.使用聚宽策略来模拟基金定投的效果

今天有人在元旦那天发布的[新年ETF基金定投计划](https://www.joinquant.com/view/community/detail/10c029abcd8f69bd59b8b1172a547d31)留言提到了使用聚宽策略来进行模拟的话题，这刚好是接触使用策略的机会，不妨试试看。

### 2.开始了解聚宽因子
