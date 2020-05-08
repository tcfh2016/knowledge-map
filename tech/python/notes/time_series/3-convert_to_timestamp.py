import pandas as pd

d = pd.to_datetime('2010/11/12')
print(d)
print(type(d))
print(isinstance(d, pd.Timestamp))
