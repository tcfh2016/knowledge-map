## [pandas.DataFrame.cumprod](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.cumprod.html)

这个函数是用来计算"cumulative product"，计算的是累乘的值。对于DataFrame调用`df.cumprod()`会逐步迭代每行，然后按照列进行累积的计算，而使用`df.cumprod(axis=1)`则按列迭代，计算行内的累积。

参考：

- [numpy.cumprod() in Python](https://www.geeksforgeeks.org/numpy-cumprod-in-python/)