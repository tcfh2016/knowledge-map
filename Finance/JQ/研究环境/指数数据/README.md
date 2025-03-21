## [指数信息](https://www.joinquant.com/help/api/help#Stock:%E8%8E%B7%E5%8F%96%E6%B2%AA%E6%B7%B1%E6%8C%87%E6%95%B0%E6%95%B0%E6%8D%AE)

获取指数信息也是使用与获取股票信息、基金信息相同的函数`get_security_info(code)`，获取到对象的属性包括：

```
display_name # 中文名称
name # 缩写简称
start_date # 上市日期, [datetime.date] 类型
end_date # 退市日期，[datetime.date] 类型, 如果没有退市则为2200-01-01
type # 类型，index(指数)
```

## [指数成分股](https://www.joinquant.com/help/api/help#index:%E8%8E%B7%E5%8F%96%E6%8C%87%E6%95%B0%E6%88%90%E4%BB%BD%E8%82%A1)

```
get_index_stocks(index_symbol, date=None)
```

举例，用`get_index_stocks('000300.XSHG')`获取所有沪深300的股票。使用`get_index_stocks('399971.XSHE', '2024-04-03')`获取中证传媒指数在2024年4月3日的成分股。