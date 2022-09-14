## 用pandas读取excel

在excel里面能够做的工作基本在pandas里面也可以做。pandas相比excel的优势：

- excel能够处理100万行的数据，pandas能够处理上亿行的数据
- 一些内存密集型的计算可能会把excel搞崩溃，但是pandas处理得游刃有余
- pandas能够更好的将一些处理进行自动化
- excel只能够在Windows上使用，但是pandas处理的数据是跨平台的


参考：

- [A Python Pandas Introduction to Excel Users](https://towardsdatascience.com/a-python-pandas-introduction-to-excel-users-1696d65604f6)


## `Missing optional dependency 'xlrd'`

第一次使用`read_excel()`接口的时候，我读取了`.xls`文件，提示`Missing optional dependency 'xlrd'`的错误。

使用`pip install xlrd`安装了xlrd之后，可以正常读取。

但是当我尝试使用`read_excel()`来读取`.xlsx`的时候，又提示`ImportError: Missing optional dependency 'openpyxl'`的错误。

应该是因为`xlrd`仅支持旧的`.xls`文件，也就是xlrd在2020年之后不再支持`xlsx`，因此需要使用`openpyxl`。

参考：

- [Python: Pandas pd.read_excel giving ImportError: Install xlrd >= 0.9.0 for Excel support](https://stackoverflow.com/questions/48066517/python-pandas-pd-read-excel-giving-importerror-install-xlrd-0-9-0-for-excel)


