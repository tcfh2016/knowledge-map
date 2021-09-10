# 简介

Python里面所有能够从左至右扫描对象的迭代工具（包括for循环、列表解析、in成员关系测试以接map内置函数等），都可以用于Python中任何序列类型，包括列表、元组以及字符串，甚至任何可迭代的对象。

“可迭代的对象”是序列观念的通用化，比如实际保存的序列，或者可以在迭代工具环境中一次产生一个结果的对象，都是可迭代的。

Python里面规定了迭代器协议，即“有__next__方法的对象会前进到下一个结果，在一系列结果的末尾时，会引发StopIteration。”在Python中任何支持迭代器协议的对象都是可迭代的，也都可以用for循环或者其他迭代工具遍历。因为所有迭代器工具内部远离都是在每次迭代中调用__next__，并捕捉StopInteration异常来确定何时离开。

# 常用迭代器

## 文件迭代器

逐行读取文本文件最好的方式是根本不要去读取，而是用for循环逐次调用next遍历每一行：

```
for line in open('script.py'):
  print(line.upper(), end='')
```

这种文件读取方式最简单，运行最快(迭代器在Python是以C语言的速度运行的)，且内存使用情况也是最好的。另一种方法是用for循环调用文件的readlines方法，这种方式将文件加载到内存再做成行字符串的列表：

```
for line in open('script.py').readlines():
  print(line.upper(), end='')  
```

这样将文件内容加载到内存的做法可能因为文件太大而无法工作。还有另外一种替代方案：

```
f = open('script')
while True:
  line = f.readline()
  if not line: break
    print(line.upper(), end='')
```

## 手动迭代

*注： next属性存在于Python2.x中，在Python3.x中使用__next__()，否则会报“list_iterator' object has no attribute 'next'”错误。*

Python提供了内置函数`next`来自动调用一个对象的`__next__`方法。给定一个可迭代对象X，调用next(X)等同于X.__next__()：

```
f = open('stript.py')
f.__next__
f.__next__

f = open('stript.py')
next(f)
next(f)
```

使用for循环时，会用内置函数`iter()`来从迭代对象中获取一个迭代器，这一步对于文件对象来说不是必需的，因为文件对象就是自己的迭代器：

```
L = [1, 2, 3]
I = iter(L)
I.next() # Python 2.x使用，Python 3.x使用 __next__()
I.next()

f = open('script.py')
f.next() # Python 2.x使用，Python 3.x使用 __next__()
f.__next__()
next(f)
```

## 其他内置类型迭代器

除了文件以及像列表这样的实际序列，其他类型也有迭代器，比如遍历字典的经典方法是获取其键的列表：

```
d = {'a':1, 'b':3, 'c':2}
for key in d.keys():
    print(key, d[key])
```

但实际上Python也给字典添加了迭代器，比如:

```
d2 = {'a':1, 'b':3, 'c':2}
i = iter(d2)
print(next(i))
```

所以在实际使用中我们不再需要调用keys()来遍历字典键，for循环会自动使用迭代协议来遍历它：

```
d3 = {'e':1, 'f':3, 'g':2}
for key in d3:
    print(key, d3[key])
```

# 列表解析：初探

列表解析是最常应用迭代器协议的环境之一。列表解析写在一个方括号中，因为它们最终会构建一个新的列表。它的格式包括两部分：“包含循环变量的表达式” + “一个可迭代的对象”，比如`L = [x + 10 for x in L]`。Python在执行该表达式时，会在解释器内部执行一个遍历L的迭代，然后按照顺序赋给每个元素，再收集对各个元素运行左边表达式的结果。

列表解析编写起来更加精简，同时比手动的for循环语句运行更快（往往快一倍），因为迭代在解释器内部是以C语言的速度执行的，而不是以手动Python代码执行的，特别对于较大的数据集合而言更是如此。

当我们考虑在一个序列中的每项上执行一个操作时，都可以考虑使用列表解析。列表解析有一些特别的扩展，比如表达式中嵌套的for循环可以有相关的if子句来过滤那些不为真的结果：`lines = [line.rstrip() for line in open('script.py') if line[0] == 'p']`。

