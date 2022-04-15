import numpy as np
import pandas as pd

# 从列表创建，指定行、列索引
df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])
print(df)

# 添加新的列数据
df['floats'] = (1.5, 2.5, 3.5, 4.5)
df['names1'] = ('Yves', 'Guido', 'Felix', 'Francesc')
print(df)

# 以列为单位修改数据
df['floats'] = 2.0
print(df)
df.floats = 22.0
print(df)

# 从新的DataFrame对象直接添加。
df['names2'] = pd.DataFrame(['Yv', 'Gu', 'Fe', 'Fr'],
                            index=['d', 'a', 'b', 'c'])
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


# 删除某列
del df['names2']
print(df)
