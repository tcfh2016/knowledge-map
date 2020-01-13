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

**代码片段二：**

```
code_df = jy.run_query(query(
     jy.SecuMain.InnerCode,jy.SecuMain.SecuCode,jy.SecuMain.ChiName
    ).filter(
    jy.SecuMain.SecuCode.in_(code)).order_by(jy.SecuMain.SecuCode))
```

**代码片段三：**

```
df = jy.run_query(query(
         jy.QT_CSIIndexQuote).filter(
        jy.QT_CSIIndexQuote.IndexCode.in_(code_df.InnerCode),
        jy.QT_CSIIndexQuote.TradingDay.in_(days),
        ))
```

**代码片段四：**

```
df2  = pd.merge(code_df, df, left_on='InnerCode',right_on='IndexCode').set_index(['TradingDay','SecuCode'])
```

**代码片段五：**

```
df2.drop(['InnerCode','IndexCode','ID','UpdateTime','JSID','OpenInterest','SettleValue','IndexCSIType'],axis=1,inplace=True)
return df2.to_panel()
```

## 二、上周计划任务

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

### [推迟任务]3.开始了解聚宽因子


## 三、本周新学知识


## 四、下周预定主题
