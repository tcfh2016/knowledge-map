import numpy as np
import pandas as pd

a = np.random.standard_normal((9, 4)).round(6)
print(a)

df = pd.DataFrame(a)
print(df)

df.columns = ['No1', 'No2', 'No3', 'No4'] # 更改列名。
print(df['No2'][3]) # 打印第2列第3行的数据

dates = pd.date_range('2015-1-1', periods=9, freq='M')
df.index = dates
print(df)
