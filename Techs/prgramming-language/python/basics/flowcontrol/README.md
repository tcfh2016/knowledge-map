Python里面的流程控制包括两种：条件语句（`if`）和循环语句（`for`, `while`）。

两种循环语句：for循环和while循环。While语句提供了编写通用循环的一种方法，for语句用来遍历序列对象内的元素，并对每个元素运行一个代码块。

## if语句

```
if (condition):
  // TODO.
elif (condition):
  // TODO.
else:
  // TODO.
```

- Python中条件语句的括号不是必须的，可以使用`and`, `or`, `not`等关键词结合多个条件判断
- `elif`语句可以1个或多个
- `else`可有可无
- Python没有条件表达式，可以通过`a if condition else b`来模拟。

参考：

-[Does Python have a ternary conditional operator?](https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator)

### 值的测试

Python不仅仅可以使用布尔型变量作为条件，它可以直接在if中使用任何表达式作为条件，大部分表达式的值都会被当作True，但以下表达式值会被当作False：

- False
- None
- 0
- 空字符串，空列表，空字典，空集合


## for 循环

for循环可以适用于任何类型的迭代器，包括字符串、列表、元组、其他内置可迭代对象以及能够通过类所创建的新对象。使用形式如下：

```
for <target> in <object>:
  <statements>
else:
  <statements>
```

range函数是通用的工具，常用在for循环中来产生索引。

当`for`语句和`if`语句结合使用的时候，有没有比较好的方式将它们结合起来。比如常见的写法如下：

```
for case in caselist1:
    if case not in caselist2:
        print(case)
```

没想到在世界上的其他地方还真有人有和我一样的想法：[Pythonic way to combine for-loop and if-statement](https://stackoverflow.com/questions/6981717/pythonic-way-to-combine-for-loop-and-if-statement)，其中的讨论给出了不同的做法，但是最受欢迎的建议却是不要过度做优化让代码显得不直接。

方法一：使用lambda

比如上面的三句可以使用`print([x for x in caselist1 if x in caselist2])`来实现，不过如果这里不是`print`，这种方式或许将不适用。

方法二：使用生成器

```
gen = (x for x in xyz if x not in a)
for x in gen:
    print(x)
```

方法三：使用过滤器

```
for x in filter(lambda x:x not in set2, set1):
    print(x)
```

## while 循环

while循环相比for循环更为灵活，使用形式如下：

```
while (test1):
  statement1
  if (test2): break
  if (test3): continue
  if (test4): pass
else:
  statement2
```

- `pass语句`：表示什么事也不做，只是空占位语句。当我们无法保持函数体为空而不产生语法错误，或者只是暂时用于填充函数主体时可以使用pass来替代。
- `循环else块`：只有当循环正常离开时才会执行（也就是没有碰到break语句），这种结构可以让你捕获循环的“另一条”出路，而不通过设定和检查标志位或条件。`else`通常需要何`break`连用。

在循环里使用break/continue语句可以完成更复杂的功能，与之相关的一个建议是：尽可能少地使用它们。
