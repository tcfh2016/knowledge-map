# 聚宽学习周记十九：


## 一、从“策略研究”模块到“模拟交易”模块的切换



## 二、上周计划任务

### 1. 尝试完成上周布置的两个任务。

### 2. 另外一个想法是扩大指数估值的统计范围，从当前支持的20只指数扩展到所有指数，然后取前50位。

A. 继续完善[指数估值自动报表系统——源代码](https://www.joinquant.com/view/community/detail/20497)里自动报表系统的改写，功能完成之后看是否能够在布局上做得更美观一点。


B. 在理解函数`send_message()`的时候发现聚宽本身定义了这个函数用来发送微信消息，当前自己在进行ETF定投，都是使用聚源数据提供的指数估值来进行决策，受这篇文章的启发其实可以尝试手动计算当前指数的估值，这样每天就可以实时掌握指数的估值状态了。


## 三、本周新学内容

### 如何

参考：

- [JoinQuant 心得——数据存取](https://www.joinquant.com/view/community/detail/1856fb977f1306b847882a138837d7d2)
- [【有用功】在回测及模拟交易中读取/写入研究中不同格式的文件](https://www.joinquant.com/view/community/detail/b048a3e848d190ad810c3930fb07a4dc)

### 调试时的问题

1. `000003.XSHG`调用`get_index_stocks`无法获取到指数成分股数据，因此添加过滤条件。

2. `000011.XSHG`为“基金指数”，怎么选择普通股指数？

```
def is_only_stock(index):
    securities = get_index_stocks(index)
    if (len(securities) > 0):    
        info = get_security_info(securities[0])        
        return (info.type == 'stock')
    return False
```

3. 函数`calc_index_valuation()`里面需要增加对于获取到的估值数据为空的处理。比如“000976.XSHG（新华金牛）”只有2014-02-18到2017-04-27的记录。

```
def calc_index_valuation(index_code, start_date, end_date=datetime.datetime.now().date() - datetime.timedelta(days=1)):
```

4. 重复记录

```
2020-04-28 00:00:00,1.81915,26.00605
2020-04-29 00:00:00,1.8317,24.6627
2020-04-30 00:00:00,1.85665,22.605999999999998
2020-04-30 00:00:00,1.85665,22.606
2020-04-30 00:00:00,1.85665,22.605999999999998
```

## 四、下周学习任务
