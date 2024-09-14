## 字符串

字符串，字符串可以通过单引号、双引号、三引号来包含，前两种形式没有太大区别但可以使得这两种类型互相包含，而三引号则可以包含多行字符串。字符串的使用场景非常多，所以Python提供了强大的字符串支持。

字符串是不可更改的，所以它的一些函数会返回新的字符串，不会改变原来字符串的值。

Python也支持原始（raw）字符串常量，即去掉反斜线转移机制，这样的字符串常量以字符“r”开头。

常见的字符串操作包括：

- 获取长度，通过调用`len(s)`来完成。
- 字符串拼接，使用`+`进行简单相加。
- t.capitalize()，转换为大写形式。
- t.split()，字符串分割，返回list。
- t.find('string')，查找字符串，返回index，未找到返回-1。
- t.replace(' ', '|')，替换字符。
- t.strip('htp:/')，删除特定字符串`头尾`特定的字符。*一定是头尾啊，其他地方用replace*
- t.rstrip()，删除字符串最右边的空白字符（未传入指定字符集作为参数）。

string类型用来处理字符串，单引号和双引号括起来的字符串本身没有什么不同，但是当你需要在字符串里面包含双引号的时候，那么就需要将该字符串包含的单引号里面（或者使用`\`进行转义），如：

```
h1 = 'he said: "hello!"'
h2 = 'he said: \"hello!\"'
```

如果你想在字符串里面适用单引号，那么也可以将其包含在双引号里面（或者使用`\`进行转义），如：

```
h3 = "It's fine!"
h4 = "It\'s fine!"
```

注意，raw string是可以让字符串的转义字符失效的：

```
h5 = r'It\'s fine!'
```

常用函数:

- len(str)
- min(str)
- max(str)
- sub_text in str
- str.count(ch)
- str.index(ch)
- str.index(ch, 3, 18)
- str.find(ch)
- str.startswith("strnew")
- str.endswith("strnew")
- str.upper()
- str.lower()
- str.split(ch)
- str.isalpha()
- str.isdigit()
- ",".join(['a', 'b', 'c'])
