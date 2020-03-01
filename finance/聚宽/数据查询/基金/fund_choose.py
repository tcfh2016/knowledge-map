from jqdata import *
import pandas as pd

#############################################################################
# 参考：获取基金数据官方文档：https://www.joinquant.com/help/api/help?name=fund
#
# 其中：
#    acc_net_value: 基金累计净值
#    unit_net_value: 基金单位净值
#############################################################################
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

# 获取当前市场上所有的etf基金
all_etf = get_all_securities(['etf'])

# 过滤自2014-01-01前发行，并且截止2020-02-12依然在交易的基金
trade_days = get_trade_days('2014-01-01', '2020-02-27')
start = trade_days[0]
end = trade_days[-1]
df = all_etf[(all_etf['start_date'] < start) & (all_etf['end_date'] > end)]

# 获取这些基金在选定期间的累积净值
acc_value_df = get_extras('acc_net_value', df.index, start_date='2010-01-01', end_date=end, df=True)
#print(acc_value_df)

# 使用最近一个交易日的当前累计净值除以近6年最高累计净值，作为衡量未来涨幅空间的判断指标
curr_div_max = acc_value_df.loc[end] / acc_value_df.describe().loc['max']

# 获取TOP100的基金代码
sorted_value = curr_div_max.sort_values(ascending=True)
fund_name = [get_security_info(stock_code).display_name for stock_code in sorted_value.index]

df = pd.DataFrame(sorted_value, columns=['code'])
df['name'] = fund_name
print(df)

#fund_ticks = get_ticks(list(sorted_df.index.values), end_dt='2020-02-11 15:30:00', start_dt='2020-02-11 09:00:00', fields=['money'])
#print(type(fund_ticks))
#df = pd.DataFrame(fund_ticks)
#print(df)

# 将基金代码转换为基金中文名称
#top100_fund_name = [get_security_info(stock_code).display_name for stock_code in sorted_df.index]
#print(top100_fund_name)
