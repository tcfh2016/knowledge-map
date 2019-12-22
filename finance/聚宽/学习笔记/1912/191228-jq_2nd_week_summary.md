# 第二周周记：获取多只股票市盈率

## 代码解析

```

```

## Pandas中的Panel类型

### Panel简介

### 上周的作业

> 上周提到的使用`get_price()`时传入股票列表所返回的Pandas中的三维数据类型Panel在Pandas 0.20.0之后就过时了，所以不建议继续使用。在调用该函数的时候也可以直接设定`panel=Fase`，这个时候获取到的结果也是DataFrame，但我们需要将其进行进一步处理来满足需求，这个主题我会在下周学习。

```
multi_stock_price = get_price(stock_code_list, start_date, end_date, 'daily', 'close', panel=False)
```

## Pandas中的pvtable

> 宽友 @jqz1226 在[《再谈获取多只股票的市盈率—极速版》](https://www.joinquant.com/view/community/detail/24517)改进过我另外一篇[价值研究笔记之获取多只股票的市盈率](https://www.joinquant.com/view/community/detail/97ac84a17f7e9da63be455ac8df30971)，迭代出两个新的版本，其中使用到了新的`get_fundamentals_continuously()`, `get_valuation`以及Padans的数据透视表，这些都是我还没有学习到的内容，因此将进一步学习。



## 下周主题

## 参考文档

-[Panel(面板)数据结构](https://www.cnblogs.com/JeremyTin/p/5324536.html)
