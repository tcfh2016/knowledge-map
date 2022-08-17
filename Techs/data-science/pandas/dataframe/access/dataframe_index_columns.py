import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])

# 打印index, columns的类型
print(df)
print("df.index:")
print(df.index)
print(list(df.index))
print("type of (df.index):{}".format(type(df.index)))
print("df.columns:")
print(df.columns)
print(list(df.columns))
print("type of (df.columns):{}".format(type(df.columns)))

# 获取数值索引对应行的名称
print(list(df.iloc[[0, 1, 3]].index))

# 添加新的列
df['floats'] = (1.5, 2.5, 3.5, 4.5)
df['names1'] = ('Yves', 'Guido', 'Felix', 'Francesc')
print("insert 2 new columns:")
print(df)

# 插入新的dataframe
df['names2'] = pd.DataFrame(['Yv', 'Gu', 'Fe', 'Fr'],
                            index=['d', 'a', 'b', 'c']) # 添加新的DataFrame对象。
print("insert 1 new dataframe:")
print(df)
