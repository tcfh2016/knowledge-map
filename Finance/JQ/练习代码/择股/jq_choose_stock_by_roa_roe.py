# 《巴菲特的护城河》：
# - 总资产收益率 > 5%
# - 净资产收益率 > 15%
#
# 参考：[获取单季度/年度财务数据](https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)

import pandas as pd

def get_stock_name(stock_code):
    stocks_df = get_all_securities()
    stock_name = [stocks_df.loc[c, 'display_name'] for c in stock_code]
    return stock_name


#pd.set_option('display.max_columns', 100)
#pd.set_option('display.max_rows', 100)

# 1.1 创建query对象，这是聚宽所规定的调用get_fundamentals()时必须传入的参数
init_filter_query = query(
                            valuation.pe_ratio, indicator.code, indicator.roe, indicator.roa,
                        ).filter(
                            indicator.roa > 5,
                            indicator.roe > 10,
                            valuation.pe_ratio > 0,
                            #income.total_operating_revenue <= 2e10,
                            income.total_operating_revenue > 1e10
                        ).order_by(
                            indicator.roe.desc()
                        ).limit(
                            100
                        )

# 1.2 调用 get_fundamentals()获取满足条件的股票, 获取股票列表
df = get_fundamentals(init_filter_query, statDate='2018')
#print(df)
stocks = df['code']
#print(stocks)

# 1.3 获取这些股票历年的roe/roa数据
multi_stock_data_query = query(
                                valuation.pe_ratio, indicator.code, indicator.roe, indicator.roa,
                            ).filter(
                                indicator.code.in_(stocks)
                            )

roe_dict = {}
roa_dict = {}
year_list = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
for year in year_list:
    df = get_fundamentals(multi_stock_data_query, statDate=year)
    df = df.set_index('code')
    roe_dict[year] = df['roe']
    roa_dict[year] = df['roa']

roe_df = pd.DataFrame(roe_dict)
roe_df.index = get_stock_name(roe_df.index)
print(roe_df['2018'].sort_values(ascending=False))

roa_df = pd.DataFrame(roa_dict)
roa_df.index = get_stock_name(roa_df.index)
print(roa_df['2018'].sort_values(ascending=False))


# 2. 由于返回的结果是包含有多行多列信息的 DataFrame结构，其中的'code'列是满足条件的股票代码，因为我像看到股票名称，所以需要再
# 将其转换为名称
#stock_code = df['code']
#stocks_df = get_all_securities()
#stock_name = [stocks_df.loc[c, 'display_name'] for c in stock_code]
#print (stock_name)
