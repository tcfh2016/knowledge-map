## DataFrame

Pandas里面的数据对象，不仅有用来处理一维数据的`Series`，还有可以用来处理多维数据的`DataFrame`。类比一下，`Series`犹如表格中的一列，`DataFrame`就犹如整个表格。

## 创建

创建一个DataFrame最简单的方式就是通过字典数据来创建，前面创建Series的时候也能够通过字典数据，它们之间的区别在于创建DataFrame的时候字典的值需要是一个列表，而创建Series的时候字典的值是单个数据。

```
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

输出：
calories  duration
0       420        50
1       380        40
2       390        45
```

## 命名索引

前面讲Series的时候提到创建Series的时候默认以数值索引来作为元素索引的标签，但同时也可以自定义标签来索引元素。

DataFrame也是类似，在创建DataFrame的时候默认以数值索引来作为索引行的标签，但同时也可以自定义标签来索引行。同样地，也是通过`index`参数。

```
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

输出：
      calories  duration
day1       420        50
day2       380        40
day3       390        45
```

*注意：Series如果有了自定义的标签来作为索引依然能够使用数值索引，但是dataframe就不行。*


## 获取数据

DataFrame数据类似一个表格。所以在获取数据的时候会有多种不同的方式。如果获取的数据是单行或者单列，那么都是Series类型。

获取行的时候可以通过数值索引，也可以通过行标签。

```
# df的index是默认的数值索引，那么可以使用loc[0]，否则不能使用。
print(df.loc[0])


输出：
calories    420
duration     50
Name: 0, dtype: int64

# 通过给定行索引列表来获取多个行
print(df.loc[[0, 1]])

输出：
calories  duration
0       420        50
1       380        40
```

如果要打印整个DataFrame的数据，需要使用`to_string()`函数。
