import pandas as pd
import numpy as np

s = pd.Series([4, 2, 1, 0], index=['a', 'b', 'c', 'd'])
print(s[:2])
print(s[::3])
print(s[::-1])


dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

print(df['A'])
print(df.A)
print(df[['A', 'B']])
print(df[::-1])
print(df[1:2])
print(df.loc['2000-01-01':'2000-01-02'])
print(df.iloc[0:1])
