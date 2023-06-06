## 获取多天的市盈率

基于如上的理解，为了获取一段交易时间内所有交易日的市盈率，必须通过创建时间序列，并将其传入get_fundamentals()函数。

对于如何创建时间序列，在研究环境给定的新手教程《Pandas库使用示例》里面有个例子：

```
dates = pd.date_range('20130101',periods=6) # 从20130101开始的6天时间序列
```

从中可知pandas的`date_range`方法可以用来完成这项功能，查找资料发现geeksforgeeks的介绍更靠谱：

```
Syntax: pandas.date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs)

pd.date_range(start ='1-1-2018', end ='1-05-2018', freq ='5H') # H, 5H...
pd.date_range(start ='1-1-2018', end ='8-01-2018', freq ='D') # D, 5D...
pd.date_range(start ='1-1-2018', end ='8-01-2018', freq ='M') # M, 5M...
pd.date_range(start ='1-1-2018', periods = 13)
```

参考：

- [获取单季度/年度财务数据](https://www.joinquant.com/help/api/help?name=Stock#%E8%8E%B7%E5%8F%96%E5%8D%95%E5%AD%A3%E5%BA%A6%E5%B9%B4%E5%BA%A6%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE)
- [Query对象的简单使用教程](https://www.joinquant.com/view/community/detail/16411)
- [Querying](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying)
- [Python | pandas.date_range() method](https://www.geeksforgeeks.org/python-pandas-date_range-method/)
