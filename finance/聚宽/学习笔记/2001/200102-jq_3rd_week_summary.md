# 聚宽学习第三周周记：财务数据中的市盈率和市净率

## 一、市盈率和市净率的理解

### 1.市盈率

### 2.市净率

## 二、`获取多只股票市盈率`代码解释

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

#############################################################################
# 获取财务数据中的市值数据（valuation），其中包含有 pe_ratio
# https://www.joinquant.com/help/api/help?name=Stock#%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE%E5%88%97%E8%A1%A8
#############################################################################

## 三、上周计划任务

## 四、本周新学知识

## 五、下周预定主题
