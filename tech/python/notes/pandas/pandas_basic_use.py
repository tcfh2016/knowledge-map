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
