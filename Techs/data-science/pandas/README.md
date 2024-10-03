## [pandas](https://pandas.pydata.org/docs/)

`Pandas`基于 `NumPy` 创建，并纳入了大量库及一些标准的数据模型，提供了大量能使我们快速便捷地处理数据的函数与方法。`Pandas`的两个主要数据结构为`Series`和`DataFrame`，它们为大多数应用提供了一种可靠的、易于使用的基础。

- [series](./series/README.md)
- [dataframe](./dataframe/README.md)
- [csv处理](./csv/README.md)
- [空值处理](./mmissing-data/README.md)
- [绘图](./plot/README.md)


## `.options.display.`显示设置

在打印出DataFrame时最大的显示行由`pd.options.display.max_rows`和`pd.options.display.min_rows`来控制的，前者默认为60，后者默认为10。它们之间的规则是：

- 如果max_rows足以显示整个df的行数，那么显示所有的行。
- 如果max_rows不足以显示整个df的行数，那么显示min_rows行。

你可以调整这两个参数：

```
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
```

还有其他参数：

```
pd.set_option('display.width', 1000)

# 解决列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
```

参考：

- [Options and settings](https://pandas.pydata.org/docs/user_guide/options.html)


## 参考

- [10 Minutes to pandas](http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
- [Data School](https://www.youtube.com/channel/UCnVzApLJE2ljPZSeQylSEyg)




