
# random

Python自带的random模块用来生成伪随机数。它支持统一正态、标准正态分布（高斯）、对数正态分
布等。

### random.gauss(mu, sigma)

生成满足高斯分布的伪随机数：mu代表均值，sigma代表标准差。

```
from random import gauss
a = [gauss(1.5, 2) for i in range(1000000)]
```
