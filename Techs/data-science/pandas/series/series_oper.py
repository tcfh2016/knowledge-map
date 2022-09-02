import pandas as pd

my_d = {'a': 1000, 'b': 2000, 'c': 500}
my_s = pd.Series(my_d)

# 最大值的索引
print(my_s.idxmax())
print(type(my_s.idxmax()))
