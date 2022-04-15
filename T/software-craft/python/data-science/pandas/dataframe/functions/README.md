# 常用函数

## [pandas.DataFrame.cumprod](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.cumprod.html)

这个函数是用来计算"cumulative product"，计算的是累乘的值。对于DataFrame调用`df.cumprod()`会逐步迭代每行，然后按照列进行累积的计算，而使用`df.cumprod(axis=1)`则按列迭代，计算行内的累积。

参考：

- [numpy.cumprod() in Python](https://www.geeksforgeeks.org/numpy-cumprod-in-python/)

## [pandas.DataFrame.groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)

函数`groupby`是对DataFrame进行分组，这个分组的操作通常仅仅是一系列操作中的排头阵。也就是说，我们在应用`groupby`这个函数不仅是“为了分组而分组”，而是“为了更重要的目的不得不先进行分组”。

比如，下面的例子展示的是求取每组分组的均值。在这个例子里面我们分组不是目的，而求取每个分组才是目的。

```
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
df
   Animal  Max Speed
0  Falcon      380.0
1  Falcon      370.0
2  Parrot       24.0
3  Parrot       26.0
df.groupby(['Animal']).mean()
        Max Speed
Animal
Falcon      375.0
Parrot       25.0
```

参考：

- [Group By: split-apply-combine](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)
