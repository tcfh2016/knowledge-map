- [聚宽学习第六周周记](./200204-jq_6st_week_summary.md)
- [聚宽学习第七周周记](./200204-jq_7st_week_summary.md)
- [聚宽学习第八周周记](./200204-jq_8st_week_summary.md)
- [聚宽学习第九周周记](./200204-jq_9st_week_summary.md)

## 错误更正

### 1. 股票交易和基金交易手续费是不同的

200329：今天看到[聚宽学习第八周周记：基于中证500ETF的基金定投策略](https://www.joinquant.com/view/community/detail/b46d980deaf0f09cbe8bd5d4fba8147e?page=1#91500)上@黄晨19留言提到：

> 您好，这句话里set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')ordercost感觉应该改为基金的ordercost对象。

查询聚宽API文档里[策略设置函数](https://www.joinquant.com/help/api/help?name=api#%E7%AD%96%E7%95%A5%E8%AE%BE%E7%BD%AE%E5%87%BD%E6%95%B0)，其中描写了`set_order_cost()`的具体用法：

```
set_order_cost(cost, type, ref=None)

指定每笔交易要收取的手续费, 系统会根据用户指定的费率计算每笔交易的手续费

参数

    cost: OrderCost 对象

    open_tax，买入时印花税 (只股票类标的收取，基金与期货不收)

    close_tax，卖出时印花税 (只股票类标的收取，基金与期货不收)

    open_commission，买入时佣金，申购场外基金的手续费

    close_commission, 卖出时佣金，赎回场外基金的手续费

    close_today_commission, 平今仓佣金

    min_commission, 最低佣金，不包含印花税

    type: 股票、场内基金、场内交易的货币基金、分级A基金、分级B基金、分级母基金、金融期货、期货、债券基金、股票基金、QDII 基金、场外交易的货币基金、混合基金、场外基金，'stock'/ 'fund' / 'mmf' /'fja'/'fjb'/ 'fjm'/ 'index_futures' / 'futures' / 'bond_fund' / 'stock_fund' / 'QDII_fund' / 'money_market_fund' / ‘mixture_fund' / 'open_fund'

    ref: 参考代码，支持股票代码/基金代码/期货合约代码，以及期货的品种，如 '000001.XSHE'/'510180.XSHG'/'IF1709'/'IF'/'000300.OF'
```

所以[聚宽学习第八周周记：基于中证500ETF的基金定投策略](https://www.joinquant.com/view/community/detail/b46d980deaf0f09cbe8bd5d4fba8147e?page=1#91500)里的交易手续费的如下设置确实不对：

```
set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
```

如上的设置需要改动两点：1，ETF不需要设置印花税；2，需要将参数`type`由“stock”改为“fund”。如下：

```
set_order_cost(OrderCost open_commission=0.0003, close_commission=0.0003, min_commission=5), type='fund')
```
