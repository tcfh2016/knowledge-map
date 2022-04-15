import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "name": ["Joe", "Sally", "Ananya"],
    "score": np.random.randint(0,100,size=3)})
print(df)
df.plot(x='name')

df1 = pd.DataFrame({
    "name": ["2013-12-31", "2014-12-31", "2015-12-31"],
    "score": np.random.randint(0,100,size=3),
    "score2": np.random.randint(0,1,size=3)})
print(df1)
df1.plot(x='name')

plt.show()
