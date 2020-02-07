# 聚宽学习第六周周记：基金的净值概念和网格交易

## 一、`获取处于历史地位的ETF基金`代码解释

原版代码见[价值研究笔记之获取处于历史地位TOP10的ETF基金](https://www.joinquant.com/view/community/detail/b7f2d084d39662b0b21295fe4db25211)。在这之前必须要先弄清楚与评价基金收益的两个基本概念：“基金单位净值”和“基金累积净值”，因为这两个概念花了我好几个小时的时间去弄清楚，好在问题搞多了习惯了坚持，总算把它弄明白了。


明白了“基金累积净值”我们就好理解下面的代码了，因为下面的代码使用的核心变量就“累积净值”这一个。如下是代码解释部分。

```
all_funds_df = get_all_securities(['fund'])
etf_funds_df = all_funds_df[all_funds_df['type'] == 'etf']

trade_days = get_trade_days('2014-01-01', '2019-12-27')
start = trade_days[0]
end = trade_days[-1]
df = etf_funds_df[(etf_funds_df['start_date'] < start) & (etf_funds_df['end_date'] > end)]

acc_value_df = get_extras('acc_net_value', df.index, start_date=start, end_date=end, df=True)
curr_div_max = acc_value_df.loc[end] / acc_value_df.describe().loc['max']


top10_fund_code = curr_div_max.sort_values(ascending=True).index[0:10]
print(top10_fund_code)
top10_fund_name = [get_security_info(stock_code).display_name for stock_code in top10_fund_code]
print(top10_fund_name)
```

**代码片段一：**

```
all_funds_df = get_all_securities(['fund'])
etf_funds_df = all_funds_df[all_funds_df['type'] == 'etf']
```

获取所有基金数据。

**代码片段二：**

```
trade_days = get_trade_days('2014-01-01', '2019-12-27')
start = trade_days[0]
end = trade_days[-1]
df = etf_funds_df[(etf_funds_df['start_date'] < start) & (etf_funds_df['end_date'] > end)]
```

过滤自2014-01-01前发行，并且截止2019-12-27依然在交易的基金。

**代码片段三：**

```
acc_value_df = get_extras('acc_net_value', df.index, start_date=start, end_date=end, df=True)
curr_div_max = acc_value_df.loc[end] / acc_value_df.describe().loc['max']
```

获取这些基金在选定期间的累积净值，使用最近一个交易日的当前累计净值除以近6年最高累计净值，作为衡量未来涨幅空间的判断指标。

**代码片段四：**

```
top10_fund_code = curr_div_max.sort_values(ascending=True).index[0:10]
print(top10_fund_code)
top10_fund_name = [get_security_info(stock_code).display_name for stock_code in top10_fund_code]
print(top10_fund_name)
```

获取TOP10的基金代码，并将基金代码转换为基金中文名称。

## 二、本周新学知识

### 1.什么是网格交易？

 @odbo
网格交易


## 三、下周预定主题
