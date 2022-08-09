## 创建DataFrame

### 1.传入等长的列表来创建

如果不指定行/列索引，默认索引为0...N-1(行/列的长度)。

```
import pandas as pd
students = ['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry']
df = pd.DataFrame(students)
```

### 2.传入等长的字典来创建

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


### 3.直接以SQL数据库、CSV、Excel文件做为数据源来创建它们


### 4.能否从多个Series拼接为新的DataFrame ？



## 指定行列名

指定列序列时按照指定顺序进行排列。

```
import pandas as pd
data = {'Name':['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry'],
        'Age':[18, 21, 29, 18, 23]}
df = pd.DataFrame(data, columns=['Age', 'Name'],
                  index=['one', 'two', 'three', 'four', 'five'])
```
