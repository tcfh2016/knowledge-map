
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


