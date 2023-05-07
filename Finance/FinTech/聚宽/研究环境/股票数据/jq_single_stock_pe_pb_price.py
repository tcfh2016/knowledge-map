import pandas as pd
from jqdata import *

#############################################################################
# 先获取股票名称对应的股票代码
#############################################################################
stock = '中国建筑'

# 查询指定股票名称对应的股票代码，用来调用其他函数获取数据
stocks_df = get_all_securities()
stock_code = stocks_df[stocks_df['display_name'] == stock].index.item()


#############################################################################
# 获取财务数据中的市值数据（valuation），其中包含有 pe_ratio
# https://www.joinquant.com/help/api/help?name=Stock#%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE%E5%88%97%E8%A1%A8
#############################################################################
start_date = '2012-12-05'
end_date = '2019-12-05'

# 获取股价
df = get_price(stock_code, start_date, end_date, 'daily', 'close', skip_paused=True)
df.columns = ['股价']
print(len(df.index))


# 获取市盈率、市净率
days = get_trade_days(start_date, end_date)
q = query(valuation.day, valuation.code, valuation.pe_ratio, valuation.pb_ratio).filter(valuation.code == stock_code)
pe = [get_fundamentals(q, date = day).loc[0, 'pe_ratio'] for day in days]
pb = [get_fundamentals(q, date = day).loc[0, 'pb_ratio'] for day in days]

print(len(pe))
print(len(pb))
df['市盈率'] = pe
df['市净率'] = pb

df.plot(figsize=(20, 10), secondary_y=['股价'], title = '市盈率、市净率与股价走势')
