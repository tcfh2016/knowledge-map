# 1.获取满足条件的股票数据，条件按照参考文档中的示例：
# - 总市值 > 1000 亿
# - 市盈率 < 10
# - 营业收入 > 200 亿
#
# 参考：[获取单季度/年度财务数据](https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)

# 1.1 创建query对象，这是聚宽所规定的调用get_fundamentals()时必须传入的参数
q = query(
        valuation.code, valuation.market_cap, valuation.pe_ratio, income.total_operating_revenue
    ).filter(
        valuation.market_cap > 1000,
        valuation.pe_ratio < 10,
        income.total_operating_revenue > 2e10
    ).order_by(
        valuation.market_cap.desc()
    ).limit(
        100
    )
# 1.2 调用 get_fundamentals()获取满足条件的股票
df = get_fundamentals(q, date='2019-12-16')

# 2. 由于返回的结果是包含有多行多列信息的 DataFrame结构，其中的'code'列是满足条件的股票代码，因为我像看到股票名称，所以需要再
# 将其转换为名称
stock_code = df['code']
stocks_df = get_all_securities()
stock_name = [stocks_df.loc[c, 'display_name'] for c in stock_code]
print (stock_name)
