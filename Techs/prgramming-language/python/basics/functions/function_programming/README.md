Python提供了许多支持函数编程的工具，其中包括比如filter, map, reduce应用于输入集合所有元素的函数。

## map()

比如map()函数支持函数对象，它将even函数应用于range(10)所有元素：

```
def even(x):             
  return x % 2 == 0         
even(3)

map(even, range(10))
```

另一种更简洁的方法，是直接将函数的定义作为参数使用，这个时候需要使用`lambda`关键字，这种定义也称为“匿名函数”：

```
map(lambda x: x % 2 == 0, range(10))
```

## filter()

类似于map()，但使用的函数对象需要是boolean类型的，以此达到可以过滤的效果。

```
def odd(val):
  return val % 2 # 奇数为 Ture, 偶数为 Flase

nums = range(10)
filter(odd, nums)  
filter(lambda val: val % 2, nums) # 使用lambda
print(list(filter(odd, nums))) # 过滤了偶数
```

## reduce()

```
def mult(x, y):
  return x * y

nums = range(1, 5)  
product = reduce(mult, nums) # 结果为 (((1 * 2) * 3) * 4) = 24
```
