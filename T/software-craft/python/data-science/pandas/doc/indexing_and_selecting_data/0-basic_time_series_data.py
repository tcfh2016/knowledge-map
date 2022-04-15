import pandas as pd
import numpy as np

s = pd.Series([4,2,1,0], index=['a', 'b', 'c', 'd'])
print(s['a'])
print(s.b)


dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

print(df['A'])
print(df.A)
print(df[['A', 'B']])
