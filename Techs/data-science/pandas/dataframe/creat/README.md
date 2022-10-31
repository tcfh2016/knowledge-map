## 创建DataFrame

1）传入等长的列表来创建

如果不指定行/列索引，默认索引为0...N-1(行/列的长度)。

```
import pandas as pd
students = ['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry']
df = pd.DataFrame(students)
```

创建时可以指定行列名，指定列序列时会按照指定顺序进行排列。

```
import pandas as pd
data = {'Name':['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry'],
        'Age':[18, 21, 29, 18, 23]}
df = pd.DataFrame(data, columns=['Age', 'Name'],
                  index=['one', 'two', 'three', 'four', 'five'])
```

2）传入等长的字典来创建

基于dictionary创建的时候默认以key做为列索引：

```
import pandas as pd
data = {'Name':['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry'],
        'Age':[18, 21, 29, 18, 23]}
df = pd.DataFrame(data)
```

*注：在聚宽上测试发现字典的值可以是Series，这样创建出来的DataFrame会自动以Series里面所携带的index做为该DataFrame的index。*

在使用字典来创建dataframe的时候有一个隐藏条件，也既是它默认字典的key-value为dataframe的列，也即是key为dataframe的column名，这个时候字典的value里面的元素个数要>1。否则会出现"ValueError: If using all scalar values, you must pass an index"这样的错误。

这个问题在[Constructing pandas DataFrame from values in variables gives “ValueError: If using all scalar values, you must pass an index”](https://stackoverflow.com/questions/17839973/constructing-pandas-dataframe-from-values-in-variables-gives-valueerror-if-usi)里面有讨论，而解决方法是可以先创建Series，再转换为dataframe。

```
data = {'a': 1, 'b': 2}
pd.Series(data).to_frame()
```

如果我要将字典的键作为index, 值作为column呢？

```
df=pd.DataFrame(dict.items(), columns=['Case', 'First Fail Build'])
df.set_index('Case', inplace=True)
```

3）嵌套列表创建

这里的嵌套列表指的是两层列表，因为它刚好是一个二维数组的结构。所以在创建时，每个外层列表元素都作为单独的一行：

```
l = [['a', 'b', 'c', 'd'],
     [1, 2, 3, 4],
     ['i', 'j', 'k', 'l']]
df = pd.DataFrame(l)

# 输出
   0  1  2  3
0  a  b  c  d
1  1  2  3  4
2  i  j  k  l
```

上面会默认添加index和columns，如果想指定行名或者列名，直接通过`pd.DataFrame(l, index=['i1', 'i2', 'i3'], columns=['c1', 'c2', 'c3', 'c4'])`指定即可。

参考：

- [Nested List to Pandas Dataframe with headers](https://stackoverflow.com/questions/32857544/nested-list-to-pandas-dataframe-with-headers)


## 从空的DataFrame开始


