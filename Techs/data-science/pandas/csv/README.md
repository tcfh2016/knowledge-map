# 什么是CSV

CSV全称为[Comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values)


# 读CSV

read_csv()函数的相关参数：

- `index_col`，指定要读取csv中的哪一列作为行标签
- `header`，指定要读取csv中的哪一行作为列标签
- `sep`，指定分隔符，默认以','去分割各个字段，其他通过`sep = "|"`指定
- `names`，指定各列名称
- `usecols`，可以传入“列名称列表”或者“列索引列表”来指定导入对应的列。
- `dtype`，导入时指定列的类型
- `dayfirst`
- `encoding='gbk'`，设置编码格式为'gbk'。


读取的时候pandas会默认将第一行识别为列名称，并且判断每列的类型。你可以通过`dtypes`来指定各列的类型，比如：

```
dtypes = {'col1': 'int32', 'col2': 'float32', 'col3': 'object'}
df = pd.read_csv('data.csv', dtype=dtypes)
```

- [How to read data using pandas read_csv](https://honingds.com/blog/pandas-read_csv/)
- [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [](https://docs.kanaries.net/articles/how-to-read-csv-files-pandas)


## `names`参数

这个参数是给读取的数据贴上列标签，也就是使用了这个参数，那么读取文件里面的每一行都是数据，不会默认采用第一行作为标题行。

如果读取一个空的csv会提示错误。


## 选择要读取的列（使用`usecols`参数）

需要注意的是在`usecols`指定的列标签并无法指定顺序，比如原始csv里面的列顺序是`a,b,c`，那么在读取的时候尽管使用`usecols=['b', 'c', 'a']`读取出来的数据列的顺序依然是`a,b,c`。


这在官方文档[usecolslist-like or callable, optional](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)里面已经进行过说明，但如果没有碰到过问题是很难留下印象的：

```
 Element order is ignored, so usecols=[0, 1] is the same as [1, 0]. To instantiate a DataFrame from data with element order preserved use pd.read_csv(data, usecols=['foo', 'bar'])[['foo', 'bar']] for columns in ['foo', 'bar'] order or pd.read_csv(data, usecols=['foo', 'bar'])[['bar', 'foo']] for ['bar', 'foo'] order.
```


## 不读取某列

如果我不想读取某列，可以使用lambda表达式来完成：

```
pd.read_csv("sample.csv", usecols=lambda x: x != "name")
```


## 不读取某行（使用`skiprows`参数）

`skiprows = 2`代表不读取开头的两行，`skiprows = [0, 1, 3]`表示不读取第0，1，3行。

```
df = pd.read_csv('data.csv', skiprows=2)
```


## 将读取的csv的index转换为`DateTimeIndex`

```
df = pd.read_csv('上证指数241101-250615.csv', index_col=0)
df.index = pd.to_datetime(df.index)
```


参考：

- [How to specify the `dtype` of index when read a csv file to `DataFrame`?](https://stackoverflow.com/questions/29792865/how-to-specify-the-dtype-of-index-when-read-a-csv-file-to-dataframe)


## `codec can't decode byte`

read_csv可以直接用来读取csv文件，且可以通过不同的参数来完成多样化的操作。第一次尝试读取时出现“UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8 in position 0: invalid continuation byte”的错误。

```
df = pd.read_csv('data.csv', encoding='utf-8')
df = pd.read_csv('data.csv', encoding='ISO-8859-1')
```

在StackOverflow上查找到答案，如上的错误提示是reas_csv默认以'utf-8'的编码方式去读取数据，发现原始文档的编码不匹配，于是指定`encoding="ISO-8859-1"`之后就能够成功读取了，但却发现在打印窗口上的中文不能正常显示，查找[Encodings and Unicode](https://docs.python.org/3/library/codecs.html#standard-encodings)之后修改`encoding="gb2312"`之后可以正常读取和显示。


参考：

- [UnicodeDecodeError when reading CSV file in Pandas with Python
](https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python)


## 远程读取认证

从网络链接读取csv的时候可能涉及到认证，这个时候可以使用`read_csv()`里面的`storage_options`参数，不过这个参数是后面`1.2`版本新增的，旧版本里就没有。

```
pd.read_csv('https://clutch-hz.dynamic.nsn-net.net/jenkins/view/Tools/job/Tools.dashboard.run_5g_gerrit/lastSuccessfulBuild/artifact/src/changes.csv',
            storage_options={'Authorization': b'Basic %s' % b64encode(bytes('{}:{}'.format(my_dict['key'], my_dict['value']), 'utf-8'))})
```

另一种方式是

```
```

不过这种方式可能会遇到“Unable to Get Local Issuer Certificate”的问题，可以通过传递`verify=False`参数来解决。

参考：

- [](https://stackoverflow.com/questions/33039327/handling-http-authentication-when-accesing-remote-urls-via-pandas)
- [Pandas: How to read an online CSV file that requires authentication](https://www.slingacademy.com/article/pandas-how-to-read-an-online-csv-file-that-requires-authentication/)
- [Python Requests Unable to Get Local Issuer Certificate](https://tech.sadaalomma.com/python/python-requests-unable-to-get-local-issuer-certificate/)


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

## read_table

read_table()与read_csv的区别在于后者默认读取以‘,’作为分隔符的文件，前者需要显示指定分隔符。


# 写CSV

## 处理csv

使用`index_col`来指定行标签：选择某列作为行标签，默认以从0开始递增的序号作为行标签，比如`df = pd.read_csv("f500.csv", index_col = 0)`就是从f500.csv里面读取数据并且将首列作为index使用。

使用`header`来指定列标签。

```
df.to_csv(path_or_buf=None, sep=',', columns=None, header=True, index=True)
```

## to_csv()时中文乱码问题

在写入中文时使用`utf-8`的编码方式依然会展示乱码，可以将其设置为`gb2312`来解决乱码问题：

```
month_groups.min().reset_index().to_csv("000898_month_min.csv", sep=',', encoding='gb2312')
```


## to_csv()时丢弃行标签和列标签

通过`header=True, index=True`两个参数来控制是否输出header和index。


## to_csv()时重排列标签

使用`columns`参数来指定顺序：

```
data.to_csv('out.csv', columns = ['x1', 'x2', 'x3', 'x4'])
```

# Q&A

## `ParserError: Error tokenizing data`

读取csv的时候碰到`ParserError: Error tokenizing data. C error: Expected 29 fields in line 2995, saw 57`，查了一下原因是其中有些异常行。

可以使用`on_bad_lines='warn'`打印出在哪一行，或者使用`skip`跳过异常行：

```
data = pd.read_csv('file1.csv', on_bad_lines='skip')
```

参考：

- [pandas.parser.CParserError: Error tokenizing data](https://stackoverflow.com/questions/18039057/pandas-parser-cparsererror-error-tokenizing-data)