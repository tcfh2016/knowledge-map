# 聚宽学习周记十八：详解@东南有大树的“指数估值自动报表系统”（下）


## 一、代码解释


## 二、上周计划任务


### 1. 继续完善[指数估值自动报表系统——源代码](https://www.joinquant.com/view/community/detail/20497)里自动报表系统的改写，功能完成之后看是否能够在布局上做得更美观一点。

```
File "/tmp/strategy/user_code.py", line 1, in <module>
  from repotool.valuationlib import *
File "/tmp/jqcore/jqboson/jqboson/plugin/web.py", line 62, in import_
  raise ImportError('您是否想导入研究中的自定义库? 自定义库暂时不支持文件夹, 请把库文件放在研究根目录: {}'.format(name))
ImportError: 您是否想导入研究中的自定义库? 自定义库暂时不支持文件夹, 请把库文件放在研究根目录: repotool.valuationlib
```

### 2. 在理解函数`send_message()`的时候发现聚宽本身定义了这个函数用来发送微信消息，当前自己在进行ETF定投，都是使用聚源数据提供的指数估值来进行决策，受这篇文章的启发其实可以尝试手动计算当前指数的估值，这样每天就可以实时掌握指数的估值状态了。


## 三、本周新学内容


## 四、下周学习任务

### 1. 爬取所有指数的估值状态？前50位。
