## 字典创建

使用字典创建时默认以key做为列索引，但有个要求，值不能是标量值（），比如下面这样会出错：

```
pd.DataFrame(
    {
        'cbxxx_1UE':24492,
        'cbxxx_2UE':24492
    }
)
```

这是因为字典的值作为列时需要根据它来生成DataFrame的index，如果你传入的是整数，那么无法生成index，所以报错。修改为下面这样就没有问题：

```
pd.DataFrame(
    {
        'cbxxx_1UE':[24492],
        'cbxxx_2UE':24492
    }
)

pd.DataFrame(
    {
        'cbxxx_1UE':24492,
        'cbxxx_2UE':24492
    },
    index = [0]
)
```


## 将key作为index

如果我要将字典的键作为index, 值作为column呢？那么传入`items()`这样就将key和value作为DataFrame的列，然后重设index就可以了。

```
df=pd.DataFrame(dict.items(), columns=['Case', 'First Fail Build'])
df.set_index('Case', inplace=True)
```

## ValueError: If using all scalar values, you must pass an index

*注：在聚宽上测试发现字典的值可以是Series，这样创建出来的DataFrame会自动以Series里面所携带的index做为该DataFrame的index。*

在使用字典来创建dataframe的时候有一个隐藏条件，也既是它默认字典的key-value为dataframe的列，也即是key为dataframe的column名，这个时候字典的value需要是“非标量值”。否则会出现"ValueError: If using all scalar values, you must pass an index"这样的错误。

这个问题在[Constructing pandas DataFrame from values in variables gives “ValueError: If using all scalar values, you must pass an index”](https://stackoverflow.com/questions/17839973/constructing-pandas-dataframe-from-values-in-variables-gives-valueerror-if-usi)里面有讨论，而解决方法是可以先创建Series，再转换为dataframe。

```
data = {'a': 1, 'b': 2}
pd.Series(data).to_frame()
```

