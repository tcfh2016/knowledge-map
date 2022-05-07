import pandas as pd
from pandas import Series, DataFrame

obj = Series([4.2, 2.3, -1.3, 5.2], index=['d', 'b', 'c', 'a'])
print(obj)

obj1 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj1)

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print(obj2)
