import pandas as pd

left = pd.DataFrame({'k': ['K0', 'K1', 'K1', 'K2'],
                     'lv': [1, 2, 3, 4],
                     's': ['a', 'b', 'c', 'd']})


right = pd.DataFrame({'k': ['K1', 'K2', 'K4'],
                      'rv': [1, 2, 3]})


merged_result = pd.merge_ordered(left, right, fill_method='ffill', left_by='s')
print(merged_result)
