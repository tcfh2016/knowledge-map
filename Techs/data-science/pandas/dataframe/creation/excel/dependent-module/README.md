
## `Missing optional dependency 'xlrd'`

第一次使用`read_excel()`接口的时候，我读取了`.xls`文件，提示`Missing optional dependency 'xlrd'`的错误。

使用`pip install xlrd`安装了xlrd之后，可以正常读取。

但是当我尝试使用`read_excel()`来读取`.xlsx`的时候，又提示`ImportError: Missing optional dependency 'openpyxl'`的错误。

应该是因为`xlrd`仅支持旧的`.xls`文件，也就是xlrd在2020年之后不再支持`xlsx`，因此需要使用`openpyxl`。

参考：

- [Python: Pandas pd.read_excel giving ImportError: Install xlrd >= 0.9.0 for Excel support](https://stackoverflow.com/questions/48066517/python-pandas-pd-read-excel-giving-importerror-install-xlrd-0-9-0-for-excel)

## `ModuleNotFoundError: No module named 'xlwt'`

在使用`df.to_excel("test.xls")`的时候提示`No module named 'xlwt'`，这是因为在保存xls格式文件的时候需要`xlwt`模块，安装这个模块之后会提示：

> FutureWarning: As the xlwt package is no longer maintained, the xlwt engine will be removed in a future version of pandas. This is the only engine in pandas that supports writing in the xls format. Install openpyxl and write to an xlsx file instead. You can set the option io.excel.xls.writer to 'xlwt' to silence this warning. While this option is deprecated and will also raise a warning, it can be globally set and the warning suppressed.