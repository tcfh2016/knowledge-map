## 财务数据

财务数据的参考文档在[这里](https://www.joinquant.com/help/api/help#Stock:%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)，查询接口是`get_fundamentals()`：

```
get_fundamentals(query_object, date=None, statDate=None)
```


财务指标的数据，存放在`indicator`表中。可以可以使用get_fundamentals() 的statDate参数查询年度数据。

比如查询营业收入增长率（`inc_revenue_year_on_year`）。

```
from jqdata import *

df = get_fundamentals(query(
        indicator.code, indicator.inc_revenue_year_on_year
    ), statDate=year)
```

参考

- [财务指标数据](https://www.joinquant.com/help/api/help#Stock:%E8%B4%A2%E5%8A%A1%E6%8C%87%E6%A0%87%E6%95%B0%E6%8D%AE)


## 资产负债表

```
q = query(
        balance.cash_equivalents,
        cash_flow.goods_sale_and_service_render_cash
    ).filter(
        income.code == '000001.XSHE',
    )

ret = get_fundamentals(q, statDate='2014')
```

## 利润数据

使用`get_fundamentals()`从`income`这张表里面查询数据，基本字段：

- `code`
- `statDate`
- `total_operating_revenue`：营业总收入
- `operating_profit`：营业利润
- `total_profit`：利润总额
- `net_profit`：净利润

选择单个股票的使用`valuation.code == '000001.XSHE'`，多个的时候使用`valuation.code.in_(['000001.XSHE', '600000.XSHG'])`。

```
# 获取多只股票在某一日期的市值, 利润
df = get_fundamentals(query(
        valuation, income
    ).filter(
        # 这里不能使用 in 操作, 要使用in_()函数
        valuation.code.in_(['000001.XSHE', '600000.XSHG'])
    ), date='2015-10-15')
```

## 获得季度利润

```
# 查询平安银行2014年四个季度的季报, 放到数组中
q = query(
        income.statDate,
        income.code,
        income.basic_eps,
        balance.cash_equivalents,
        cash_flow.goods_sale_and_service_render_cash
    ).filter(
        income.code == '000001.XSHE',
    )

rets = [get_fundamentals(q, statDate='2014q'+str(i)) for i in range(1, 5)]
```


参考：

- [利润数据](https://www.joinquant.com/help/api/help#Stock:%E5%88%A9%E6%B6%A6%E6%95%B0%E6%8D%AE)
- [获取单季度/年度财务数据](https://www.joinquant.com/help/api/help#Stock:%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)