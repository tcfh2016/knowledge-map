# 聚宽学习第四周周记：获取中证指数行情

## 一、`获取中证指数行情`代码解释

原版代码见[聚宽已有的共享函数](https://www.joinquant.com/view/community/detail/16656)。

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
```

效果图如下：

![]()

**代码片段一：**

```
if isinstance(code,str):
    code=[code]
code.sort()

code = [x[:6] for x in code]
days = get_trade_days(start_date,end_date,count)
```

第一句`isinstance()`是Python的内建函数，用来判断对象的类型，比如`isinstance(code, str)`表示判断code是否为str(字符串类型)。第二句的处理是如果code为str类型，那么将其转化为list（列表）类型，这是因为`get_zz_quote()`函数默认支持查询多个标的的数据，所以传入的标的要求为列表类型，为了支持使用者仅仅查询一个标的，才有了这一步转换。之后调用`sort()`对列表里面的代码进行升序排列。

`[x[:6] for x in code]`是对包含代码的列表进行规整处理，因为聚宽服务里使用的股票/指数代码是“数字+后缀”的格式，比如000905.XSHG。但在使用聚源数据库提供的服务时，使用的代码仅仅包含数字。所以这一句代码相当于将列表里面标的代码的后缀抹去。

最后一句`get_trade_days()`之前在[第三周的周记](https://www.joinquant.com/view/community/detail/dea963ac96739ecd008c52cba3819d0c)提到过，它是在jqdata里面定义的用来获取指定日期内的所有交易日，这个函数会自动去除起止日期和结束日期中间的非交易日。

*注：需要区分“聚宽”和“聚源”，前者是聚宽平台，后者指的是聚源数据库，它是一个独立于聚宽平台的金融数据提供商，由上海恒生聚源数据服务有限公司开发和维护。*

**代码片段二：**

```
code_df = jy.run_query(query(
     jy.SecuMain.InnerCode,jy.SecuMain.SecuCode,jy.SecuMain.ChiName
    ).filter(
    jy.SecuMain.SecuCode.in_(code)).order_by(jy.SecuMain.SecuCode))
```

这段代码里使用了`query对象`，在[周记二](https://www.joinquant.com/view/community/detail/3cc22ef4218363686917d718ba90f4f8)里对query对象进行过大致的了解，它是用来简化数据库的查询过程的，被初始化的query对象最终会被翻译为对应的SQL语句来完成数据库的查询过程。

这里的查询操作主要针对`SecuMain`，要明白这个字段的含义在聚宽上的“聚源数据”专页最上方的搜索栏进行搜索，可以得知它对应的是“证券主表”，里面收录单个证券品种（股票、基金、债券）的代码、简称、上市交易所等基础信息。代码里面使用到的`InnerCode`/`SecuCode`/`ChiName`分别表示`证券内部编码`/`证券代码`/`中文名称`。

综上，我们可以理解这段代码的意思为：

- 从证券主表（SecuMain）里面查询在`code`列表里面指定的那些证券代码的“基本信息”
- 这些信息有三种：证券内部编码、证券代码和中文名称
- 获取的信息以证券代码排序展示（默认升序）

如果我们单独执行上面这段代码：

```
from jqdata import jy

code = ['000905.XSHG']
code = [x[:6] for x in code]
code_df = jy.run_query(query(
     jy.SecuMain.InnerCode,jy.SecuMain.SecuCode,jy.SecuMain.ChiName
    ).filter(
    jy.SecuMain.SecuCode.in_(code)).order_by(jy.SecuMain.SecuCode))

输出为：
  InnerCode SecuCode       ChiName
  0        535   000905  厦门港务发展股份有限公司
  1       4978   000905     中证小盘500指数
  2      43044   000905   鹏华安盈宝货币市场基金
```

可见一个证券编码可能对应多个不同实体。

**代码片段三：**

```
df = jy.run_query(query(
         jy.QT_CSIIndexQuote).filter(
        jy.QT_CSIIndexQuote.IndexCode.in_(code_df.InnerCode),
        jy.QT_CSIIndexQuote.TradingDay.in_(days),
        ))
```

这里又是另外一条查询语句，主要针对`QT_CSIIndexQuote`，这个对象用于查询“中证指数行情”，详细的细节可以从[中证指数行情 - QT_CSIIndexQuote](https://www.joinquant.com/help/data/data?name=jy#nodeId=63)查看到，它代表的含义为：

- 从中证指数行情表（QT_CSIIndexQuote）里面查询在`code_df.InnerCode`列表里面指定的那些证券代码的“行情信息”
- 同时指定获取的时间范围

尽管在`code_df.InnerCode`列表里面对于同一个“证券代码”可能包括多个不同证券的“证券内部编码”，但由于当前查询的是中证指数行情，所以仅仅会选中“中证小盘500指数”的记录。下面的代码是同时指定了两个指数代码：

```
from jqdata import *

code = ['000905.XSHG', '000903.XSHG']
code = [x[:6] for x in code]
days = get_trade_days(end_date='2020-01-10', count=3)

code_df = jy.run_query(query(
     jy.SecuMain.InnerCode,jy.SecuMain.SecuCode,jy.SecuMain.ChiName
    ).filter(
    jy.SecuMain.SecuCode.in_(code)).order_by(jy.SecuMain.SecuCode))
df = jy.run_query(query(
         jy.QT_CSIIndexQuote).filter(
        jy.QT_CSIIndexQuote.IndexCode.in_(code_df.InnerCode),
        jy.QT_CSIIndexQuote.TradingDay.in_(days),
        ))

输出的证券信息为：
     InnerCode SecuCode         ChiName
  0        534   000903    昆明云内动力股份有限公司
  1       4293   000903         中证100指数
  2      41360   000903  新华活期添利货币市场基金A类
  3        535   000905    厦门港务发展股份有限公司
  4       4978   000905       中证小盘500指数
  5      43044   000905     鹏华安盈宝货币市场基金

输出的行情数据为：

               ID  IndexCode      ...                JSID PrevClosePrice
  0  631818958856       4293      ...        631871451753      4351.4348
  1  631818957259       4978      ...        631871451767      5499.8395
  2  631909904379       4293      ...        631958257263      4305.1009
  3  631909904383       4978      ...        631958257268      5423.7966
  4  631992328243       4293      ...        632044217571      4358.5678
  5  631992328247       4978      ...        632044217573      5497.5429
```

当指定多个证券代码进行查询的时候，展示的结果会先按证券再按时间顺序进行排列。


**代码片段四：**

```
df2  = pd.merge(code_df, df, left_on='InnerCode',right_on='IndexCode').set_index(['TradingDay','SecuCode'])
```

Pandas提供的`merge()`用来完成数据库操作中的表合并操作（JOIN），理解这个东西就需要基本的数据库概念了（突然发现虽然工作中极少使用数据库，但上课学的一点数据库基本理论还是有点用处的）。

上面的代码是将获取到的`code_df`和`df`两张二维表数据进行合并，合并基于证券内部代码作为键值，同时设定新的列作为合并之后新表（DataFrame）的索引（index）。

```
                     InnerCode      ...       PrevClosePrice
TradingDay SecuCode                 ...                     
2020-01-08 000903         4293      ...            4351.4348
2020-01-09 000903         4293      ...            4305.1009
2020-01-10 000903         4293      ...            4358.5678
2020-01-08 000905         4978      ...            5499.8395
2020-01-09 000905         4978      ...            5423.7966
2020-01-10 000905         4978      ...            5497.5429
```

**代码片段五：**

```
df2.drop(['InnerCode','IndexCode','ID','UpdateTime','JSID','OpenInterest','SettleValue','IndexCSIType'],axis=1,inplace=True)
return df2.to_panel()
```

由于合并之后的表格包含有许多列数据，有些我们不感兴趣，所以这里使用`drop()`函数将其中的某些列丢弃掉，最后再将二维表（DataFrame类型）转换为三维表（Panel类型）。


## 二、上周计划任务

### 1.理解获取中证指数市盈率的共享函数，并且看是否可以修改不再使用panel。

经过上面的理解之后，结合在[周记二](https://www.joinquant.com/view/community/detail/3cc22ef4218363686917d718ba90f4f8)里面讲解过Panel数据的处理，我们可以使用`pivot`来替代`panel`。

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

### [推迟任务]3.开始了解聚宽因子


## 三、本周新学知识


## 四、下周预定主题
