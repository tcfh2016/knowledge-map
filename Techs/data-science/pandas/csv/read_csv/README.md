
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


## `codec can't decode byte`

read_csv可以直接用来读取csv文件，且可以通过不同的参数来完成多样化的操作。第一次尝试读取时出现“UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8 in position 0: invalid continuation byte”的错误。

在StackOverflow上查找到答案，如上的错误提示是reas_csv默认以'utf-8'的编码方式去读取数据，发现原始文档的编码不匹配，于是指定`encoding="ISO-8859-1"`之后就能够成功读取了，但却发现在打印窗口上的中文不能正常显示，查找[Encodings and Unicode]()之后修改`encoding="gb2312"`之后可以正常读取和显示。


参考：

- [UnicodeDecodeError when reading CSV file in Pandas with Python
](https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python)
- [Encodings and Unicode](https://docs.python.org/3/library/codecs.html#standard-encodings)