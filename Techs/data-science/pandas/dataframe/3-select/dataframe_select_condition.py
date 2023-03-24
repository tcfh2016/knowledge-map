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

# 选择行
print("按行名选择列：")
print(df.loc['b'])
print("按行名选择多行：")
print(df.loc[['a', 'b']])
print("按行名切片选择多行：")
print(df['a':'c'])
print("按行数字索引选择多行：")
print(df.loc[df.index[0:3]])

print("按列数字索引选择多行：")
print(df[0:1])

print("按列数字索引选择多行：")
print(df[0:1])

print("按条件选择行例1：")
print(df[df.floats > 3.0]) # 选择列'floats'值大于3.0的那些行

print("按条件选择行例2：")
conditions = []
for f in df.floats:
    if f > 3.0:
        conditions.append(True)
    else:
        conditions.append(False)
print(df[conditions])
match_condition = pd.Series(conditions, index=df.index)
print(df[match_condition])

print("按条件选择行例3：")
condition = df.floats > 3.0
print(df[condition])
