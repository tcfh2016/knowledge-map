## 财务指标

财务指标的数据，存放在`indicator`表中。可以可以使用get_fundamentals() 的statDate参数查询年度数据。

比如查询营业收入增长率（`inc_revenue_year_on_year`）。

```
from jqdata import *

df = get_fundamentals(query(
        indicator.code, indicator.inc_revenue_year_on_year
    ), statDate=year)
```

## 参考

- [财务指标数据](https://www.joinquant.com/help/api/help#Stock:%E8%B4%A2%E5%8A%A1%E6%8C%87%E6%A0%87%E6%95%B0%E6%8D%AE)