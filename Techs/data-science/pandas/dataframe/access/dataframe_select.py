import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])

print(df)
print("df.index:{}".format(df.index))
print("type of (df.index):{}".format(type(df.index)))
print("df.columns:{}".format(df.columns))
print("type of (df.columns):{}".format(type(df.columns)))

df['floats'] = (1.5, 2.5, 3.5, 4.5)
df['names1'] = ('Yves', 'Guido', 'Felix', 'Francesc')
df['names2'] = pd.DataFrame(['Yv', 'Gu', 'Fe', 'Fr'],
                            index=['d', 'a', 'b', 'c']) # 添加新的DataFrame对象。
print(df)

# 索引
print("打印索引和列名：")
print(df.index)
print(df.columns)

# 选择行
print("不同方式选择行：")
print(df.loc['b']) # 通过索引访问元素，之前是df.ix['b']，但已经不推荐使用旧的方法。
print(df.loc[['a', 'b']]) # 索引多个元素。
print(df.loc[df.index[0:3]]) # 使用index对象来索引多个元素。
print(df['a':'c']) # 选择'a', 'b', 'c'三行
print(df[0:1]) # 选择第1列 —— 'a'。

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

# 选择列
print("不同方式选择列：")
print(df.names1)
print(df['names1'])
print(df[['names1','names2']])
