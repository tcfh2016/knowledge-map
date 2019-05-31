Python提供了许多支持函数编程的工具，其中包括比如filter, map, reduce应用于输入集合所有元
素的函数。

比如map()函数支持函数对象，它将even函数应用于range(10)所有元素：

```
def even(x):             
  return x % 2 == 0         
even(3)

map(even, range(10))
```

另一种更简洁的方法，是直接将函数的定义作为参数使用，这个时候需要使用`lambda`关键字，这种
定义也称为“匿名函数”：

```
map(lambda x: x % 2 == 0, range(10))
```
