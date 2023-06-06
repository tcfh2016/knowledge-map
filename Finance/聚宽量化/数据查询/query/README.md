# query对象

要认识query对象先必须要认识SQLAlchemy ORM，因为query对象是SQLAlchemy ORM的操作对象，但是在这之前必须要先将SQLAlchemy ORM拆分为两段进行解释：`SQLAlchemy`是一个用来支持Python与数据库之间进行交互的工具包，它包括两个部分`SQLAlchemy ORM`和`SQLAlchemy Core`两部分，SQLAlchemy ORM简称ORM(Object Relational Mapper)在Python的类与数据库中的表之间建立了连接，使得用户可以像操作Python类那样完成数据库的访问工作。简单来说SQLAlchemy ORM是一个用来便捷访问数据库的函数库，层次高，用得爽。

那么[query对象](https://docs.sqlalchemy.org/en/13/orm/query.html#sqlalchemy.orm.query.Query)就是ORM里面专门用于查询功能的对象。我们只需要按照规则写一句`query(valuation.day, valuation.code, valuation.pe_ratio).filter(valuation.code == stock_code)`之后的工作就交给`SQLAlchemy ORM`，执行时它可能要将其转换为很多句SQL语句来完成数据库的查询，上面这句查询条件的意思是“查询对应股票的市值表，同时过滤出查询的日期、股票代码和股票当日的市盈率”。

在理解query对象之后，我发现上面的query对象的那条语句实际上可以简化：`q = query(valuation.day, valuation.code, valuation.pe_ratio).filter(valuation.code == stock_code)`可以简化为`q = query(valuation.pe_ratio).filter(valuation.code == stock_code)`，因为我们当前仅仅对市盈率感兴趣。

参考：

- [SQLAlchemy Overview](https://docs.sqlalchemy.org/en/13/intro.html)
- [Constructing Database Queries with SQLAlchemy](https://hackersandslackers.com/database-queries-sqlalchemy-orm/)
- [The Query Object](https://docs.sqlalchemy.org/en/13/orm/query.html#the-query-object)


## filter(criterion)

对数据库的查询指定条件，这些条件相当于select表达式里面的WHERE子句，可以同时指定多个条件。

```
session.query(MyClass).\
    filter(MyClass.name == 'some name', MyClass.id > 5)
```


## order_by(criterion)

指定针对查询结果的一个或者多个排序条件，默认以升序排列。比如下面的代码是查询指定代码的市盈率和市值数据，并默认按从市值从小到大排序：


```
q = query(
  valuation.code, valuation.pe_ratio, valuation.market_cap
).filter(
  valuation.code.in_(code)
).order_by(valuation.market_cap)
```

将`...).order_by(valuation.market_cap)`修改为`...).order_by(valuation.market_cap.desc())`。

参考：

- [沪深港通持股数据](https://www.joinquant.com/help/api/help#name:Stock)
- [【有用功】Query的简单教程及TTM/同比/环比算法示例](https://www.joinquant.com/view/community/detail/433d0e9ed9fed11fc9f7772eab8d9376)
- [SQL | ORDER BY](https://www.geeksforgeeks.org/sql-order-by/)
- [SQLAlchemy ORDER BY DESCENDING?](https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending)
