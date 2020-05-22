# [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

DataFrame 是一个二维表式的数据结构，由data(数据)、rows(行)、columns(列)组成，数据基于
行列进行存储，因此它既有行索引也有列索引，可被看做是由Series组成的字典（共用同一个索引）。

![](dataframe.png)

## DataFrame所包含的数据类型

DataFrame每列的数据类型可以通过`print(df.dtypes)`显示出来。

- object: 字符串类型。


## DataFrame创建

1.传入等长的列表来创建

如果不指定行/列索引，默认索引为0...N-1(行/列的长度)。

```
import pandas as pd
students = ['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry']
df = pd.DataFrame(students)
```

2.传入等长的字典来创建

基于dictionary创建的时候默认以key做为列索引：

```
import pandas as pd
data = {'Name':['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry'],
        'Age':[18, 21, 29, 18, 23]}
df = pd.DataFrame(data)
```

*注：在聚宽上测试发现字典的值可以是Series，这样创建出来的DataFrame会自动以Series里面所
携带的index做为该DataFrame的index。*

3.指定行列名

指定列序列时按照指定顺序进行排列。

```
import pandas as pd
data = {'Name':['Lisha', 'Shelly', 'Greay', 'Leo', 'Marry'],
        'Age':[18, 21, 29, 18, 23]}
df = pd.DataFrame(data, columns=['Age', 'Name'],
                  index=['one', 'two', 'three', 'four', 'five'])
```

- 直接以SQL数据库、CSV、Excel文件做为数据源来创建它们

## DataFrame 获取

需要注意DataFrame的获取是以列优先的，比如dataframe[x]是获取列名为x的对应的Series，这种
理解方式与C/C++二维数组是不同的。

### 列的遍历

```
```

### 获取某行某列的值

*注：DataFrame的单一行或者列均是Series类型，只不过index不同：DataFrame行的index为DataFrame
的columns名称，DataFrame列的index为DataFrame的index*

- Dataframe.[ ] ; This function also known as indexing operator
- Dataframe.loc[ ] : This function is used for labels.
- Dataframe.iloc[ ] : This function is used for positions or integer based
- Dataframe.ix[] : This function is used for both label and integer based

获取某行某列的值仅仅是获取多行多列的值的简化形式。如上最后一种方法已经过时。

```
data["Age"] # 选择列名为Age的一列
data[["Age", "College", "Salary"]] # 选择列名为Age, College, Salary的三列

data.loc["R.J. Hunter"] # 选择行名为R.J. Hunter的一行
data.loc[["Avery Bradley", "R.J. Hunter"]] # 选择行名为Avery Bradley, R.J. Hunter的三行
data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Number", "Position"]] # 选择两行三列

data.iloc[3] # 选择一行
data.iloc [[3, 5, 7]] # 选择三行
data.iloc [[3, 4], [1, 2]] # 选择两行两列
```

参考：

- [Indexing and Selecting Data with Pandas](https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/)

### columns / index 获取

通过`df.columns`选中所有列名。通过`df.index`选中所有行名。

### 列的获取

通过类似字典标记或属性的方式，可以将 DataFrame的列获取为一个 Series。多列的选取需要指
定多个列的名称，切片默认用来选取多行，因此想要在多列选取的时候使用切片必须采用`混合索引/
同时选择行和列`的方式，即`obj.ix[val1,val2]`，在val2里使用切片。

```
df.Age  # 这种方式很简洁，但是如果某个行名由多个单词组成，比如‘start time’就无法工作了。
df['Age'] # 选取单列
df[['Age','Name']] # 注意多列
```

一次性指定多个列的名称可以同时选中两列，比如如上例子里面`df['Name', 'Age']`。

### 行的获取

行的选取有三种方式：`loc`方法、切片和布尔索引（Boolean indexing）。

**1.使用`loc`方法**

使用`loc`方法通常用来进行单行索引，在选择多行时语法上与列有些类似。

```
df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])

print(df.loc['b'])        # 通过索引访问元素，之前是df.ix['b']，已不推荐使用旧的方法。
print(df.loc[['a', 'b']]) # 索引'a', 'b'两行。
```

**2.使用切片**

切片支持行名称和行序号来确定范围（*DataFrame仅能用行进行切片*）：

```
print(df['a':'c'])        # 索引'a', 'b', 'c'三行。
print(df[0:1])            # 索引'a'一行数据。
```

**3.使用布尔索引**

根据列的条件来进行选择，这种方式是pandas所独有的方式。

```
df[df.A > 0]    # 以某列的数据做为标准选择数据
df[df['A'] > 0] # 以某列的数据做为标准选择数据
df[df > 0]      # 选择 df中大于0的数，其余置为 NaN
```

简单地说，pandas支持df[SeriesOfBollean]来选取行，而实际上SeriesOfBollean的创建可以通
过简单的df.column > contion来完成。

```
conditions = []
for f in df.floats:
    if f > 3.0:
        conditions.append(True)
    else:
        conditions.append(False)
print(df[conditions])
match_condition = pd.Series(conditions, index=df.index)
print(df[match_condition])
```

如上的代码与下面这段等价：

