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

# 添加一列
df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
groups = df.groupby('Quarter')
print(groups.mean())
print(groups.max())
print(groups.size())

df['Odd_Even'] = ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
groups = df.groupby(['Quarter', 'Odd_Even'])
print(groups.size())
