# 聚宽学习第三周周记：财务数据中的市盈率和市净率

## 一、市盈率和市净率的理解

### 1.市盈率

### 2.市净率

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

## 四、本周新学知识

## 五、下周预定主题