列表解析还可以变得更复杂，它们的完整语法允许任意数目的for子句，每个子句有一个可选的相关的子句，比如`[x + y for x in 'abc' for y in 'lmn']`。

# 其他迭代环境

用户定义的类也可以实现迭代协议，只要实现了迭代协议的任何工具，都能够提供该工具的任何内置类型或用户定义的类上自动地工作。

Python包含了多种处理迭代的内置函数：

- map：它把一个函数调用应用于传入的可迭代对象中的每一项，并返回一个可迭代对象（Python3.x）。
- sorted：排序可迭代对象中的各项，并返回一个列表。
- zip：组合可迭代对象中的各项。
- enumerate：根据相对位置来配对可迭代对象的项。
- filter：选择一个函数为真的项。
- reduce：针对可迭代对象中的成对的项运行一个函数。

另外一些内置函数接受可迭代对象作为参数，使用迭代器来扫描它，但返回单个结果：

- sum：调用计算可迭代对象中的总数。
- any：任何项为真的时候返回True。
- all：所有项为真的时候返回True。
- min：返回可迭代对象中的最小值。
- max：返回可迭代对象中的最大值。

列表解析可以成为比map和filter更通用的工具：

```
# 列表解析与map
[x**2 for x in range(10)]
list(map((lambda x:x**2), range(10)))

# 列表解析与map，增加测试
# 方法一
[x for x in range(5) if x % 2 == 0]
# 方法二
list(filter((lambda x:x % 2 == 0), range(5)))
res = []
# 方法三
for x in range(5):
  if x % 2 == 0:
    res.append(x)
# 方法四
list(map((lambda x:x**2), filter((lambda x:x%2 == 0), range(10))))
```

# 生成器

生成器也称为“生成器函数”，是相对于普通函数的一种变形。普通函数接收输入参数并立即返回单个结果，但生成器函数自动在生成值的时刻挂起并继续函数的执行，这允许代码随着时间产生一系列的值。

生成器函数包含一条yield语句，该语句会被编译为生成器。当调用时，它们返回一个迭代器对象。如下比较使用生成器函数、普通函数、map或者列表解析。

最简单的生成器：

```
def abc_generator():
  yield 'a'
  yield 'b'
  yield 'c'

for char in abc_generator():
  print(char)
```

稍微复杂一点的`lazy generator`， 之所以叫"lazy"是因为它并不需要提前准备好所有数据，而仅仅是当需要的时候才生成这些数据：

```
# 生成器
def gensquare(N):
  for i in range(N):
    yield i ** 2

# 普通函数
def buildsquare(n):
  res = []
  for i in range(n):
    res.append(i ** 2)
  return res

# 列表解析
[n**2 for n in range(5)]

# map
[map((lambda n: n**2), range(5))]
```

生成器在内存使用和性能方面都很好。它们允许函数避免临时再做所有的工作，当结果的列表很大或者在处理每一个结果都需要很多时间时，这一点尤其有用。

# Python3.0 解析语法概括

在最新版本的Python中，迭代器和列表解析的概念形成了这种语言的一个新的特性：生成器表达式。从语法上讲，生成器表达式就像一般的列表解析，但它们是包含在圆括号而不是方括号中：

```
(x ** 2 for x in range(5))

# 以下两者等价
[x ** 2 for x in range(5)]
list(x ** 2 for x in range(5))
```

在执行过程上，生成器表达式很不相同：不是在内存中构建结果，而是返回一个生成器对象，这个对象支持迭代器协议并在任意的迭代语境的操作中。我们一般不会使用next迭代器来操作生成器表达式，因为for循环会自动触发。

和列表解析及生成器表达式一样，集合和字典解析都支持嵌套相关的if子句从结果中过滤掉元素：

```
# 列表解析，有序
[x*x for x in range(10) if x%2 == 0]

# 集合解析，无序
{x*x for x in range(10) if x%2 == 0}

# 字典解析
{x:x*x for x in range(10) if x%2 == 0}
```
