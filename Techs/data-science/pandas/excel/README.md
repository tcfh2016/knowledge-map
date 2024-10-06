# 用pandas读取excel

在excel里面能够做的工作基本在pandas里面也可以做。pandas相比excel的优势：

- excel能够处理100万行的数据，pandas能够处理上亿行的数据
- 一些内存密集型的计算可能会把excel搞崩溃，但是pandas处理得游刃有余
- pandas能够更好的将一些处理进行自动化
- excel只能够在Windows上使用，但是pandas处理的数据是跨平台的


参考：

- [A Python Pandas Introduction to Excel Users](https://towardsdatascience.com/a-python-pandas-introduction-to-excel-users-1696d65604f6)


## [pandas.read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas-read-excel)

`read_excel()`读取excel文件时，行索引会自动生成，默认以第0行作为列索引。

- 如果要指定原始数据中某列作为行索引，可以通过`index_col = value`来指定。
- 如果要指定原始数据中某行作为列索引，可以通过`header = value`来指定，`header = None`默认以数字作为列索引。

其他参数：

- `usecols`指定要导入的列。


注：office 2003及以前的`.xls`格式或者office 2007年及之后的`.xlsx`，并将读取的数据内容保存为DataFrame。


参考：

- [Tutorial Using Excel with Python and Pandas](https://www.dataquest.io/blog/excel-and-pandas/)



## `Missing optional dependency 'xlrd'`

在读取`.xlsx`的时候依赖`openpyxl`，需要提前安装。否则你会得到“ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.”这样的错误。

第一次使用`read_excel()`接口的时候，我读取了`.xls`文件，提示`Missing optional dependency 'xlrd'`的错误。

使用`pip install xlrd`安装了xlrd之后，可以正常读取。

但是当我尝试使用`read_excel()`来读取`.xlsx`的时候，又提示`ImportError: Missing optional dependency 'openpyxl'`的错误。

应该是因为`xlrd`仅支持旧的`.xls`文件，也就是xlrd在2020年之后不再支持`xlsx`，因此需要使用`openpyxl`。

参考：

- [Python: Pandas pd.read_excel giving ImportError: Install xlrd >= 0.9.0 for Excel support](https://stackoverflow.com/questions/48066517/python-pandas-pd-read-excel-giving-importerror-install-xlrd-0-9-0-for-excel)

## `ModuleNotFoundError: No module named 'xlwt'`

在使用`df.to_excel("test.xls")`的时候提示`No module named 'xlwt'`，这是因为在保存xls格式文件的时候需要`xlwt`模块，安装这个模块之后会提示：

> FutureWarning: As the xlwt package is no longer maintained, the xlwt engine will be removed in a future version of pandas. This is the only engine in pandas that supports writing in the xls format. Install openpyxl and write to an xlsx file instead. You can set the option io.excel.xls.writer to 'xlwt' to silence this warning. While this option is deprecated and will also raise a warning, it can be globally set and the warning suppressed.

# 导出Excel

使用`df.to_excel(file_name, sheet_name='name')`，将df到处到excel中的'name'sheet，默认为`Sheet1`

如果要到处到多个sheet，那么需要首先使用`pd.ExcelWriter`打开一个Excel文件再操作：

```
work = pd.ExcelWriter('out.excel')
df1.to_excel(work, sheet_name='df1')
df2.to_excel(work, sheet_name='df2')
```