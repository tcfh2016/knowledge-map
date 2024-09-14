## [range()](https://www.geeksforgeeks.org/python-range-function/)

函数`range()`用来生成一系列数字，它常用在循环场景。使用range()的时候可以通过指定三个参数来生成不同的数据集：

- start: 起始值
- stop: 结束标记，返回的数据集最大值为stop-1
- step: 步长

```
# 生成0...stop-1的数据集
range(stop)

# 生成start, stop-1的数据集
range(start, stop) takes two arguments.

# 修改默认1的步长为step
range(start, stop, step) takes three arguments.
```

## 怎样反转一个range ？

直观的写法是`range(stop - 1, start - 1, -1)`，但是在[Print a list in reverse order with range()?](https://stackoverflow.com/questions/7286365/print-a-list-in-reverse-order-with-range)给出了一个更优美的方式：

```
reversed(range(10))
```

## 如果结束位置比起始位置低怎么办？

比如下面的代码，不会有任何输出。

```
for i in range(0, -5, 1):
    print(i)
```
