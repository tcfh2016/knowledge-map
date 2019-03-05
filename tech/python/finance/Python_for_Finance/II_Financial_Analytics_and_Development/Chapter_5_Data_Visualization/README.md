## Chapter 5. Data Visualization

matplotlib是与NumPy兼容良好的可视化函数库。

### Two-Dimensional Plotting

绘图相关函数主要存在于matplotlib的子函数库matplotlib.pyplot里， 绘图函数为
plot。

```
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
```

绘图时候需要同时传入x, y轴的数据（支持list和array），当省略x轴的数据时默认将
y轴数据的索引当作x轴引用数据。plot能够支持ndarray，但谨防传入过于复杂的数据。
