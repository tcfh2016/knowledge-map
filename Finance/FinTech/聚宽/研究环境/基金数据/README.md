## 基金信息：`get_all_securities(['fund'])`

获取基金的基本数据，和股票一样，都需要使用`get_all_securities()`，只不过传入的参数是`fund`。

```
- display_name # 中文名称
- name # 缩写简称
- start_date # 上市日期
- end_date # 退市日期，如果没有退市则为2200-01-01
- type # 类型， etf(ETF基金)，fja（分级A），fjb（分级B）,fjm(分级母基金），lof(场内交易开发基金），mmf(场内交易货币基金）
```

如果要获取ETF的信息，那么需要进一步筛选`df[df['type'] == 'etf']`，其实也可以直接通过`get_all_securities('etf')`来达到目的。


## 获取单只基金信息：`get_security_info(code)`

得到对象的属性都具有如上的display_name, namme, start_date, end_date, type等。


## 累计净值、单位净值

```
get_extras(info, security_list, start_date='2015-01-01', end_date='2015-12-31', df=True,count=None):
```

其中的`info`参数选择 [‘acc_net_value’, ‘unit_net_value’] 中的一个。


## 参考

- [基金累计单位净值](https://www.joinquant.com/help/api/help#fund:%E5%9F%BA%E9%87%91%E7%B4%AF%E8%AE%A1%E5%8D%95%E4%BD%8D%E5%87%80%E5%80%BC)
