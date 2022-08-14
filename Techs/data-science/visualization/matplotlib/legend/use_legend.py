import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series(np.random.randn(100), index=np.arange(100))

plt.plot(s, label='random100')
plt.legend(loc=0)
plt.show()