```
print("按条件选择行例3：")
condition = df.floats > 3.0  # 创建一个bollean 的Series。
print(df[condition])
```

对于`datetime.date`类型如何通过布尔索引来进行呢？创建`compare_date = datetime.date(2012, 1, 1)`
在进行比较，否则提示：

```
not supported between instances of 'datetime.date' and 'str'
```

参考：

- [How do I filter rows of a pandas DataFrame by column value?](https://www.youtube.com/watch?v=2AFGPdNn4FM)


### 多行多列

```
df.loc[:, ['A', 'B']]
```

## DataFrame 查询

### 判断DataFrame是否为空

```
if df.empty:
    print('DataFrame is empty!')

len(df.index) == 0    
```

参考：

- [How to check whether a pandas DataFrame is empty?](https://stackoverflow.com/questions/19828822/how-to-check-whether-a-pandas-dataframe-is-empty)

### 根据某列的值查询对应的index

因为index是行索引，引起可以借助条件选择的功能选择特定的行，然后再获取结果的index属性：

```
stocks_df[stocks_df['display_name'] == '洋河股份'].index
结果为：Index(['002304.XSHE'], dtype='object')

stocks_df[stocks_df['display_name'] == '洋河股份'].index.item()
结果为：002304.XSHE
```

参考：

- [Python Pandas: Get index of rows which column matches certain value](https://stackoverflow.com/questions/21800169/python-pandas-get-index-of-rows-which-column-matches-certain-value)
- [Get index of a row of a pandas dataframe as an integer](https://stackoverflow.com/questions/41217310/get-index-of-a-row-of-a-pandas-dataframe-as-an-integer/41217335)

## DataFrame 修改

### 修改行、列名

1.修改行名

直接赋值，如下将DataFrame的index修改为其中的某一列：

```
min_max_df.index = min_max_df['日期'] # 之前的'日期'列依然存在
min_max_df = min_max_df.set_index('日期', drop=True) #

# 这种方式复写之前的index后，索引的名字也不见了。
# 使用 df.index.name = xx 来写入。
df.index = [1, 2, 3, 4]
```


*注1：DataFrame的set_index函数会将一个或多个列转换为行索引，并创建新的DataFrame。*
*注2：Index 对象是不可修改的。因此df.index[1] = 'c'会提示错误。*

参考：

- [Remove index name in pandas](https://stackoverflow.com/questions/29765548/remove-index-name-in-pandas)

2.修改列名

两种方式：直接赋值和调用 rename方法：

```
df.columns = ['price'] # 用等长的列表来覆盖之前的列名
df.rename(columns=lambda x:x.replace('$',''), inplace=True)
df.rename(columns={'a':'b'}, inplace=True) # 将'a'重命名为'b'，可以支持多列的重命名。
```

另外在read_csv()的时候可以修改读取数据的列名：

```
ufo = pd.read_csv(name_file, names=ufo_cols, header=0) # 不指定header，直接使用自
定义ufo_cols作为列名。
```

### 增/删行、列

1.增加行

在某个DataFrame里面添加一列必须使用`[]`操作符，`此时应保证Series和DataFrame具有相同的index`

```
df['numbers'] = series
```

2.删除行

调用`drop()`:

```
df.frop([0,1], axis=0, inplace=True) # 删除index为0，1的行。
```

3.删除列

两种方法：调用`drop()`和使用`del`。

`drop()`函数可以用来删除行和列。

```
df.drop('column name', axis=1) # 指定axis=1说明删除列。
df.drop(['city', 'state'], axis=1) # 删除'city'和'state'两列。
```

删除列时必须通过索引的方式指定，不能通过属性的方式来指定。

```
del df['newdata']
del df.newdata # 会提示错误。
```

### 修改行、列

1.修改整列

直接通过赋值的方式修改（添加）：

```
df['numbers'] = 1.0
df.numbers = 1.0
```

将列表或数组赋值给某列时，其长度必须跟DataFrame的长度匹配：

```
val = Series([-1, -2, -3, -4], index=['b', 'a', 'c', 'd'])
df['newdata'] = val
df.newdata = val
```

## Dataframe统计

**1.如何统计DataFrame某列的和？**

`dataframe.sum()`默认对“行”进行求和，即以列为单位求每列对应所有行的和，可以指定坐标轴，
比如`dataframe.sum(axis=1)`对“列”进行求和，按行为单位求对应所有列的和。

对单一列进行求和可以使用`dataframe['column'].sum()`。

**2.如何统计DataFrame某列相同值的个数？**

```
df["category"].value_counts()

df = pd.DataFrame({'a':list('abssbab')})
df.groupby('a').count()

输出：
b    3
a    2
s    2


print (df['col'] == 1).sum()
```

参考：

- [count the frequency that a value occurs in a dataframe column](https://stackoverflow.com/questions/22391433/count-the-frequency-that-a-value-occurs-in-a-dataframe-column)

## DataFrame 输出格式

```
.dataframe tbody tr th:only-of-type { vertical-align: middle; }
.dataframe tbody tr th { vertical-align: top; }
.dataframe thead th { text-align: right; }
```
