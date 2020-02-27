# 聚宽学习第九周周记：


## 一、` ` 代码解释

```
```


**代码片段一：**

```
```


**代码片段二：**

```
```


**代码片段三：**

```
```


**代码片段四：**

```
```


**代码片段五：**

```
```


## 二、上周计划任务

### 1.写函数统计基金的成交量，提供按天、月为单位进行统计。

保存在聚宽研究模块里面，但今天似乎还在维护一直无法访问，下周周报里面再放吧。

### 2.如何获取创业板指数的市盈率？

聚宽“数据字典”中的“指数数据”并不包含市盈率方面的估值信息，想起中证500的估值是聚宽提供的共享函数去从聚源数据里面获取的（详细的介绍见[聚宽学习第五周周记：中证指数共享函数使用更新与策略指标的理解](https://www.joinquant.com/view/community/detail/99a6ea4179cfa056552d3567b3387bc6))，所以尝试着去查看[聚源数据](https://www.joinquant.com/help/data/data?name=jy)。在[指数估值指标 - LC_IndexDerivative](https://www.joinquant.com/help/data/data?name=jy#nodeId=67)页面可以看到：

![](./JQ_index_derivative_.PNG)

其中包含了“PE_TTM（动态市盈率）”。

```
# 获取指数估值指标，包括指数总市值、静态市盈率、动态市盈率、市净率、股息率等指标
#   TotalMV        -- 指数总市值(元)
#   PE_TTM         -- 动态市盈率
#   PE_LYR         -- 静态市盈率(LYR)
#   PB_LF          -- 市净率(LF)
#   DividendRatio  -- 股息率(%)
#   PCF_LYR        -- 静态市现率
#   PCF_TTM        -- 动态市现率
#   PS_LYR         -- 静态市销率
#   PS_TTM         -- 动态市销率

def get_index_derivative(code,start_date=None,end_date=None,count=None):
    if isinstance(code,str):
        code=[code]
    code.sort()

    code = [x[:6] for x in code]
    days = get_trade_days(start_date,end_date,count)

    basic_info_df = jy.run_query(query(
         jy.SecuMain.InnerCode,jy.SecuMain.SecuCode,jy.SecuMain.ChiName
        ).filter(
        jy.SecuMain.SecuCode.in_(code)).order_by(jy.SecuMain.SecuCode))
    #print(basic_info_df)

    derivative_info_df = jy.run_query(query(
             jy.LC_IndexDerivative).filter(
            jy.LC_IndexDerivative.IndexCode.in_(basic_info_df.InnerCode),
            jy.LC_IndexDerivative.TradingDay.in_(days),
            ))

    df = pd.merge(basic_info_df, derivative_info_df, left_on='InnerCode',right_on='IndexCode').set_index(['TradingDay','SecuCode'])
    df.drop(['InnerCode','IndexCode','ID','InsertTime','UpdateTime','JSID'],axis=1,inplace=True)
    return df
```

一个问题：这种方式获取的动态市盈率为什么和另外一种方式获取的有些差别呢？

### 3.聚宽里企业的年度营业收入增长率如何获得？

这是宽友 @freemars 的一个问题：

> 聚宽的 indicator.inc_revenue_year_on_year, 是（2019q3-2019q2）/(2018q3-2018q2)， 我想要的数据是财报里的 本年至今营收/去年同期营收, 我的选股条件是 营业收入增长率 ＞ 20%。 pe ＞ 15， pe ＜ 60， roe ＞ 15， 每天选股，按照 roe 从 大到小 排序。 排序这个我可以搞定，前面那个选股条件我搞不定

这个问题之后和freemars讨论他的问题在于在获取股票对应的年营业收入增长率的时候获取到的是季度的营业收入增长率，比如2019年9月份获取到的是2019年半年度的营业收入增长率，2020年2月份的获取到的是2019年三季度的数据，这一点在[财务指标数据](https://www.joinquant.com/help/api/help?name=Stock#%E8%B4%A2%E5%8A%A1%E6%8C%87%E6%A0%87%E6%95%B0%E6%8D%AE)里面有说明，上面的提示信息是`按季度更新, 统计周期是一季度。可以使用get_fundamentals() 的statDate参数查询年度数据。`

在聚宽API的[数据获取函数](https://www.joinquant.com/help/api/help?name=api#%E6%95%B0%E6%8D%AE%E8%8E%B7%E5%8F%96%E5%87%BD%E6%95%B0)章节，有对查询财务数据的函数`get_fundamentals()`的说明：

```
get_fundamentals(query_object, date=None, statDate=None)

date和statDate参数只能传入一个:

- 传入date时, 查询指定日期date收盘后所能看到的最近(对市值表来说, 最近一天, 对其他表来说, 最近一个季度)的数据, 我们会查找上市公司在这个日期之前(包括此日期)发布的数据, 不会有未来函数.
- 传入statDate时, 查询 statDate 指定的季度或者年份的财务数据. 注意:


statDate: 财报统计的季度或者年份, 一个字符串, 有两种格式:

1. 季度: 格式是: 年 + 'q' + 季度序号, 例如: '2015q1', '2013q4'.
2. 年份: 格式就是年份的数字, 例如: '2015', '2016'.
```


### 4.开始新的学习计划：学习聚宽社区2019年度评选文章

## 三、本周新学内容

## 四、下周学习任务
