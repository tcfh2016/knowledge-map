# 聚宽学习周记二一：ETF投资参考日报

本周围绕“历史百分位”这个概念将ETF定投里面的“ETF筛选”和“全网估值”分别进行了更新，同时也对生成的HTML页面内容进行了稍许的美化。收到邮件时候的效果如下：

![](./w21-new-page-content.png)

下周会将新的研究内容发布到模拟策略里面每天进行估值测算并完成邮件递送工作。目前为止这些内容都得益于下面两位宽友：

- @Gyro 和他的《[价值低波（中）-- 市盈率研究](https://www.joinquant.com/view/community/detail/328831058b45f5f1080914aaea6e0d09)》，从中我学习到了如何计算指数的市盈率。
- @东南有大树 和他的《[指数估值自动报表系统——源代码](https://www.joinquant.com/view/community/detail/20497)》，从中我学习到了如何百分比的概念，以及如何使用Python来进行自动报表的递送，另外还有一些比较细节的Python知识点。让自己再学习了HTML重新来调整版面。

因此，我将重构之后的代码附加在研究中，供有兴趣的宽友进一步整理和发挥。目前报表里面的内容主要包括两个：

- ETF的选择策略。主要遵照如下思路：

  1. 过滤出2014年1月1日之前发行的并且前一个交易日仍旧在交易，且日均成交量大于5万手的所有ETF。
  2. 对于选取的每只ETF，分别计算两个指标：
      a, “前一个交易日的累计净值” 除以 “该只基金发行以来累计净值的最高值”。
      b, “前一个交易日的累计净值” 在近5年的历史百分位。
  3. 按照 b,a两个指标进行从小到大排序，并以此为优先级进行选择。

- 全网指数的估值。估值主要按照市盈率近5年的历史百分位进行，详细内容已经发布在上周笔记：[聚宽学习周记二十：指数基金定投实践的估值调整](https://www.joinquant.com/view/community/detail/033d0930c64633db7d266dc0c32eff63)

如果需要将研究内容发布到模拟实盘进行每日邮件发送估值报表，可以参考@东南有大树 和他的《[指数估值自动报表系统——源代码](https://www.joinquant.com/view/community/detail/20497)》。


## 下周计划

在第15周曾经布置了下面的学习计划：

```
学习到了“波动”、“指数市盈率”、“大中小盘股”、“指数ETF轮动”、“动量”等概念，因此决定趁热打铁，下周的学习依然围绕着这些新接触的概念开展，和这些概念相关的有如下几篇：

- [相信波动率还是相信基本面？波动与估值因子A股驱动力测试](https://www.joinquant.com/view/community/detail/17255)
- [小盘价值股策略2.01，年化131%，回撤8.8%](https://www.joinquant.com/view/community/detail/16755)
- [高频因子探索——动量交易](https://www.joinquant.com/view/community/detail/22472)
- [指数估值自动报表系统——源代码](https://www.joinquant.com/view/community/detail/20497)
- [波动率因子在A股市场探索](https://www.joinquant.com/view/community/detail/2c6ae14a9e675394762eb24061e6207c)
```

这几周都在学习[指数估值自动报表系统——源代码](https://www.joinquant.com/view/community/detail/20497)，目前有心根据当前的思考尝试制定ETF策略，因此决定先选择上面的[高频因子探索——动量交易](https://www.joinquant.com/view/community/detail/22472)看看。
