import pandas as pd
import numpy as np

# from_tuples
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print(index)
s = pd.Series(np.random.randn(8), index=index)

# from_product
iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]
index2 = pd.MultiIndex.from_product(iterables, names=['first', 'second'])
print(index2)

# from_frame
df = pd.DataFrame([['bar', 'one'], ['bar', 'two'],
                   ['foo', 'one'], ['foo', 'two']],
                  columns=['first', 'second'])
index3 = pd.MultiIndex.from_frame(df)
print(index3)
