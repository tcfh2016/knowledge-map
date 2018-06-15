
# [lambda表达式的使用](https://www.zhihu.com/question/20125256)

lambda表达式可以看成是一个匿名函数，它支持多个参数但只能够有一个表达式。那它的好处在什么
地方？比如下面的代码：

```
def sq(x):
    return x * x

map(sq, [y for y in range(10)])
```

可以用一条简单的语句搞定：

```
map(lambda x: x*x, [y for y in range(10)])
```

这种使用方式在一些函数只会少量使用的时候能够使得程序看起来更加简洁。


# map, filter, reduce

大多时候lambda表达式传递给一些接收函数对象的函数，比如`map`, `filter`或`reduce`。

`map`的原型如下，它接收一个函数对象和多个可以迭代的参数比如list, dictionary，它将函数
对象应用到每个参数并返回被改变的列表。

```
map(function_object, iterable1, iterable2,...)
```

`filter`的原型如下，它只接受2个参数，目的是将iterable里满足function_object条件的元素
过滤出来。

```
filter(function_object, iterable)
```

`reduce`是迭代将function_object应用到iterable里，每次对前两个元素进行运用。可以用来实
现累加运算。

```
reduce(function_object, iterable)
```

# 参考

- [Lambda, filter, reduce and map](https://www.python-course.eu/lambda.php)
- [lambda, map and filter in Python](https://medium.com/@happymishra66/lambda-map-and-filter-in-python-4935f248593)
