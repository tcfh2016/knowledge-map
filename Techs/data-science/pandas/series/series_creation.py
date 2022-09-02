import pandas as pd

data = {'oli': 1000, 'tae': 2000, 'Oed': 500}
obj = pd.Series(data)

# s.values的类型
print(obj.values)
print(type(obj.values))

# s.index的类型
print(obj.index)
print(type(obj.index))

# 元素的类型
print(obj['tae'])
print(type(obj['tae']))
