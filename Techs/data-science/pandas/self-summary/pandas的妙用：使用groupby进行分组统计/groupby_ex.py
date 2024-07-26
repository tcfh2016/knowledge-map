import pandas as pd
import numpy as np

provinces = ["A", "B", "C", "D", "E"]
champion = pd.DataFrame({
    "province":[provinces[x] for x in np.random.randint(0, len(provinces), 9)],
    "language":np.random.randint(0, 12, 9),
    "math":np.random.randint(0, 12, 9)
})

print(champion)
