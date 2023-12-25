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
