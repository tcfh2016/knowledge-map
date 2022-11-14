## 股票信息

获取单支股票的信息使用`get_security_info(code)`，这个`code`可以是单个股票的代码，也可以是基金的代码。返回值是一个类型为`jqdata.models.security.Security`的对象，包含了如下属性：

```
display_name # 中文名称
name # 缩写简称
start_date # 上市日期, [datetime.date] 类型
end_date # 退市日期， [datetime.date] 类型, 如果没有退市则为2200-01-01
type # 类型，stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），fjb（分级B）
parent # 分级基金的母基金代码
```

如果要查看市场上所有股票的信息，那么需要使用`get_all_securities(types=['stock'], date=None)`，这个时候返回的是一个`DataFrame`类型，包含多只股票的数据。当然，也可以传入不同的`types`来确认是股票还是基金数据。
