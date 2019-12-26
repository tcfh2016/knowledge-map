import pandas as pd
import numpy as np
import pandas.util.testing as tm

tm.N = 3
'''
创建3行的测试数据：
                   A         B         C         D
2000-01-03 -0.959954  0.847779  0.367563 -0.078667
2000-01-04 -0.023550  0.032854 -0.672666  0.427653
2000-01-05  0.042094  0.873816  1.695094 -0.063146
'''

def unpivot(frame):
    N, K = frame.shape
    data = {'value': frame.to_numpy().ravel('F'),
            'variable': np.asarray(frame.columns).repeat(N),
            'date': np.tile(np.asarray(frame.index), K)}
    return pd.DataFrame(data, columns=['date', 'variable', 'value'])

print(tm.makeTimeDataFrame().shape)
df = unpivot(tm.makeTimeDataFrame())
print(df)

# 选择满足特定条件的行
specified_rows = df[df['variable'] == 'A']
print(type(specified_rows))
print(specified_rows)

# 使用pivot
pivot = df.pivot(index='date', columns='variable', values='value')
print(pivot)
pivot_without_value = df.pivot(index='date', columns='variable')
print(pivot_without_value)
