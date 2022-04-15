import pandas as pd
import numpy as np

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])


right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

join = left.join(right)
print(join)

join_with_outer = left.join(right, how='outer')
print(join_with_outer)

join_with_inner = left.join(right, how='inner')
print(join_with_inner)
