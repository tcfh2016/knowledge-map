import pandas as pd
import numpy as np

n = 10
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
print(df)

df_select = df[(df.a < df.b) & (df.b < df.c)]
print(df_select)

df_query = df.query('(a < b) & (b < c)')
print(df_query)

print(df.query('index > 2'))
