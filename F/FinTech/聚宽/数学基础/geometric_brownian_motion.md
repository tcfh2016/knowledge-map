# 几何布朗运动（GBM，Geometric Brownian motion）

几何布朗运动，也称为“指数布朗运动”，是一种连续随机过程，其中随机变量的对数跟随波浪运动飘逸，满足随机微分方程（SDE）。在数学金融里，它应用在Black-Scholes模型中建模股票价格。

金融领域建模的不足之处：

- 真实股票价格的波动也会跟随时间而变化（随机），但在GBM里面波动率是常数。
- 真实股票价格可能因为不可预测的事件或者消息跳空，但在GBM里面是连续的。

参考：

- [Geometric Brownian motion](https://en.wikipedia.org/wiki/Geometric_Brownian_motion)
