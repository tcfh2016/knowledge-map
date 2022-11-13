## 查看重复行

通过`df.duplicated(keep='first')`来对重复数据进行检测，返回的结果是一个bool类型的Series对象，其中的keep参数是用来判定第一次重复数据的标记，可以接受`first`, `last`和`False`选项，False会将所有的重复数据返回True。

当然，还可以真对特定列进行重复数据的检查，比如`df.duplicated(subset='a', keep='first')`就是只针对'a'列进行。

得到了bool类型的Series后，我们可以通过`df[df.duplicated](keep=False)]`直接引用重复的行。


## 处理重复行

函数`drop_duplicates()`用来移除重复行，原型如下：

```
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
```

支持三个参数：subset某列或者列名的列表，表示参考那些列来对比重复；keep表示处理重复记录时保存哪一条；inplace表示将修改应用到原来的dataframe里。

参考：

- [pandas.DataFrame.drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)
- [Python | Pandas dataframe.drop_duplicates()](https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/)
