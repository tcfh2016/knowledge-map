import pandas as pd
import numpy as np

s = pd.Series(range(-4, 3))
print(s)

print(s > 0)
print(s[s > 0])
print(s[(s > -2) & (s < 2)])

print (s.isin([-1, 0, 1]))
print (s[s.isin([-1, 0, 1])])

df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)
print(df[df > 0])
print(df['A'] > 0)
print(df[df['A'] > 0])
