# 《巴菲特的护城河》：
# - 总资产收益率 > 5%
# - 净资产收益率 > 15%
#
# 参考：[获取单季度/年度财务数据](https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)

import pandas as pd
import datetime as dt

def get_stock_name(stock_code):
    stocks_df = get_all_securities()
    stock_name = [stocks_df.loc[c, 'display_name'] for c in stock_code]
    return stock_name


#pd.set_option('display.max_columns', 100)
#pd.set_option('display.max_rows', 100)

# 1. 创建query对象，这是聚宽所规定的调用get_fundamentals()时必须传入的参数
init_filter_query = query(
                            indicator.code, indicator.inc_revenue_year_on_year
                        ).filter(
                            indicator.inc_revenue_year_on_year > 5
                        ).order_by(
                            indicator.inc_revenue_year_on_year.desc()
                        ).limit(
                            100
                        )

# 2. 调用 get_fundamentals()获取满足条件的股票, 获取股票列表
year = dt.datetime.today().year - 1
df = get_fundamentals(init_filter_query, statDate=year)
#print(df)
stocks = df['code']
#print(stocks)

# 3 获取这些股票历年的inc_revenue_year_on_year数据
multi_stock_data_query = query(
                                indicator.code, indicator.inc_revenue_year_on_year
                            ).filter(
                                indicator.code.in_(stocks)
                            )

year_list = list(range(year, -1 ,year - 8))
inc_revenue_dict = {}
for year in year_list:
    df = get_fundamentals(multi_stock_data_query, statDate=year)
    df = df.set_index('code')
    inc_revenue_dict[year] = df['inc_revenue_year_on_year']


df = pd.DataFrame(inc_revenue_dict)
df.index = get_stock_name(df.index)
print(df)
#print(df['2018'].sort_values(ascending=False))
