import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt


S0 = 100
r = 0.05
sigma = 0.25
T = 2.0
I = 10000

ST1 = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * npr.standard_normal(I))

plt.hist(ST1, bins=50)
plt.xlabel('index level')
plt.ylabel('frequency')
plt.grid(True)

plt.show()
