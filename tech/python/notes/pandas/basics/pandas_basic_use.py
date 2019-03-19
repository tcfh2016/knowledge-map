import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])
print(df)
print(df.index)
print(df.columns)
print(df.loc['b']) # 通过索引访问元素，之前是df.ix['b']，但已经不推荐使用旧的方法。
print(df.loc[['a', 'b']]) # 索引多个元素。
print(df.loc[df.index[0:3]]) # 使用index对象来索引多个元素。
print(df.sum()) # 对每列求和
print(df.apply(lambda x: x**2)) # 对每个元素求平方

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
