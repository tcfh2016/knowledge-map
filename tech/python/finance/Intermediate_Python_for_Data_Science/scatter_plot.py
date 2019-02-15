year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008]
pop = [1.0, 2.3, 3.5, 4.6, 5.9, 7.0, 9.2, 12.1, 16.6]

import matplotlib.pyplot as plt

plt.scatter(year, pop)
plt.xscale('log')
plt.show()
