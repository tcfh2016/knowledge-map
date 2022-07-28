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
- `循环else块`：只有当循环正常离开时才会执行（也就是没有碰到break语句），这种结构可以让你捕获循环的“另一条”出路，而不通过设定和检查标志位或条件。

在循环里使用break/continue语句可以完成更复杂的功能，与之相关的一个建议是：尽可能少地使用它们。
