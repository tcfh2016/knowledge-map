## 利润数据

使用`get_fundamentals()`从`income`这张表里面查询数据，基本字段：

- `code`
- `statDate`
- `total_operating_revenue`：营业总收入
- `operating_profit`：营业利润
- `total_profit`：利润总额
- `net_profit`：净利润


```
# 获取多只股票在某一日期的市值, 利润
df = get_fundamentals(query(
        valuation, income
    ).filter(
        # 这里不能使用 in 操作, 要使用in_()函数
        valuation.code.in_(['000001.XSHE', '600000.XSHG'])
    ), date='2015-10-15')
```


参考：

- [利润数据](https://www.joinquant.com/help/api/help#Stock:%E5%88%A9%E6%B6%A6%E6%95%B0%E6%8D%AE)
- [获取单季度/年度财务数据](https://www.joinquant.com/help/api/help#Stock:%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)