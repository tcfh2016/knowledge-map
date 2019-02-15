## [Intro to Python for Data Science course](https://www.datacamp.com/courses/intro-to-python-for-data-science)

### 1.Python Basics

- Python as a calculator

Python支持基本的运算操作，除了基本的加减乘除外，`**`代表指数运算，`%`为取余操作。

- Variable

四种常见的类型:int, float, str, bool。使用`type()`去打印对应变量的类型。

字符串类型(str)在拼接自定义提示信息的时候非常有用，只是你无法将其他类型与字符串使用`+`直
接拼接起来，这个时候需要进行类型转换：使用`str()`来将其他类型转换为字符串类型。类似的转
换函数包括`int()`, `float()`, `bool()`。

Python里面的字符串操作比较多样化，比如` ("Hey " * 2)`会将"Hey"重复两次。

### 2.Python Lists

list是一种可以将多个数值组合在一起的复合数据类型，这些数值可以是不同的数据类型。当然list
也可以内嵌包含。

- subsetting lists

list里面元素的索引从前往后从0开始，从后往前自-1开始：

```
[a, b, c, d, e, f, g]
 0  1  2  3  4  5  6
-7 -6 -5 -4 -3 -2 -1
```

- List slicing

list切片遵循前闭后开的原则：[start, end)，同时也支持省略：省略start默认从第一个元素开始，
省略end，默认最后一个元素+1。

修改元素直接通过索引进行重新赋值即可。

- 增删操作

列表的扩展可以通过"+"操作来完成，而删除操作需要使用`del()`。

*`;`用来在一行代码里面分割不同的代码指令。*

- 列表拷贝

直接通过“=”来拷贝列表那么拷贝变量和被拷贝变量都指向相同的对象，

```
# areas, areas_copy都指向相同的对象。
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = areas

# 通过list()进行复制拷贝，areas, areas_copy都指向各自不同的对象。
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas)

```

### 3.Functions and Packages

使用`?function_name`或者`help(function_name)`去获取对应函数的帮助信息。

- Multiple arguments Functions

```
sorted(iterable, key=None, reverse=False)
```

- Method :Functions that belong to objects.

In Python, everything is object, and object have methods associated, depending on
type.

- String Methods

```
place = "house"
place = place.upper()
place.count('o')
```

- List Methos

```
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas.index(20.0))
print(areas.count(9.50))
areas.append(24.5)
areas.reverse()
```

- Packages

Packages was used for code distribution, it replace of the directory of Python
scripts, and each script = module. Each module often contains specified functions
methods, types.

There are thousands of packages available such as Numpy, Matplotlib, Scikit-learn.

- Import Package

使用`import math`会将math里面所有的对象全部包含进来，另一种方式是采用选择性的import方式，
即`from math import pi`。

另一种复合型的导入方式是`from scipy.linalg import inv as my_inv`。

### 4.Numpy, a powerful package to do data science

Numeric Python, an alternative to Python List, it can do calculations over entire
arrays and easy, fast.

```
pip3 install numpy
```

- NumPy Side Effects

NumPy合适用于向量运算，相比常规的List，它有如下局限：一、Numpy里面的array是让集合中的元
素进行统一操作所以无法包括不同的数据类型；二、算术操作的含义与常规List不同，其操作符针对
两个集合的元素逐个进行处理：

```
python_list = [1,2,3]
# python_list + python_list = [1,2,3,1,2,3]

numpy_array = numpy.array([1,2,3])
# numpy_array + numpy_array = array([2,4,6])
```  

其列表索引与常规List相同。

- numpy array 逻辑操作

```
import numpy as np

# 计算BMI。
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# 创建bool的numpy 列表，对于bmi中的每个值，如果小于21则为True，否则为False。
light = bmi < 21

# 打印出对应bmi小于21的值。
print(bmi[light])
```

- 2D NumPy Arrays

对二维NumPy列表索引的时候可以使用省略符，同时可以更方便地使用`,`操作符来指定行列。

```
np_2d[0,2]
np_2d[0][2]

np_2d[:,1:3]
```

- Basic Statistics

|函数|功能|
|-|-|
|numpy.mean(x)|均值|
|numpy.median(x)|中值|
|numpy.std(x)|标准差|
|numpy.corrcoef(x)|方差|
