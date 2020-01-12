# 聚宽学习第四周周记：获取中证指数的市盈率

## 一、`获取某只指数的市盈率`代码解释

原版代码见2019年12月24日发布在社区的[价值研究笔记之获取单只指数市盈率和股价变化](https://www.joinquant.com/view/community/detail/86b91e08d858edc519c763b0aa449221)。

```
from jqdata import jy
from jqdata import *
import pandas as pd

def get_zz_quote(code,end_date=None,count=None,start_date=None):
    '''获取中证指数行情,返回panel结构'''
    if isinstance(code,str):
        code=[code]
    code.sort()

    code = [x[:6] for x in code]
    days = get_trade_days(start_date,end_date,count)
    code_df = jy.run_query(query(
         jy.SecuMain.InnerCode,jy.SecuMain.SecuCode,jy.SecuMain.ChiName
        ).filter(
        jy.SecuMain.SecuCode.in_(code)).order_by(jy.SecuMain.SecuCode))
    df = jy.run_query(query(
             jy.QT_CSIIndexQuote).filter(
            jy.QT_CSIIndexQuote.IndexCode.in_(code_df.InnerCode),
            jy.QT_CSIIndexQuote.TradingDay.in_(days),
            ))
    df2  = pd.merge(code_df, df, left_on='InnerCode',right_on='IndexCode').set_index(['TradingDay','SecuCode'])
    df2.drop(['InnerCode','IndexCode','ID','UpdateTime','JSID','OpenInterest','SettleValue','IndexCSIType'],axis=1,inplace=True)
    return df2.to_panel()

# 中证500，指数代码 = 000905.XSHG
panel = get_zz_quote(['000905.XSHG'], end_date='2019-12-22', start_date='2009-12-22')
df_905 = panel.ix[:, :, '000905']
df_905.plot(y = ['ClosePrice', 'IndexPERatio1', 'IndexPERatio2'], secondary_y = 'ClosePrice', figsize=(20,10))

```

效果图如下：

![](./index_pe.png)

**代码片段一：**

```
from jqdata import jy
from jqdata import *
import pandas as pd
```

这段代码最后两句在[第三周的周记](https://www.joinquant.com/view/community/detail/dea963ac96739ecd008c52cba3819d0c)里面有过解释，使用`from jqdata import *`的原因在于`get_zz_quote()`中要使用聚宽服务中的`get_trade_days()`，而后者定义在了`jqdata`模块里面。

对于第一句的`from jqdata import jy`是因为`get_zz_quote()`中要使用定义在`jqdata`模块里的`jy`服务，`jy`服务是提供了对聚源数据的访问，聚源数据是恒生提供的[金融数据数据库](http://www.gildata.com/)。

**代码片段二：**

```
def get_zz_quote(code,end_date=None,count=None,start_date=None):
    '''获取中证指数行情,返回panel结构'''
    if isinstance(code,str):
        code=[code]
    code.sort()

    code = [x[:6] for x in code]
    days = get_trade_days(start_date,end_date,count)
    code_df = jy.run_query(query(
         jy.SecuMain.InnerCode,jy.SecuMain.SecuCode,jy.SecuMain.ChiName
        ).filter(
        jy.SecuMain.SecuCode.in_(code)).order_by(jy.SecuMain.SecuCode))
    df = jy.run_query(query(
             jy.QT_CSIIndexQuote).filter(
            jy.QT_CSIIndexQuote.IndexCode.in_(code_df.InnerCode),
            jy.QT_CSIIndexQuote.TradingDay.in_(days),
            ))
    df2  = pd.merge(code_df, df, left_on='InnerCode',right_on='IndexCode').set_index(['TradingDay','SecuCode'])
    df2.drop(['InnerCode','IndexCode','ID','UpdateTime','JSID','OpenInterest','SettleValue','IndexCSIType'],axis=1,inplace=True)
    return df2.to_panel()
```

这段代码是直接拷贝[聚宽已有的共享函数](https://www.joinquant.com/view/community/detail/16656)，这个函数我还没有拆解过先不直接解释，直接使用就行了。目前使用这个函数的小问题是因为之前提到过的panel在pandas 0.25.0版本之后不再使用，所以使用的时候会提示一些警告信息。我准备之后对这个函数进行修改来消除警告信息，再深入解析函数的基本原理。

**代码片段三：**

```
panel = get_zz_quote(['000905.XSHG'], end_date='2019-12-22', start_date='2009-12-22')
df_905 = panel.ix[:, :, '000905']
df_905.plot(y = ['ClosePrice', 'IndexPERatio1', 'IndexPERatio2'], secondary_y = 'ClosePrice', figsize=(20,10))
```

最后这段代码是对于获取到的数据的进一步抽取，因为panel是一种三维数据表的类型，首先通过第一维的索引`000905`访问它所对应的DataFrame数据，也就是是`panel.ix[:, :, '000905']`已经是一个二维数据表，也即DataFrame类型。

由于DataFrame类型里面包含了很多列的数据，包括`ChiName`,	`OpenPrice`, `HighPrice`, `LowPrice`, `ClosePrice`, `TurnoverVolume`, `TurnoverValue`, `ChangeOF`, `ChangePCT`, `TotalMV`, `IndexPERatio1`, `IndexPERatio2`, `IndexDYRatio1`和`IndexDYRatio2`，但是我们仅仅对其中的市盈率数据感兴趣，也就是`IndexPERatio1`和`IndexPERatio2`，所以在调用`plot()`进行绘图的时候指定了它们。

注：至于`IndexPERatio1`和`IndexPERatio2`的具体区别是什么我还没有完全弄清楚，按照定义来说前者是“是按总股本计算的市盈率”，后者是“是按照中证指数调整后的股本计算的市盈率”。不过没有明白定义里面“调整”的含义。

## 二、上周计划任务

### 1.使用聚宽策略来模拟基金定投的效果

>有人在元旦那天发布的[新年ETF基金定投计划](https://www.joinquant.com/view/community/detail/10c029abcd8f69bd59b8b1172a547d31)留言提到了使用聚宽策略来进行模拟的话题，这刚好是接触使用策略的机会，不妨试试看。

为了完成这个任务，我本周使用聚宽策略对“拍脑袋想出来的定投计划”进行了一次模拟，整个过程中有不少收获，比如：

- 定投的收益来自于行情处于低谷时加大投入，在行情过于火热时停止定投并卖出。
- 进一步坚信了指数定投能够带来的相比个股更小波动、相比储蓄更加可靠的收益。
- 发现当时拍脑袋随意制定的定投计划还可以进行优化，比如每月定投金额所带来的收益。

**对原始策略进行的模拟**

原始的策略是根据中证500指数对应市盈率划分的区间进行定投：

```
指数 < 20，每月第一个交易日投入3000元
指数 < 30，每月第一个交易日投入2000元
指数 < 40，每月第一个交易日投入1000元
指数 > 40，每月第一个交易日卖出
```

分别对7个时间段进行了回测模拟，有以下数据：

|起始日期|结束日期|基准收益|策略收益|策略年化收益率|最大浮亏|
|-|-|-|-|-|-|
|2019-01-01|2019-12-31|36.07%|2.86%|2.94%|-0.68%|
|2018-01-01|2019-12-31|1.63%|4.06%|2.07%|-3.55%|
|2017-01-01|2019-12-31|23.76%|3.28%|1.11%|-5.33%|
|2016-01-01|2019-12-31|9.80%|3.59%|0.91%|-5.07%|
|2015-01-01|2019-12-31|15.93%|4.44%|0.89%|-4.22%|
|2014-01-01|2019-12-31|75.82%|20.28%|3.20%|-0.42%|
|2013-03-15|2019-12-31|61.65%|40.39%|5.25%|-0.61%|

是不是觉得年化收益率2.94%也太低了？起始并不低，对于上面统计的这几项收益率需要简单的进行解释，因为在执行策略模拟的时候需要指定初始资金，所以“基准收益”和“策略收益”所表达的含义并不一样：对于“基准收益”来讲相当于你在第一个交易日即全部投入了所有资金，然后最后一个交易日的时候来看它的收益率是多少；对于“策略收益”来讲，它也默认你在第一个交易日投入了所有的资金，在最后一个交易日来看它的收益率，但实际上我们的策略是逐步定投的，并不是一次性全部投入。所以，上面显示的策略收益实际上要更高一些。

举个例子，比如我们模拟的2019-01-01到2019-12-31这个时间段，假设指定的初始资金为100000元，那么“基准收益为36.07%”表示的是“2019-01-01投入了100000元购买基准指数，2019-12-31卖出共得到136070元，盈利36070元”。而“策略收益为2.86%”表示的是“假设你开始就投入了100000元资金，2019-12-31总共的资金为102860元”，但实际上我所采用的策略并不是一开始就投入了100000元，而是每个月投入2000/3000,整个一年累计投入了30225.39元，也就是说总投入30225.39元盈利2860元，至少也有超过9.46%的年化收益率（真实收益率需要计算内部收益率，比简单通过2860/30225.39要答）。

**对新的策略进行的模拟**

对于如上的策略我们可以变更投入的金额，比如在<20的时候加大投入，这样可以获取到更多的绝对收益。这里我们想讨论卖出时机的问题，比如`指数市盈率>50`的时候卖出：

|起始日期|结束日期|基准收益|策略收益|策略年化收益率|最大浮亏|
|-|-|-|-|-|-|
|2019-01-01|2019-12-31|36.07%|2.86%|2.94%|-0.68%|
|2018-01-01|2019-12-31|1.63%|4.06%|2.07%|-3.55%|
|2017-01-01|2019-12-31|23.76%|3.28%|1.11%|-5.33%|
|2016-01-01|2019-12-31|9.80%|2.84%|0.72%|-6.80%|
|2015-01-01|2019-12-31|15.93%|3.98%|0.80%|-5.98%|
|2014-01-01|2019-12-31|75.82%|25.93%|4.02%|-0.35%|
|2013-03-15|2019-12-31|61.65%|52.73%|6.60%|-0.59%|

可以看到如果过于在乎卖出时机，比如一定要等到牛市的顶峰才卖出，那个时候尽管可以获取更多的收益，但是需要承受更长的等待期，并且要经历眼看着收益从较高点滑落至低点的难熬过程。

### 2.开始了解聚宽因子

还没有开始学，拖了2周啦，估计要年后才能开始咯@_@

## 三、本周新学知识

基于策略模板写了一个粗略的模拟策略，附后。

## 四、下周预定主题

### 1.理解获取中证指数市盈率的共享函数，并且看是否可以修改不再使用panel。

### 2.弄清楚策略回测时候的一些基本概念。

- 阿尔法
- 贝塔
- 夏普比率
- 胜率
- 盈亏比
- 最大回撤
- 索提诺比率
- 信息比率
- 策略波动率
- 基准波动率

房间空调坏了，发现写周记冻得手痛，有点辛苦呀。
