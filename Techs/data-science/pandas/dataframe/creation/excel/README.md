## 用pandas读取excel

在excel里面能够做的工作基本在pandas里面也可以做。pandas相比excel的优势：

- excel能够处理100万行的数据，pandas能够处理上亿行的数据
- 一些内存密集型的计算可能会把excel搞崩溃，但是pandas处理得游刃有余
- pandas能够更好的将一些处理进行自动化
- excel只能够在Windows上使用，但是pandas处理的数据是跨平台的


参考：

- [A Python Pandas Introduction to Excel Users](https://towardsdatascience.com/a-python-pandas-introduction-to-excel-users-1696d65604f6)

## [pandas.read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas-read-excel)

`read_excel()`读取excel文件（office 2003及以前的`.xls`格式或者office 2007年及之后的`.xlsx`），并将读取的数据内容保存为DataFrame。

在读取`.xlsx`的时候依赖`openpyxl`，需要提前安装。否则你会得到“ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.”这样的错误。

使用`pd.read_excel("fund_data.xlsx")`读取excel文件，默认读取的是第一个sheet，你可以通过`sheet_name`参数来指定要读取哪一个sheet，可以通过sheet名称或者索引值：

```
# 通过sheet索引来指定
pd.read_excel("fund_data.xlsx", sheet_name=1)

# 通过sheet名称来指定
pd.read_excel("fund_data.xlsx", sheet_name="股票基金")

# 指定多个sheet，返回的是一个包含多个结果的字典
pd.read_excel("fund_data.xlsx", sheet_name=[0, "股票基金"])

# 获取所有sheet
pd.read_excel("fund_data.xlsx", sheet_name=None)
```

参考：

- [Tutorial Using Excel with Python and Pandas](https://www.dataquest.io/blog/excel-and-pandas/)