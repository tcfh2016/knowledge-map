Python里面的流程控制包括两种：条件语句和循环语句。

# 条件语句

```
if (condition):
  // TODO.
elif (condition):
  // TODO.
else:
  // TODO.
```

# 循环语句

两种循环语句：for循环和while循环。While语句提供了编写通用循环的一种方法，for语句用来遍
历序列对象内的元素，并对每个元素运行一个代码块。

## for 循环

for循环可以适用于任何类型的迭代器，包括字符串、列表、元组、其他内置可迭代对象以及能够通
过类所创建的新对象。使用形式如下：

```
for <target> in <object>:
  <statements>
else:
  <statements>
```

range函数是通用的工具，常用在for循环中来产生索引。

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

- `pass语句`：表示什么事也不做，只是空占位语句。当我们无法保持函数体为空而不产生语法错误，
或者只是暂时用于填充函数主体时可以使用pass来替代。
- `循环else块`：只有当循环正常离开时才会执行（也就是没有碰到break语句），这种结构可以让
你捕获循环的“另一条”出路，而不通过设定和检查标志位或条件。

在循环里使用break/continue语句可以完成更复杂的功能，与之相关的一个建议是：尽可能少地使
用它们。
