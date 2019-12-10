import pandas as pd

#############################################################################
# 先获取股票名称对应的股票代码
#############################################################################
stock_name = '洋河股份'

# 查询指定股票名称对应的股票代码，用来调用其他函数获取数据
stocks_df = get_all_securities()
stock_code = stocks_df[stocks_df['display_name'] == stock_name].index.item()

#############################################################################
# 获取财务数据中的市值数据（valuation），其中包含有 pe_ratio
# https://www.joinquant.com/help/api/help?name=Stock#%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE%E5%88%97%E8%A1%A8
#############################################################################
q = query(valuation.day, valuation.code, valuation.pe_ratio).filter(valuation.code == stock_code)

days = pd.date_range(start = '2018-12-05', end = '2019-12-05')
pe_ratio = [get_fundamentals(q, date = day).loc[0, 'pe_ratio'] for day in days]
df = pd.DataFrame(pe_ratio)
df.plot(figsize=(20, 10))
