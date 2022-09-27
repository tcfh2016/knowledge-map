## 编码规约

当你复制粘贴代码的时候，基本上都会使未来的维护工作倍增。考虑一下：如果最初的版本发生改变，将修改两个地方的代码。当你试图按照这种复制代码的方式来编写程序的时候，可能需要考虑一下有没有更好的方法。[*Ref: 《Python学习手册》第4版 P661，机械工业出版社，Mark Lutz。*]()


- 所有的源代码文件都以`# -*- coding: utf-8 -*-`开头。
- 定义类的时候按照新格式`class A(object)`。
- 类名使用驼峰命名法。
- 文件名/方法名/变量使用小写字母+下划线的方式：
  - 方法名以动词开头。
  - 变量命不以动词开头。

## 如何换行？

引用Google Python Style Guide，在[3.2 Line length](https://google.github.io/styleguide/pyguide.html#32-line-length)定义了代码行最大长度为80个字符，如果超过80个字符需要另起一行，主要分下面几种情况：

1）超行的是函数定义

直接另起一行，不过需要考虑可读性。尤其是换行的是函数定义，请参考[3.19.2 Line Breaking](https://google.github.io/styleguide/pyguide.html#3192-line-breaking)里面的内容。

```
foo_bar(self, width, height, color='black', design=None, x='foo',
        emphasis=None, highlight=0)

if (width == 0 and height == 0 and
   color == 'red' and emphasis == 'strong'):
```

2）超行的是`with`语句 或者 if语句

`with`语句换行时需要添加`\`来另起一行，比如：

```
with very_long_first_expression_function() as spam, \
     very_long_second_expression_function() as beans, \
     third_thing() as eggs:
    place_order(eggs, beans, spam, beans)
```

3）超行的是字符串

使用`()`来进行隐式连结：

```
x = ('This will build a very long long '
     'long long long long long long string')
```

## 注释
