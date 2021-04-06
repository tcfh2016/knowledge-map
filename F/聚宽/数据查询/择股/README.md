今天突然想到，在第一趋势上能够很快地通过条件过滤出股票，那么在聚宽上如何操作？尽管在第一
趋势上能够完成对应的工作，但那得来简单有些时候反倒缺少了一些将人带入更深层次的“准备工作”，
在聚宽上通过手动获取，在编写代码、阅读反馈结果在进行下一步操作，这一系列过程能够将人的思
考维系住。

# 获得当前市盈率小于10的所有普通股

可以根据在[获取单季度/年度财务数据]里面给出的如下例子进行修改：

```
# 选出所有的总市值大于1000亿元, 市盈率小于10, 营业总收入大于200亿元的股票
 df = get_fundamentals(query(
         valuation.code, valuation.market_cap, valuation.pe_ratio, income.total_operating_revenue
     ).filter(
         valuation.market_cap > 1000,
         valuation.pe_ratio < 10,
         income.total_operating_revenue > 2e10
     ).order_by(
         # 按市值降序排列
         valuation.market_cap.desc()
     ).limit(
         # 最多返回100个
         100
     ), date='2015-10-15')
```

修改分两步：创建Query对象，再调用get_fundamentals函数：

```
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

df = get_fundamentals(q, date='2019-12-16')
```


参考：

- [获取单季度/年度财务数据](https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)
