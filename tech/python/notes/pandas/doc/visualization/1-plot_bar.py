import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DataFrame绘图
td = pd.DataFrame(np.random.randn(10,3),
                  index=pd.date_range('2000-01-01', periods=10),
                  columns=list('ABC'))
td = td.cumsum()

#td.iloc[2].plot(kind='bar')
td.iloc[2].plot.bar()
td.plot.bar()
td.plot.bar(stacked=True)  # 堆叠形式的条形图
td.plot.barh(stacked=True)  # 堆叠形式的条形图，水平形式

plt.show()
