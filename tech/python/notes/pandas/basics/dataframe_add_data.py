import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])
df['floats'] = (1.5, 2.5, 3.5, 4.5)
df['names1'] = ('Yves', 'Guido', 'Felix', 'Francesc')
df['names2'] = pd.DataFrame(['Yv', 'Gu', 'Fe', 'Fr'],
                            index=['d', 'a', 'b', 'c']) # 添加新的DataFrame对象。
print(df)

# Missing Data
ms = df.join(pd.DataFrame([1, 4, 9, 16],
                          index=['a', 'b', 'c', 'y'],
                          columns=['squares',]))
print(ms)

ms = df.join(pd.DataFrame([1, 4, 9, 16],
                             index=['a', 'b', 'c', 'y'],
                             columns=['squares',]),
                             how='outer')
print(ms)
