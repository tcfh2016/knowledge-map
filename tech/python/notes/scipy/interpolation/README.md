# [Interpolation](https://docs.scipy.org/doc/scipy/reference/interpolate.html)

插值处理专用子模块。

数学的数值分析领域中，插值是一种通过已知的、离散的数据点来推求新数据点的过程或方法。求解
科学和工程的问题时，通常有许多数据是由采样、实验等方法获得，这些数据可能代表了有限个数值
函数中自变量的值。而根据这些数据来推球一个连续的函数（曲线）或者更密集的离散方程与已知数
据相吻合的过程叫做拟合。

与插值密切相关的另一个问题是通过简单函数逼近复杂函数。假定给定函数的公式是已知的，但是太
复杂以至于不能有效进行评估，这时可以根据原始函数的一些已知数据点来使用较简单函数来产生插
值。当然，若使用一个简单函数来估计原始数据点时会出现插值误差，这取决于该问题领域和所使用
的插值方法。以简单函数推得插值数据，可能会导致精度损失更大。


参考：

- [插值](https://zh.wikipedia.org/zh/%E6%8F%92%E5%80%BC)

## Univariate interpolation

## Multivariate interpolation

## 1-D Splines

[scipy.interpolate.splrep](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splrep.html#scipy.interpolate.splrep)

scipy.interpolate.splrep(x, y, w=None, xb=None, xe=None, k=3, task=0, s=None, t=None, full_output=0, per=0, quiet=1)[source]

找到1-D曲线的符合B-spline的表示值。在给定(xi, yi)范围内找到xb <= x <= xe的k幂次的spline
近似值。比如：

```
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep

# 创建模拟数据集x, y
x = np.linspace(0, 10, 10)
y = np.sin(x)

# 获取近似值（似乎为系数？）
spl = splrep(x, y)

# 设定新的自变量数据集 x2
x2 = np.linspace(0, 10, 200)
# 产生新的因变量数据集 y2
y2 = splev(x2, spl)


plt.plot(x, y, 'o', x2, y2)
plt.show()
```

[scipy.interpolate.splev](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splev.html#scipy.interpolate.splev)

scipy.interpolate.splev(x, tck, der=0, ext=0)

评估B-spline或者它的派生值。给定自变量集合和B-spine表示法的系数，评估多项式的值和其派生
值。


## 2-D Splines

## Additional tools
