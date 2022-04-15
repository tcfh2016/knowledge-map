import pandas as pd
import numpy as np

df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                   ('bird', 'Psittaciformes', 24.0),
                   ('mammal', 'Carnivora', 80.2),
                   ('mammal', 'Primates', np.nan),
                   ('mammal', 'Carnivora', 58)],
                  index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                  columns=('class', 'order', 'max_speed'))
print(df)

grouped = df.groupby('class')
print(grouped)
print(grouped.first())
print(grouped.get_group('bird'))

print("all groups information:")
for name, group in grouped:
    print(name)
    print(group)
