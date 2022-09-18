
## 处理csv

使用`index_col`来指定行标签：选择某列作为行标签，默认以从0开始递增的序号作为行标签，比如`df = pd.read_csv("f500.csv", index_col = 0)`就是从f500.csv里面读取数据并且将首列作为index使用。

使用`header`来指定列标签。

```
import pandas as pd
```


## read_table

read_table()与read_csv的区别在于后者默认读取以‘,’作为分隔符的文件，前者需要显示指定分隔符。


## 将 DataFrame / DataFrameGroupBy 对象写入csv

DataFrame 对象可以直接调用`to_csv()`函数:

```
df.to_csv(file_name, sep='\t', encoding='utf-8')
```

DataFrameGroupBy 对象没有`to_csv()`函数，常见的使用是调用min()/sum()等接口返回 group里面的某个值，如此组成新的 DataFrame 对象。

在写入中文时使用`utf-8`的编码方式依然会展示乱码，可以将其设置为`gb2312`来解决乱码问题：

```
month_groups.min().reset_index().to_csv("000898_month_min.csv", sep=',', encoding='gb2312')
```


参考：

- [Pandas groupby to to_csv](https://stackoverflow.com/questions/47602097/pandas-groupby-to-to-csv?rq=1)


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

## pandas.read_csv 分行统计

按照每个月份、年份进行统计。

```
df = pd.read_csv("000898.csv", encoding="gb2312", dayfirst=True, usecols = ["日期", "总市值"])
df["日期"] = pd.to_datetime(df["日期"])
df["年"] = df["日期"].dt.year
df["月"] = df["日期"].dt.month

groups = df.groupby(["年", "月"])
```

- [python pandas extract year from datetime](https://stackoverflow.com/questions/30405413/python-pandas-extract-year-from-datetime-dfyear-dfdate-year-is-not)
- [Python: Datetime to season](https://stackoverflow.com/questions/44124436/python-datetime-to-season)


## pandas.read_csv

read_csv可以直接用来读取csv文件，且可以通过不同的参数来完成多样化的操作。第一次尝试读取时出现“UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8 in position 0: invalid continuation byte”的错误。

在StackOverflow上查找到答案，如上的错误提示是reas_csv默认以'utf-8'的编码方式去读取数据，发现原始文档的编码不匹配，于是指定`encoding="ISO-8859-1"`之后就能够成功读取了，但却发现在打印窗口上的中文不能正常显示，查找[Encodings and Unicode]()之后修改`encoding="gb2312"`之后可以正常读取和显示。

参数详解：

1. sep

分隔符：默认以','去分割各个字段，如果原始文件不是以逗号做为分隔符，那么需要另外指定。

```
import pandas as pd
df2 = pd.read_csv("dataset.txt", sep = "|")
```

2. header

标题：默认以第一行（header = 0）作为标题，不需要标题则设置 header=None。

```
import pandas as pd
df = pd.read_csv("f500.csv", header = 0)
```

3. names

列名：指定各列名称。

```
import pandas as pd
df = pd.read_csv("f500.csv", names = ["column0", "column1", "column2",    "column3", "column4", "column5", "column6", "column7", "column8", "column9", "column10", "column11", "column12", "column13"])
```



5. usecols

导入指定列：可以传入“列名称列表”或者“列索引列表”来指定导入对应的列。

```
import pandas as pd
df = pd.read_csv("f500.csv", usecols = ["company", "rank", "revenues"])
df = pd.read_csv("f500.csv", usecols = [0,1,2])
```

你可以使用lambeda表达式进行反向选取。

```
df = pd.read_csv("f500.csv", usecols = lambda column : column not in
["company" , "rank", "revenues"])
```

6. dtype

指定列的类型。

```
df = pd.read_csv("f500.csv", dtype = {"revenues" : "float64"})
```

7. dayfirst

对于列的日期 04/10/2019 统一转换为 2019-10-04，避免混淆04是月份。

```
pd.read_csv('./data/es50.txt', index_col=0, parse_dates=True, sep=';', dayfirst=True)
```


参考：

- [How to read data using pandas read_csv](https://honingds.com/blog/pandas-read_csv/)
- [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [UnicodeDecodeError when reading CSV file in Pandas with Python
](https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python)
- [Encodings and Unicode](https://docs.python.org/3/library/codecs.html#standard-encodings)
