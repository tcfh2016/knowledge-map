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
