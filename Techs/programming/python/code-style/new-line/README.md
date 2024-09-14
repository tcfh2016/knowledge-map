引用Google Python Style Guide，在[3.2 Line length](https://google.github.io/styleguide/pyguide.html#32-line-length)定义了代码行最大长度为80个字符，如果超过80个字符需要另起一行，主要分下面几种情况：


## 超行的是函数定义

直接另起一行，不过需要考虑可读性。尤其是换行的是函数定义，请参考[3.19.2 Line Breaking](https://google.github.io/styleguide/pyguide.html#3192-line-breaking)里面的内容。

```
foo_bar(self, width, height, color='black', design=None, x='foo',
        emphasis=None, highlight=0)

if (width == 0 and height == 0 and
   color == 'red' and emphasis == 'strong'):
```


## 超行的是`with`语句 或者 if语句

`with`语句换行时需要添加`\`来另起一行，比如：

```
with very_long_first_expression_function() as spam, \
     very_long_second_expression_function() as beans, \
     third_thing() as eggs:
    place_order(eggs, beans, spam, beans)
```

然而，使用if语句的时候，是否需要添加`\`需要视情况而定，比如下面的代码就不需要添加：

```
if (a == 0 and b == 0 and
    c == 'red' and d == 'strong'):
    print("ok, I'm here")
```

但是下面的代码就需要，否则会在第一行提示“SyntaxError: invalid syntax”：

```
if (a == 0) and (b == 0) and \
    (c == 'red') and (d == 'strong'):
    print("ok, I'm here")
```

为啥？因为Python解析器在解析的时候会识别当前行是否结束，对于前者因为对多个条件使用了括号`()`所以可能将多行解析为一行，但是对于后者则是多个单独的语句，无法直接将其识别为一行，因此需要显示的连接，即使用`\`。


## 超行的是字符串

使用`()`来进行隐式连结：

```
x = ('This will build a very long long '
     'long long long long long long string')
```