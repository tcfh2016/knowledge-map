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
start_date = '2018-12-05'
end_date = '2019-12-05'

start_date = '2018-12-05'
end_date = '2019-12-05'
multi_stock_price = get_price(stock_code_list, start_date, end_date, 'daily', 'close', panel=True)
multi_stock_price['close'].columns = stock_list
multi_stock_price['close'].plot(figsize = (20, 10), secondary_y = ['贵州茅台'], title = '股价走势对比')

'''
# old version

multi_stock_price = {}
for i in range(len(stock_list)):
    stock_code = stock_code_list[i]
    stock_name = stock_list[i]
    stock_price = get_price(stock_code, start_date, end_date, 'daily', 'close')
    multi_stock_price[stock_name] = stock_price['close']

df = pd.DataFrame(multi_stock_price)
df.plot(figsize = (20, 10))
'''
#print ((valuations))
