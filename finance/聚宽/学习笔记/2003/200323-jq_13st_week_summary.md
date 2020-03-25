# 聚宽学习周记十三：详解@东南有大树的“ETF二八轮动对冲模型”（上）

@东南有大树写的[用指数战胜指数，ETF二八轮动对冲模型](https://www.joinquant.com/view/community/detail/19490)这篇内容有点多，所以不得不将学习笔记分成多篇。在上篇里面主要是解决这篇文章里面的一些扩展阅读，比如代码解释部分是解析文中引用的聚宽官方的[【量化课堂】斗牛蛋卷二八轮动原版策略实现](https://www.joinquant.com/view/community/detail/9434c4a9c9482c7d1071be947dd3558a?type=1)，后面的周记里面再去学习@东南有大树文章中的研究和策略内容，最后在理解了整篇文章的基础之上尝试写作练习策略。


## 一、代码解释

打开[【量化课堂】斗牛蛋卷二八轮动原版策略实现](https://www.joinquant.com/view/community/detail/9434c4a9c9482c7d1071be947dd3558a?type=1)里面的策略源代码，有种赏心悦目的感觉。不得不说这样的代码写得实在是很清晰，这次一句一句的阅读也是一个学习的过程。

```
'''
=================================================
总体回测前设置参数和回测
=================================================
'''
def initialize(context):
    set_params()    #1设置策参数
    set_variables() #2设置中间变量
    set_backtest()  #3设置回测条件

#1 设置参数
def set_params():
    # 设置基准收益
    set_benchmark('000300.XSHG')
    g.lag = 20
    g.hour = 14
    g.minute = 53

    g.hs =  '000300.XSHG' #300指数
    g.zz =  '000905.XSHG'#500指数

    g.ETF300 = '510300.XSHG'#'510300.XSHG'
    g.ETF500 = '510500.XSHG'#'510500.XSHG'


#2 设置中间变量
def set_variables():
    return

#3 设置回测条件
def set_backtest():
    set_option('use_real_price', True) #用真实价格交易
    log.set_level('order', 'error')


'''
=================================================
每天开盘前
=================================================
'''
#每天开盘前要做的事情
def before_trading_start(context):
    set_slip_fee(context)

#4
# 根据不同的时间段设置滑点与手续费

def set_slip_fee(context):
    # 将滑点设置为0
    set_slippage(FixedSlippage(0))
    # 根据不同的时间段设置手续费
    dt=context.current_dt

    if dt>datetime.datetime(2013,1, 1):
        set_commission(PerTrade(buy_cost=0.0003, sell_cost=0.0013, min_cost=5))

    elif dt>datetime.datetime(2011,1, 1):
        set_commission(PerTrade(buy_cost=0.001, sell_cost=0.002, min_cost=5))

    elif dt>datetime.datetime(2009,1, 1):
        set_commission(PerTrade(buy_cost=0.002, sell_cost=0.003, min_cost=5))

    else:
        set_commission(PerTrade(buy_cost=0.003, sell_cost=0.004, min_cost=5))


'''
=================================================
每日交易时
=================================================
'''
def handle_data(context, data):
    # 获得当前时间
    hour = context.current_dt.hour
    minute = context.current_dt.minute

    # 每天收盘时调整仓位
    if hour == g.hour and minute == g.minute:
        signal = get_signal(context)

        if signal == 'sell_the_stocks':
            sell_the_stocks(context)
        elif signal == 'ETF300' or signal == 'ETF500':
            buy_the_stocks(context,signal)

#5
#获取信号
def get_signal(context):

    #沪深300与中证500的当日收盘价
    hs300,cp300 = getStockPrice(g.hs, g.lag)
    zz500,cp500  = getStockPrice(g.zz, g.lag)

    #计算前20日变动
    hs300increase = (cp300 - hs300) / hs300
    zz500increase = (cp500 - zz500) / zz500

    hold300 = context.portfolio.positions[g.ETF300].total_amount
    hold500 = context.portfolio.positions[g.ETF500].total_amount

    if (hs300increase<=0 and hold300>0) or (zz500increase<=0 and hold500>0):
        return 'sell_the_stocks'
    elif hs300increase>zz500increase and hs300increase>0 and (hold300==0 and hold500==0):
        return 'ETF300'
    elif zz500increase>hs300increase and zz500increase>0 and (hold300==0 and hold500==0):
        return 'ETF500'

#6
#取得股票某个区间内的所有收盘价（用于取前20日和当前 收盘价）
def getStockPrice(stock, interval):
    h = attribute_history(stock, interval, unit='1d', fields=('close'), skip_paused=True)
    return (h['close'].values[0],h['close'].values[-1])

#7
#卖出股票
def sell_the_stocks(context):
    for stock in context.portfolio.positions.keys():
        return (log.info("Selling %s" % stock), order_target_value(stock, 0))

#8
#买入股票
def buy_the_stocks(context,signal):
    return (log.info("Buying %s"% signal ),order_value(eval('g.%s'% signal), context.portfolio.cash))


'''
=================================================
每日收盘后（本策略中不需要）
=================================================
'''  
def after_trading_end(context):
    return
```

聚宽策略目前来说我写作过两个练习策略，第一个是模拟基金定投的策略（现在回过头去看突然觉得几个月前自己太菜了，因为现在在学的二八轮动等策略毫无疑问是我那种思路上的好几个翻版，要说那个策略的唯一亮点之处就是简单好操作）；第二个是上周基于@Gyro市盈率研究的文章上修改的基于指数的再平衡策略。前一个策略是完全按照聚宽给定的策略模板改写的，后面是在阅读了API稳当之后从无到有写作的。尽管我还是个初学者，但基于当前已经能够感受到学习时已经在产生的变化，对于初学者学习聚宽有个建议。

这个建议也就是尽可能比较完整的照着聚宽官方的API文档走几遍，把它提供的大致的服务函数有个印象，这不是一蹴而就的事，要多看几遍。最重要的一定要理解整个策略的执行框架，这是自己写作策略和看懂其他人写的策略的基础。否则，你可能会觉得策略很难理解。理解了策略的框架后，其他的就剩Python知识点了。

**策略的整体框架**

解释这次的代码我需要换个形式了，不再是从第一句开始解释到最后一句，而是要从逻辑的衔接上进行划分来帮助理解。首先，我们要认识这个策略的整体框架。

如果你学习过聚宽API中的[策略程序架构](https://www.joinquant.com/help/api/help?name=api#%E7%AD%96%E7%95%A5%E7%A8%8B%E5%BA%8F%E6%9E%B6%E6%9E%84%E2%99%A6)你会比较清楚策略的组成主要包括两部分：一、初始化函数`initialize()`，它是必须的；二、定时运行系列函数，它们是可选的，但是实际上也是必不可少的。定时运行系列函数又可以分为三类：

- 开盘前执行：before_trading_start
- 开盘时执行：run_daily/run_weekly/run_monthly/handle_data
- 收盘后执行：after_trading_end

基于如上的理解那么我们可以看到上面的策略是由“initialize + before_trading_start + handle_data + after_trading_end” 组成的，也就是“初始化函数 + 开盘前执行函数 + 开盘时执行函数 + 收盘后执行函数”组成。你获取会奇怪为什么这里的开盘时执行函数没有使用`run_daily/run_weekly/run_monthly`而是使用了`handle_data`呢？这要明白它们之间的区别：

- `run_daily/run_weekly/run_monthly`顾名思义是按天、周、月的频率执行策略，而`handle_data`支持天、分钟、tick的执行频率，你需要在策略平台的选项里面点击选项进行选择。
- `run_daily/run_weekly/run_monthly`可以指定更加细致的时间，比如按天时可以指定具体的几点几分，而`handle_data`按天时默认在09:30执行。
- 两者的参数不同，`handle_data`除了传入`context`参数外还可以多传入`data`，表示前一天股票的行情数据。
- `run_daily/run_weekly/run_monthly`需要手动注册调用函数，但`handle_data`默认直接调用。

所以实际上也可以使用`run_daily`来替代`handle_data`，但相比之下要多写一行代码。

**策略初始化**

```
def initialize(context):
    set_params()    #1设置策参数
    set_variables() #2设置中间变量
    set_backtest()  #3设置回测条件

#1 设置参数
def set_params():
    # 设置基准收益
    set_benchmark('000300.XSHG')
    g.lag = 20
    g.hour = 14
    g.minute = 53

    g.hs =  '000300.XSHG' #300指数
    g.zz =  '000905.XSHG'#500指数

    g.ETF300 = '510300.XSHG'#'510300.XSHG'
    g.ETF500 = '510500.XSHG'#'510500.XSHG'


#2 设置中间变量
def set_variables():
    return

#3 设置回测条件
def set_backtest():
    set_option('use_real_price', True) #用真实价格交易
    log.set_level('order', 'error')
```

策略初始化我们已经提到过`initialize`这个函数一定是必须的，因为每个策略开始执行前系统会调用这个函数来完成基本的初始化工作。这里的`set_params`,`set_variables`,`set_backtest`这三个函数是辅组函数，或者说是为了代码风格而将功能进行了细分，按照我当前粗糙的写法可能就是下面这样：

```
def initialize(context):
    set_benchmark('000300.XSHG')
    g.lag = 20
    g.hour = 14
    g.minute = 53

    g.hs =  '000300.XSHG' #300指数
    g.zz =  '000905.XSHG'#500指数

    g.ETF300 = '510300.XSHG'#'510300.XSHG'
    g.ETF500 = '510500.XSHG'#'510500.XSHG'

    set_option('use_real_price', True) #用真实价格交易
    log.set_level('order', 'error')
```

对比之下显然将不同部分分成不同函数看起来层次感好要一些。整个初始化里面完成的任务包括了四部分：

- `set_benchmark...` 设定了业绩参考基准
- `g....` 设置了全局变量，共之后交易时使用
- `set_option...` 设定复权模式
- `log....` 设定日志输出级别

这些初始化的工作仅仅在策略开始的时候做一次，和每次开盘前/中/后执行的策略函数是不一样的。

**开盘前的工作**

```
#每天开盘前要做的事情
def before_trading_start(context):
    set_slip_fee(context)

def set_slip_fee(context):
    # 将滑点设置为0
    set_slippage(FixedSlippage(0))
    # 根据不同的时间段设置手续费
    dt=context.current_dt

    if dt>datetime.datetime(2013,1, 1):
        set_commission(PerTrade(buy_cost=0.0003, sell_cost=0.0013, min_cost=5))

    elif dt>datetime.datetime(2011,1, 1):
        set_commission(PerTrade(buy_cost=0.001, sell_cost=0.002, min_cost=5))

    elif dt>datetime.datetime(2009,1, 1):
        set_commission(PerTrade(buy_cost=0.002, sell_cost=0.003, min_cost=5))

    else:
        set_commission(PerTrade(buy_cost=0.003, sell_cost=0.004, min_cost=5))
```

`before_trading_start()`这个函数是开盘前默认调用的函数，如果需要在每次开盘前做一些配置
或者计算那么直接写在里面。这里它做的工作包括两部分：设置滑点和手续费。

滑点的介绍可以阅读聚宽API上[滑点部分](https://www.joinquant.com/help/api/help?name=api#%E8%82%A1%E6%81%AF%E7%BA%A2%E5%88%A9%E7%A8%8E%E7%9A%84%E8%AE%A1%E7%AE%97)，滑点主要用来设定真实成交价格与预期价格之间的偏差。如果不设置滑点系统会默认设定百分比滑点` PriceRelatedSlippage(0.00246)`。

这里也按照日期区间设置了不同的交易手续费。交易手续费有下降的趋势，2009年之前设定为千分之三/四，2009年后年前降到千分之二/三，2011年降到千分之一/二，2013年后进一步下降到万分之三。这些手续费对于低频交易影响不大，但高频交易就有不小的影响。

**开盘时的工作**

```
def handle_data(context, data):
    # 获得当前时间
    hour = context.current_dt.hour
    minute = context.current_dt.minute

    # 每天收盘时调整仓位
    if hour == g.hour and minute == g.minute:
        signal = get_signal(context)

        if signal == 'sell_the_stocks':
            sell_the_stocks(context)
        elif signal == 'ETF300' or signal == 'ETF500':
            buy_the_stocks(context,signal)

def get_signal(context):

    #沪深300与中证500的当日收盘价
    hs300,cp300 = getStockPrice(g.hs, g.lag)
    zz500,cp500  = getStockPrice(g.zz, g.lag)

    #计算前20日变动
    hs300increase = (cp300 - hs300) / hs300
    zz500increase = (cp500 - zz500) / zz500

    hold300 = context.portfolio.positions[g.ETF300].total_amount
    hold500 = context.portfolio.positions[g.ETF500].total_amount

    if (hs300increase<=0 and hold300>0) or (zz500increase<=0 and hold500>0):
        return 'sell_the_stocks'
    elif hs300increase>zz500increase and hs300increase>0 and (hold300==0 and hold500==0):
        return 'ETF300'
    elif zz500increase>hs300increase and zz500increase>0 and (hold300==0 and hold500==0):
        return 'ETF500'

def getStockPrice(stock, interval):
    h = attribute_history(stock, interval, unit='1d', fields=('close'), skip_paused=True)
    return (h['close'].values[0],h['close'].values[-1])

def sell_the_stocks(context):
    for stock in context.portfolio.positions.keys():
        return (log.info("Selling %s" % stock), order_target_value(stock, 0))

def buy_the_stocks(context,signal):
    return (log.info("Buying %s"% signal ),order_value(eval('g.%s'% signal), context.portfolio.cash))
```

`handle_data()`是在开盘后调用，这个策略是按照分钟级别的频率运行，所以我们定义的盘前、盘中和盘后的执行函数都会在每分钟执行。交易执行时函数`handle_data()`的实现上会判断当前的时间，只有在满足`hour == g.hour and minute == g.minute`的时候才会进行仓位调整的尝试。`g.hour`和`g.minute`都是在策略初始化的时候定义好的，翻译过来就是在每个交易日的14点53分尝试调整仓位。

`get_signal()`这个函数用来获取当前的操作指导，这个函数里面的算法包括如下几步：

- 获取沪深300和中证500在20天前的收盘价和今天的收盘价
- 计算今天的收盘价相比20天前的增幅
- 获得当前沪深300和中证500指数对应ETF的持仓数量
- 给出当前操作指导
  - 如果沪深300/中证500 ETF持仓数量大于0，且它们各自当前的收盘价小于20天前收盘价，那么建议“卖出”
  - 如果沪深300涨幅大于中证500涨幅，且当前空仓，那么建议买入“沪深300ETF”
  - 如果中证500涨幅大于沪深300涨幅，且当前空仓，那么建议买入“中证500ETF”

最后是根据操作指导来买卖股票：

- 建议“卖出”，那么卖出当前所有持仓证券
- 建议“沪深300ETF”，那么用当前持有的现金买入所有沪深300ETF
- 建议“中证500ETF”，那么用当前持有的现金买入所有中证500ETF

**收盘后的工作**

```
def after_trading_end(context):
    return
```

`after_trading_end()`是在每次收盘后系统调用的。我们可以说before_trading_start/handle_data/after_trading_end这三个函数是按天/分/tick进行交易需要使用到的，而run_daily/run_weekly/run_monthly是按天/周/月进行交易需要使用的。这两组重合的部分是“按天交易”，这个时候使用哪种就需要在明确它们之间的区别上根据自己的使用习惯和具体场景来选择。


## 二、上周计划任务

开始从[聚宽2019年度评选+精选文章合集](https://www.joinquant.com/view/community/detail/5fea4e17fa8ad5eb32b85201375e2669?type=1)选择第2篇文章来学习，这次选择@东南有大树写的[用指数战胜指数，ETF二八轮动对冲模型](https://www.joinquant.com/view/community/detail/19490)。


## 三、本周新学内容

### 1.大盘股、中小盘股的分类

@东南有大树在[用指数战胜指数，ETF二八轮动对冲模型](https://www.joinquant.com/view/community/detail/19490)里面提到了大盘股和小盘股的如下概念：

>“二八轮动”就是根据A股市场中大盘股和小盘股走势不同作为信号判断的。（所谓二，就是指数量占20%的大盘股、权重股；所谓的八,就是数量占80%左右的中小盘股，非权重股；其轮动就是指在两者之间不断切换，轮流持有。） 大盘股和小盘股的区分就是根据公司的流通股本的多少，大盘股通常指流通股本大于1亿的上市公司股票，而小盘股则与大盘股相对，通常指流通股本不足3000万的股票。沪深300通常可以近似表示大盘股的整体走势，中证500指数近似表示小盘股的整体走势。

这让我想起了上上周读完的江湖LAOK 季凯帆2008年写的《解读基金》，里面有对大中小盘指数的定义，摘录如下：

- 中证100指数：在沪深300指数成分股中选择市值最大的100支股票组成的指数。这是沪深两市市值
最大的100支股票，大概覆盖了A股流动市值的50%。这个指数实际上就是A股市场的大盘股票指数。
- 中证200指数：在沪深300中扣除中证100剩下的200支股票组成的支出，它们大概占了A股市值50%
到70%中间的20%部分。中证200指数被认为是中盘股指数。
- 中证500指数：A股中排在沪深300以后的500支股票组成的指数，它们大约构成了A股市值从70%到
90%中间的20%部分，认为是小盘股指数。

这些概念虽然简单，但是对于理解国内的证券市场还是挺重要的。

### 2.获取指数市盈率的另一种方法

在前面的学习里面已经接触到三种计算指数市盈率的方法：

1. [周记五](https://www.joinquant.com/view/community/detail/99a6ea4179cfa056552d3567b3387bc6)里面提到的使用共享函数`get_zz_quote()`从聚源数据库里面获取[中证指数行情 - QT_CSIIndexQuote](https://www.joinquant.com/help/data/data?name=jy#nodeId=63)来得到中证相关指数市盈率。
2. [周记九](https://www.joinquant.com/view/community/detail/ec5acca99671b1a70d78296829324ae1)里面自己仿照共享函数`get_zz_quote()`编写的从聚源数据库里获取[指数估值指标 - LC_IndexDerivative](https://www.joinquant.com/help/data/data?name=jy#nodeId=67)来得到中证系列指数外的市盈率。
3. [周记十一](https://www.joinquant.com/view/community/detail/6f4ec5802b1710be8e39248afec64a64)里面学习@Gyro策略时候他使用的手动计算方法。

这次在读@东南有大树这篇文章时恍然大悟，原来我们可以直接像获取股票[“市值数据”](https://www.joinquant.com/help/api/help?name=Stock#%E5%B8%82%E5%80%BC%E6%95%B0%E6%8D%AE)那样直接获取到指数的市盈率，确实让人眼前一亮：我怎么之前就没有想到呢？！

### 3.量化投资的基本思想

在引用的聚宽官方推出的[【量化课堂】斗牛蛋卷二八轮动原版策略实现](https://www.joinquant.com/view/community/detail/9434c4a9c9482c7d1071be947dd3558a?type=1)里面提到：

> 虽然这是两种极不靠谱的交易策略，但其中蕴含了量化投资中如何发现趋势的基本思想。第一种交易是典型的动量策略，即根据涨跌趋势都会继续保持的特点，继续买入持续上涨股票，卖出下跌股票——用通俗的话来讲，就是“追涨杀跌”。第二种交易是典型的反转策略，即认为股票价值是被低估的，在未来的时间内会出现均值回归，就是所谓的“低吸高抛”。

简单解释，其中解释了量化的基本思想，其实这种思想是投资界所共享的，并不一定属于量化所特有。接触量化几个月觉得量化独有的特征包括但不限于：

- 能够通过计算机技术更便利来提高交易的便捷性
- 从海量的交易数据里提取特征，然后应用数学、计算机科学的算法来提供新的交易参考

## 四、下周学习任务
