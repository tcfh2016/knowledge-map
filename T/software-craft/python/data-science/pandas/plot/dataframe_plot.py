import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

a = np.random.standard_normal((9, 4)).round(6)
df = pd.DataFrame(a)

df.columns = ['No1', 'No2', 'No3', 'No4'] # 更改列名。
dates = pd.date_range('2015-1-1', periods=9, freq='M')
df.index = dates
print(df)

df.describe()

#%matplotlib inline # IPYTHON里面的魔法函数，此处不可用。
df.cumsum().plot(lw=2.0)

# 为No1列绘图
df['No1'].cumsum().plot(style='r', lw=2.)
plt.xlabel('date')
plt.ylabel('value')

plt.show()
