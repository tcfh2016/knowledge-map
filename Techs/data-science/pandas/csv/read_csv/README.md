
## pandas.read_csv 简单用法

```
pd.read_csv('data.csv')  
```

- [How to read data using pandas read_csv](https://honingds.com/blog/pandas-read_csv/)
- [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)


## `names`参数

这个参数是给读取的数据贴上列标签，也就是使用了这个参数，那么读取文件里面的每一行都是数据，不会默认采用第一行作为标题行。

如果读取一个空的csv会提示错误。


## `usecols`参数

需要注意的是在`usecols`指定的列标签并无法指定顺序，比如原始csv里面的列顺序是`a,b,c`，那么在读取的时候尽管使用`usecols=['b', 'c', 'a']`读取出来的数据列的顺序依然是`a,b,c`。


这在官方文档[usecolslist-like or callable, optional](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)里面已经进行过说明，但如果没有碰到过问题是很难留下印象的：

```
 Element order is ignored, so usecols=[0, 1] is the same as [1, 0]. To instantiate a DataFrame from data with element order preserved use pd.read_csv(data, usecols=['foo', 'bar'])[['foo', 'bar']] for columns in ['foo', 'bar'] order or pd.read_csv(data, usecols=['foo', 'bar'])[['bar', 'foo']] for ['bar', 'foo'] order.
```

如果我不想读取某列，可以使用：

```
pd.read_csv("sample.csv", usecols=lambda x: x != "name")
```

## `codec can't decode byte`

read_csv可以直接用来读取csv文件，且可以通过不同的参数来完成多样化的操作。第一次尝试读取时出现“UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8 in position 0: invalid continuation byte”的错误。

在StackOverflow上查找到答案，如上的错误提示是reas_csv默认以'utf-8'的编码方式去读取数据，发现原始文档的编码不匹配，于是指定`encoding="ISO-8859-1"`之后就能够成功读取了，但却发现在打印窗口上的中文不能正常显示，查找[Encodings and Unicode]()之后修改`encoding="gb2312"`之后可以正常读取和显示。


参考：

- [UnicodeDecodeError when reading CSV file in Pandas with Python
](https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python)
- [Encodings and Unicode](https://docs.python.org/3/library/codecs.html#standard-encodings)

## 不读取某列

