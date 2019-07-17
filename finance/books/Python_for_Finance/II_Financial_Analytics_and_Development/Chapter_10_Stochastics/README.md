# Chapter 10. Stochastics

20世纪70，80年代现代金融发端，金融研究的主要目标是为特定的金融模型提出封闭式的解决方案，
但近年来研究重点已经转向为整个衍生品市场提供持续的评估参考，因此预测学和蒙特卡罗模拟逐渐
成为主流了。

本章包括如下方面：

- Random number generation
- Simulation
- Valuation
- Risk measures

## Random Numbers

我们使用numpy.random子库来生成随机数，比如我们直接调用`np.random.rand(10)`来生成10个
符合均匀分布且值处于[0,1)的随机数。并且能够定制出符合其他范围的随机数：

```
import numpy.random as npr

a = 5.
b = 10.
npr.rand(10) * (b - a) + a
```
