# 聚宽学习周记十：


## 一、代码解释

这是[聚宽2019年度评选+精选文章合集](https://www.joinquant.com/view/community/detail/5fea4e17fa8ad5eb32b85201375e2669?type=1)的第一篇，选择的是 @Gyro 编写的[价值低波（中）-- 市盈率研究](https://www.joinquant.com/view/community/detail/328831058b45f5f1080914aaea6e0d09)。

其实@Gyro在这篇文章里面已经将代码拆散再讲解了，但是我这里由于学习需要要先将它合拢再重新拆解开学习。

```
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib

# 取得2005-4-8 ~ 2019-3-30 之间的所有的交易日
index = '000300.XSHG'
start_date = dt.date(2005, 4, 8)
end_date = dt.date(2019, 3, 30)
p = get_price(index, start_date, end_date, 'daily', ['close'])

# 建立市场估值
mp = pd.Series([],[])
for d in p.index:
    # 取得股票池
    stocks = get_index_stocks(index, date=d)

    # 基本面过滤
    df = get_fundamentals(query(
        valuation.code,
        valuation.market_cap,
        (valuation.market_cap/valuation.pe_ratio).label('value'),        
    ).filter(
        valuation.code.in_(list(stocks)),
    ), date=d).dropna()
    market_value = df.market_cap.sum()/df.value.sum()
    mp[d]= market_value

# 把估值数据加入表格
p['pv_ratio'] = mp

# 归一化
p['n_price'] = p.close/p.close[0]
p['n_pv_ratio'] = p.pv_ratio/p.pv_ratio[0]

# 对数化
p['ln_price'] = np.log(p.n_price)
p['ln_pv_ratio'] = np.log(p.n_pv_ratio)

from jqdata import finance
q = query(finance.STK_EXCHANGE_TRADE_INFO.exchange_name, \
        finance.STK_EXCHANGE_TRADE_INFO.pe_average,\
        finance.STK_EXCHANGE_TRADE_INFO.date)\
        .filter(finance.STK_EXCHANGE_TRADE_INFO.date=='2019-04-12')

f = finance.run_query(q)
```

**代码片段一：**

```
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib
```

最前面的这几行是Python里面的`import`语句，如果你要使用某些非内建的变量或者函数，那么需要使用该语句将对应的模块导入进来。也就是说，导入/import模块是使用该模块里面变量或者函数的前提。这里面导入的四个模块为:

- numpy: Numberical Python的简称，是Python科学计算的基础模块，提供快速的数组处理能力。
- pandas：基于numpy之上构建，除了具有NumPy高性能的数组计算功能，还具有便捷地处理结构化数据如电子表格、关系型数据库数据的功能。
- datetime：Python用来处理日期和时间的专用模块。
- matplotlib：专门用于绘制数据图表的Python库。


**代码片段一：**

**代码片段一：**

**代码片段一：**

**代码片段一：**

## 二、上周计划任务


## 三、本周新学内容

### 1.如何获取次新股

[聚宽学习第六周周记：选取处于历史地位的ETF基金](https://www.joinquant.com/view/community/detail/45e63a7494ea446eb921b89977389325)

```
trade_days = get_trade_days('2014-01-01', '2019-12-27')
start = trade_days[0]
end = trade_days[-1]
df = etf_funds_df[(etf_funds_df['start_date'] <  start) & (etf_funds_df['end_date'] > end)]
```


## 四、下周学习任务
