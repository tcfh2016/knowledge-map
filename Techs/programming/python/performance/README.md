## 怎么测量程序的执行时间

程序执行的时间可以分为两种：

1，clock time：包含程序占用CPU的时间，以及等待其他资源的时间，比如I/O
2，cpu time：仅仅是占用CPU的时间


## 使用`time`模块中的`time()`函数

计算结束时间点和起始时间点的差值，单位为秒：

```
import time

st = time.time()
...
et = time.time()

print("execution time {} seconds", et - st)
```

如果想要转换为毫秒，可以乘以1000，另外可以使用`time.strftime("%H:%M:%S", time.gmtime(et-st))`来调整显示格式。

参考：

- [Python Measure the Execution Time of a Program](https://pynative.com/python-get-execution-time-of-program/)

## 使用`time.process_time()`计算CPU时间

```
import time

st = time.process_time()
...
et = time.process_time()

print("cpu execution time {} seconds", et - st)
```

## 使用`timeit.timeit()`测试代码行或函数

该测试的值也是程序执行的总时间：

```
def func():
    ...

# 函数func()执行1000次的总时间
result = timeit.timeit(stmt='func()', globals=globals(), number=1000)
```

参考：

- [timeit — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)