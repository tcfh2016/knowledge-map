## 什么是CSV

CSV全称为[Comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values)


## 读取csv 调用`to_numeric()`出现`ValueError: Unable to parse string " " at position 0`错误

读取lrb000898.csv, zcfzb000898.csv进行数据清洗、转换没有问题，但读取xjllb000898.csv的时候出现错误:

```
File "C:\Users\lianbche\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\tools\numeric.py", line 135, in to_numeric
  coerce_numeric=coerce_numeric)
File "pandas\_libs\lib.pyx", line 1925, in pandas._libs.lib.maybe_convert_numeric
ValueError: Unable to parse string " " at position 0
```

调试发现多转换了一列，查看原始文件发现在xjllb000898.csv每行末多了一个空行，因此问题出在转换空行时的错误。

参考：

- [pandas.to_numeric - find out which string it was unable to parse](https://stackoverflow.com/questions/40790031/pandas-to-numeric-find-out-which-string-it-was-unable-to-parse)

## 处理csv

使用`index_col`来指定行标签：选择某列作为行标签，默认以从0开始递增的序号作为行标签，比如`df = pd.read_csv("f500.csv", index_col = 0)`就是从f500.csv里面读取数据并且将首列作为index使用。

使用`header`来指定列标签。

```
import pandas as pd
```


## read_table

read_table()与read_csv的区别在于后者默认读取以‘,’作为分隔符的文件，前者需要显示指定分隔符。




## pandas.read_csv 删除行或列

从DataFrame删除行时需要使用drop函数，删除对应行需要指定index并且axis设定为“0”，删除列时需要指定列名且axis设定为“1”。

```
data = data.drop([0,1,2], axis=0)

data = data.drop("Area", axis=1)
data = data.drop(columns="area") # 这种方式不需要指定 axis参数。
```

如果需要删除满足某些条件的行，分两步走：

- Step 1 过滤出对应的行: df_age_negative = df[ df['Age'] < 0 ]
- Step 2 调用drop进行删除: df = df.drop(df_age_negative.index, axis=0)

参考：

[How to drop a list of rows from Pandas dataframe?](https://stackoverflow.com/questions/14661701/how-to-drop-a-list-of-rows-from-pandas-dataframe)
[The Pandas DataFrame – loading, editing, and viewing data in Python](https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/)


## pandas.read_csv

read_csv可以直接用来读取csv文件，且可以通过不同的参数来完成多样化的操作。第一次尝试读取时出现“UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8 in position 0: invalid continuation byte”的错误。

在StackOverflow上查找到答案，如上的错误提示是reas_csv默认以'utf-8'的编码方式去读取数据，发现原始文档的编码不匹配，于是指定`encoding="ISO-8859-1"`之后就能够成功读取了，但却发现在打印窗口上的中文不能正常显示，查找[Encodings and Unicode]()之后修改`encoding="gb2312"`之后可以正常读取和显示。


- [How to read data using pandas read_csv](https://honingds.com/blog/pandas-read_csv/)
- [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [UnicodeDecodeError when reading CSV file in Pandas with Python
](https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python)
- [Encodings and Unicode](https://docs.python.org/3/library/codecs.html#standard-encodings)


## to_csv()时中文乱码问题

在写入中文时使用`utf-8`的编码方式依然会展示乱码，可以将其设置为`gb2312`来解决乱码问题：

```
month_groups.min().reset_index().to_csv("000898_month_min.csv", sep=',', encoding='gb2312')
```