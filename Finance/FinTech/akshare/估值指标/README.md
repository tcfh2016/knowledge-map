## A股市值和市盈率

使用百度提供的接口`stock_zh_valuation_baidu`，但一次只能够获得 {"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"}中的一个指标。

```
import akshare as ak

stock_zh_valuation_baidu_df = ak.stock_zh_valuation_baidu(symbol="002044", indicator="总市值", period="近一年")
print(stock_zh_valuation_baidu_df)
```

如果要同时获得多个指标，那么就需要多次获取在拼接起来：

```
indicator_dfs = []
for ind in ['总市值', '市盈率(TTM)']:
    df = ak.stock_zh_valuation_baidu(symbol='002044', indicator=ind, period='近一年')
    df = df.set_index('date').rename(columns={'value':ind})
    indicator_dfs.append(df)

pd.concat(indicator_dfs, axis=1)
```

## 港股市值和市盈率

港股的估值指标要使用百度网的`stock_hk_valuation_baidu`，也只能一次只能获取到"港股", "市盈率", "市净率", "股息率", "ROE", "市值"中的一个指标，包含所有历史数据：

```
stock_hk_valuation_baidu_df = ak.stock_hk_valuation_baidu(symbol="02358", indicator="总市值", period="近一年")
print(stock_hk_valuation_baidu_df)
```

获取多个需要拼接：

```
indicator_dfs = []
for ind in ['总市值', '市盈率(TTM)']:
    df = ak.stock_hk_valuation_baidu(symbol='02358', indicator=ind, period='近一年')
    df = df.set_index('date').rename(columns={'value':ind})
    indicator_dfs.append(df)

pd.concat(indicator_dfs, axis=1)
```