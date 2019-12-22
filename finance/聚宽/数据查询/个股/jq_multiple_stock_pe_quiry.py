import pandas as pd

#############################################################################
# 先获取股票名称对应的股票代码
#############################################################################
stock_list = ['贵州茅台', '五粮液', '洋河股份', '泸州老窖', '古井贡酒']

# 查询指定股票名称对应的股票代码，用来调用其他函数获取数据
stocks_df = get_all_securities()
stock_code_list = [stocks_df[stocks_df['display_name'] == stock].index.item() for stock in stock_list]
#print(stock_code_list)

#############################################################################
# 获取财务数据中的市值数据（valuation），其中包含有 pe_ratio
# https://www.joinquant.com/help/api/help?name=Stock#%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE%E5%88%97%E8%A1%A8
#############################################################################
days = pd.date_range(start = '2018-12-05', end = '2019-12-05')
multi_pe_ratio = {}
for i in range(len(stock_list)):
    stock_code = stock_code_list[i]
    stock_name = stock_list[i]
    q = query(valuation.day, valuation.code, valuation.pe_ratio).filter(valuation.code == stock_code)
    pe_ratio = [get_fundamentals(q, date = day).loc[0, 'pe_ratio'] for day in days]
    multi_pe_ratio[stock_name] = pe_ratio

df = pd.DataFrame(multi_pe_ratio)
df.index = days
df.plot(figsize = (20, 10))

#print ((valuations))
