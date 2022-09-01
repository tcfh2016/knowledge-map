## Plotting

我们可以使用`plot()`函数来为DataFrame画图，当然这个函数只是准备了图形需要的数据，我们还需要使用`matplotlib.pyplot`来将图形可视化。

```
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot()
plt.show()
```

## 画点图

使用`kind`参数可以指定想要画出的图形类型。在画点图时需要指定横纵坐标的数据集：

```
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
```

## 画直方图

直方图的参数为“hist”，直方图用来表达数据在特定范围内的频次，这个时候只需要单列的数据即可：

```
df["Duration"].plot(kind = 'hist')
```
