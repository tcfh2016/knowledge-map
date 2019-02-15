pop = [1.0, 2.3, 3.5, 4.6, 5.9, 7.0, 9.2, 12.1, 16.6]
pop2 = [10, 23, 35, 46, 59, 70, 92, 121, 166]

import matplotlib.pyplot as plt

plt.hist(pop, 2)
plt.show()
plt.clf()

plt.hist(pop2, 50)
plt.show()
plt.clf()
