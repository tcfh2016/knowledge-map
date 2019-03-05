import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(1000)
y = np.random.standard_normal(20)
x = range(len(y))
print(y)

plt.plot(x, y)
plt.plot(y.cumsum())

plt.show()
