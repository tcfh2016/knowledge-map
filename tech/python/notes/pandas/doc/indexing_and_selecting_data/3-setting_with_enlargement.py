import pandas as pd
import numpy as np

s = pd.Series([4, 2, 1, 0], index=['a', 'b', 'c', 'd'])
print(s)

s['e'] = 100
print(s)

df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)

df['E'] = 10
print(df)
df.loc[:, 'E'] = 12
print(df)
