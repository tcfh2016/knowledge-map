from pandas import Series, DataFrame
import pandas as pd
import numpy as np

s = Series([1, np.NaN, 3.2, np.NaN, 7])
print(s)
print(s.dropna())

df = DataFrame([[1.2, 6.5, 3.0],
               [1., np.NaN, np.NaN],
               [np.NaN, np.NaN, np.NaN],
               [np.NaN, 6.2, 3.1]])
print(df)
print(df.dropna())
print(df.dropna(how='all'))
print(df.dropna(axis=1, how='all'))


print(df.fillna(0))
print(df.fillna({1:0.5, 2:1.0}))
