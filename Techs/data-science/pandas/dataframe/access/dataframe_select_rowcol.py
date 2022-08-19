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


print("按行名、列名选择区块：")
print(df.loc[['b', 'c'], ['numbers']])

print("按行、列索引选择单个元素：")
print(df.iloc[1, 1])
print(df.iloc[1][1])

print("按行、列索引选择区块：")
print(df.iloc[1:3, 1])
print(df.iloc[1:3, 1:3])
print(df.iloc[1:3, [1,2]])
