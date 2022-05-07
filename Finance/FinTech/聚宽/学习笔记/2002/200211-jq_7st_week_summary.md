# 聚宽学习第七周周记：基于财务数据选股的简单尝试

开始在聚宽上花时间学习快两个月了，觉得收益良多，最起码可以很方便验证偶尔冒出的想法。很多数据都是看财报、上财经网站没有办法直接获取到的，但是聚宽上可以很快的获取到。当然这是需要花些时间去学习和实践的，希望宽友们都是理性的实践派，一步一步做出更好的社区，而不仅仅是为了不费力气赚快钱图爽。尽管我现在不是会员，使用的服务都很低级，但希望往后逐渐能够使用一些高级的服务。

本周的周记代码解释部分主要分解[价值研究笔记之获取较高ROA/ROE市场普通股名单](https://www.joinquant.com/view/community/detail/d3df3da54ac78f7f5e0495fb8fdcbe16)里面的策略研究，这是我第一次使用聚宽来进行全网选股，标准还比较粗略。

## 一、`获取较高ROA/ROE市场普通股名单`代码解释

```
import pandas as pd

def get_stock_name(stock_code):
    stocks_df = get_all_securities()
    stock_name = [stocks_df.loc[c, 'display_name'] for c in stock_code]
    return stock_name

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

init_filter_query = query(
                            valuation.pe_ratio, indicator.code, indicator.roe, indicator.roa,
                        ).filter(
                            indicator.roa > 5,
                            indicator.roe > 10,
                            valuation.pe_ratio > 0,
                            income.total_operating_revenue <= 2e10,
                            income.total_operating_revenue > 1e10
                        ).order_by(
                            indicator.roe.desc()
                        ).limit(
                            100
                        )

df = get_fundamentals(init_filter_query, statDate='2018')
stocks = df['code']

multi_stock_data_query = query(
                                valuation.pe_ratio, indicator.code, indicator.roe, indicator.roa,
                            ).filter(
                                indicator.code.in_(stocks)                                
                            )
roe_dict = {}
roa_dict = {}
year_list = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
for year in year_list:
    df = get_fundamentals(multi_stock_data_query, statDate=year)
    df = df.set_index('code')
    roe_dict[year] = df['roe']
    roa_dict[year] = df['roa']

roe_df = pd.DataFrame(roe_dict)
roe_df.index = get_stock_name(roe_df.index)
print(roe_df)

roa_df = pd.DataFrame(roa_dict)
roa_df.index = get_stock_name(roa_df.index)
print(roa_df)
```

输出结果如下：

```
# ROE 数据

         2012     2013      2014      2015      2016     2017     2018
德赛电池  42.0292  45.6301   36.7709   27.5280   24.4718  23.4739  25.4401
深圳华强  17.1353  23.4449   22.3831   12.6922   11.2260  10.0807  15.4378
中国长城  -8.0230   1.0715    2.2067   -1.3878    1.2367  12.3040  15.2863
鄂武商A  18.0024  17.4650   20.4505   20.8006   19.4758  18.7633  13.6118
万向钱潮   8.8288  14.9370   19.0177   19.0923   19.5368  18.7561  14.0804
泸州老窖  52.0411  33.9179    8.6760   14.7377   18.0952  19.5248  21.6930
攀钢钒钛   3.9985   3.6770  -29.7426  -23.2050 -101.0578  22.3341  52.8145
中信特钢   7.4773   6.6369    8.3031    7.9346    8.1060  10.1889  12.1011
美锦能源  -6.6148   8.2321    2.0762  -10.8518   10.3246  14.5507  24.2232
......

# ROA 数据
          2012     2013     2014     2015     2016     2017     2018
德赛电池  10.4086  10.5129   7.7766   7.6278   8.1814   5.6996   6.3939
深圳华强   5.8560   8.2264  10.5712   7.3072   6.7120   5.8976   8.1577
中国长城   0.2652  -1.9459  -0.1234  -0.4921   0.5345   2.4832   6.7707
鄂武商A   5.0216   5.1215   4.5341   4.7944   5.5878   6.9328   5.1334
万向钱潮   4.3959   6.5947   7.2278   6.8035   7.3400   8.0144   6.3492
泸州老窖  32.3885  24.1409   7.2556  11.7691  14.5198  15.5671  16.5742
攀钢钒钛   1.9185   1.6826 -13.5574  -4.4712 -20.0210   9.1558  28.3191
中信特钢   4.8734   4.6063   5.6260   5.3200   5.3289   6.3561   7.1571
美锦能源  -3.8911   4.9415   1.1571  -5.1976   5.5847   9.2763  12.7299
中百集团   2.5571   2.0240   2.0761   0.0383   0.1003   0.9043   5.5498
......
```

**代码片段一：**

```
def get_stock_name(stock_code):
    stocks_df = get_all_securities()
    stock_name = [stocks_df.loc[c, 'display_name'] for c in stock_code]
    return stock_name
```

这里定义的是一个函数，这个函数的目的是按照给定的股票代码（参数`stock_code`）返回这些股票代码对应的股票名称。之所以要进行这么转换是因为服务器存储股票数据的时候以股票代码作为主要索引，但我们把这些打印出来看的时候代码很难懂，所以才需要转换成中文的股票名称。你可以看到这个函数仅仅在最后打印的时候才调用。

**代码片段二：**

```
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
```

这两句代码也是为打印服务的，它们的作用是设置打印DataFrame二维数据表时能够展现的最大列（`max_columns`）和最大行（`max_rows`）,最大行的默认值是60，最大列的默认值是20，可以参看[官方文档 Options and settings](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html)。

比如你看到的下面这种省略号就是因为打印出的内容的行数超过了规定的最大行数，然后多于的被隐藏起来了。

```
圣农发展  -0.5864  -3.5291   0.4164  -4.7529   6.1012   2.1596  11.1367
天虹股份   6.4131   6.1543   4.8855   9.5108   3.6536   4.7611   5.7144
嘉事堂    3.9370   6.2293   8.3544   5.7761   6.1810   5.6614   5.6905
申通快递   0.8766   0.7571   0.2913   0.0019  26.4799  17.7387  19.8468
...       ...      ...      ...      ...      ...      ...      ...
方大炭素   6.5444   2.6178   2.6571   0.1398   0.3517  36.0962  39.8629
天士力   11.2192  13.1801  12.5392  10.7550   7.4940   7.2547   6.8172
精达股份   2.8342   3.0622   3.1841   3.0099   5.4698   7.9539   9.0348
新安股份   2.0343   6.0315   0.8074  -3.2645   1.1020   6.1547  13.0519
```

**代码片段三：**

```
init_filter_query = query(
                            valuation.pe_ratio, indicator.code, indicator.roe, indicator.roa,
                        ).filter(
                            indicator.roa > 5,
                            indicator.roe > 10,
                            valuation.pe_ratio > 0,
                            income.total_operating_revenue <= 2e10,
                            income.total_operating_revenue > 1e10
                        ).order_by(
                            indicator.roe.desc()
                        ).limit(
                            100
                        )

df = get_fundamentals(init_filter_query, statDate='2018')
stocks = df['code']
```

对于query对象的理解在[周记二](https://www.joinquant.com/view/community/detail/3cc22ef4218363686917d718ba90f4f8)里面有比较详细的介绍。这里创建query对象所包含的条件也即使本次选择普通股应用的条件，包括：

- indicator.roa > 5：总资产收益率（ROA）大于5%。
- indicator.roe > 10：净资产收益率（ROE）大于10%。
- valuation.pe_ratio > 0：动态市盈率（PE）大于0。
- income.total_operating_revenue <= 2e10：营业收入小于或等于20亿。
- income.total_operating_revenue > 1e10：营业收入大于10亿。

要应用上面这些标准需要查看不同的数据表，比如indicator是[财务指标数据](https://www.joinquant.com/help/api/help?name=JQData#%E8%B4%A2%E5%8A%A1%E6%8C%87%E6%A0%87%E6%95%B0%E6%8D%AE)，里面包含了ROA和ROE等数据。valuation是[市值数据](https://www.joinquant.com/help/api/help?name=JQData#%E5%B8%82%E5%80%BC%E6%95%B0%E6%8D%AE%EF%BC%88%E6%AF%8F%E6%97%A5%E6%9B%B4%E6%96%B0%EF%BC%89)，里面包含了PE等数据。income是[利润表](https://www.joinquant.com/help/api/help?name=Stock#%E5%88%A9%E6%B6%A6%E6%95%B0%E6%8D%AE)，里面包含了营业收入等数据。把这些条件设定好了之后使用`filter`过滤。

然后`order_by`是针对查询结果的排序方法，这里是按照净资产收益率（ROE）进行降序排列，最后使用`limit`取用排名靠前的100条记录。在创建好query对象之后我们调用`get_fundamentals()`来执行前面准备的这些查询操作，就可以得到下面这样的结果：

```
    pe_ratio         code      roe      roa
0    11.5008  000629.XSHE  52.8145  28.3191
1     4.3696  600507.XSHG  51.7314  32.1590
2     4.9300  600516.XSHG  50.0955  39.8629
3    11.1500  002027.XSHE  47.3919  33.5042
4    10.4912  603260.XSHG  42.0329  18.8691
5    38.0252  300760.XSHE  34.1555  20.6608
......
```

最后我们使用`stocks = df['code']`把上面这个二维表数据里面的`code`这一列取出来，它们就是我们需要进一步去查询的股票代码。因为我们这时查询的是`2018年`财务数据对应的结果，我们还想进一步去看这些股票在往年的财务表现怎么样。

**代码片段四：**

```
multi_stock_data_query = query(
                                valuation.pe_ratio, indicator.code, indicator.roe, indicator.roa,
                            ).filter(
                                indicator.code.in_(stocks)                                
                            )

roe_dict = {}
roa_dict = {}
year_list = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
for year in year_list:
    df = get_fundamentals(multi_stock_data_query, statDate=year)
    df = df.set_index('code')
    roe_dict[year] = df['roe']
    roa_dict[year] = df['roa']
```

对于上面初步筛选出来的那些在2018年具有最高净资产收益率（ROE）的普通股，我们想看看这些普通股在2012年~2018年的总资产收益率（ROA）和净资产收益率（ROE）的历史表现，所以我们这里需要再次进行一轮新的查询，分两步。

第一步：我们先设定好要查询的数据，主要是每只股票的市盈率（`valuation.pe_ratio`）、股票代码（`indicator.code`）、净资产收益率（indicator.roe）和总资产收益率（indicator.roa），`filter`条件指定为上面初步筛选出来的股票。

第二步：循环查询每年这些股票的数据，然后讲净资产收益率（ROE）和总资产收益率（ROA）分别用字典保存起来，使用查询的年作为字典存储时候的键值。

完成这两步之后我们就得到了之前筛选出来的股票在2012年~2018年的总资产收益率、净资产收益率数据，然后我们要接用Pandas将其更友好的展示出来（*复习一下：Pandas是用来进行更加便捷地处理数据的Python库，在金融领域进行数据处理可以说是无法回避的。*）。

**代码片段五：**

```
roe_df = pd.DataFrame(roe_dict)
roe_df.index = get_stock_name(roe_df.index)
print(roe_df)

roa_df = pd.DataFrame(roa_dict)
roa_df.index = get_stock_name(roa_df.index)
print(roa_df)
```

然后我们分别根据保存净资产收益率和总资产收益率的字典来创建DataFrame，然后我们要讲默认index为股票代码（code）修改为股票名称，方便我们阅读。打印出来就能得到下面这样的结果：

```
# ROE 数据

         2012     2013      2014      2015      2016     2017     2018
德赛电池  42.0292  45.6301   36.7709   27.5280   24.4718  23.4739  25.4401
深圳华强  17.1353  23.4449   22.3831   12.6922   11.2260  10.0807  15.4378
中国长城  -8.0230   1.0715    2.2067   -1.3878    1.2367  12.3040  15.2863
鄂武商A  18.0024  17.4650   20.4505   20.8006   19.4758  18.7633  13.6118
万向钱潮   8.8288  14.9370   19.0177   19.0923   19.5368  18.7561  14.0804
......

# ROA 数据
        2012     2013     2014     2015     2016     2017     2018
德赛电池  10.4086  10.5129   7.7766   7.6278   8.1814   5.6996   6.3939
深圳华强   5.8560   8.2264  10.5712   7.3072   6.7120   5.8976   8.1577
中国长城   0.2652  -1.9459  -0.1234  -0.4921   0.5345   2.4832   6.7707
鄂武商A   5.0216   5.1215   4.5341   4.7944   5.5878   6.9328   5.1334
......
```

## 二、上周计划任务

### 1.什么是网格交易？

> 宽友@odbo前段时间留言时提到“网格交易”这个名词，自己还没有了解过，做些学习和了解。

先要感谢 @odbo 同学！让太懒惰的我这周又解锁了一个新概念。在经过一些了解之后基本弄清楚“网格交易”的定义，它其实是我们经常说的“分批买入、分批卖出”的升级版，实际上是一种做波段的方法，比较适合于震荡市场行情中。

就像没人能准确预测未来行情走势一样，后世是否为“震荡行情”也是无法得知的，这是它的不足之处，其实也是所有投资需要面对的风险所在。由于“估值”是其中最重要的一个环节。所以，其实用这种方式来优化价值投资的操作。大致过程如下：

- 对普通股/指数进行估值，确定其模糊的内在价值区间[a, b]
- 在市值小于a时进行网格交易，进行分批买入
- 在市值大于b时进行网格交易，进行分批卖出

这种方式给我的启发是手里面要留有一定的现金以备不时之需。

参考：

- [网格交易致命弱点是什么？有什么好办法克服？](https://www.zhihu.com/question/41829464/answer/777301686)
- [初识网格交易](https://zhuanlan.zhihu.com/p/80052984)

### 2.修改之前第一个模拟定投的策略，计算下真实收益率

已经完成，并且发布到社区，参看[价值研究笔记之基金定投模拟](https://www.joinquant.com/view/community/detail/3d7d7a201cc6dedc526b5c5e329d9baa)。

其实觉得不管是量化还是简单的买卖股票，一些金融尝试和财务知识还是需要的，因为这能够帮助你更准确地理解证券市场里面的一些运作概念。有了这些概念不一定就能做得很好，但没有这些概念便会觉得没有根基，很多内容难以做到真正的理解。

## 三、本周新学内容

### 如何在策略完成时计算策略的总体收益率？

在执行策略的时候需要在策略完成时计算策略的内部收益率（IRR），但是从写的第一个简单策略里面只有针对定时运行策略的控制，比如可以给run_daily/run_weekly/run_monthly 指定before_market_open/market_open/after_market_close分别在开盘前、中、后执行，但我想要的是在整个策略执行完成的时候计算策略的总体收益。

于是决定阅读[API文档](https://www.joinquant.com/help/api/help?name=api#%E7%AD%96%E7%95%A5%E7%A8%8B%E5%BA%8F%E6%9E%B6%E6%9E%84%E2%99%A6)，在策略程序架构章节里面发现了可以完成这项功能的函数`on_strategy_end()`，定义如下：

```
def on_strategy_end(context)

在回测、模拟交易正常结束时被调用， 失败时不会被调用。

在模拟交易到期结束时也会被调用， 手动在到期前关闭不会被调用。
```

这个函数会默认调用，可以通过重写这个函数来决定策略执行结束时做什么。

### 统计基金当日的交易量

官方API里面给定了[获取场内基金tick数据](https://www.joinquant.com/help/api/help?name=fund#%E8%8E%B7%E5%8F%96%E5%8D%95%E6%94%AF%E5%9F%BA%E9%87%91%E6%95%B0%E6%8D%AE)的方法，如果统计当天的需要重新写函数进行统计。

比如如下统计创业板在2020年2月14日这一天的成交量，需要先使用`get_ticks()`获取整天的所有成交信息，然后再对这一整天进行求和操作：

```
nd = get_ticks('159915.XSHE','2020-02-14 15:30:00','2020-02-14 09:00:00')
df = pd.DataFrame(nd)
print(df['volume'].sum())

# 输出：691 194 074 791 股
```

这种看起来有些粗略，其实可以再写一个函数来以天为单位分别统计。

## 四、下周学习任务

### 1.写函数统计基金的成交量，提供按天、月为单位进行统计。

### 2.如何获取创业板指数的市盈率？
