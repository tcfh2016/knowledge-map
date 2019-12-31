import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series绘图
ts = pd.Series(np.random.randn(1000), index=pd.date_range('2000-01-01', periods=1000))
ts = ts.cumsum()
ts.plot()

# DataFrame绘图
td = pd.DataFrame(np.random.randn(1000,3),
                  index=pd.date_range('2000-01-01', periods=1000),
                  columns=list('ABC'))
td = td.cumsum()
td.plot()

# 指定某列做为x轴
td2 = pd.DataFrame(np.random.randn(1000,3),
                  index=pd.date_range('2000-01-01', periods=1000),
                  columns=list('ABC'))
td2 = td2.cumsum()
td2['D'] = pd.Series(list(range(len(td))), index=td2.index)
td2.plot(x='D', y='C')

plt.show()
#print(ts)
