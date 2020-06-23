# 序列

包括字符串、列表、元组，支持索引、分片和合并等操作。

序列的索引是按照从最前面的偏移量进行编码的，也就是从0开始，第一项索引为0，第二项索引为1，
依次类推。Python支持反向索引，从最后一个开始计算。一般来说，负的索引号会简单地与字符串的
长度相加。

需要留意的是，尽管序列操作是通用的，但方法不通用。一条简明的法则是这样的：可作用于多种类
型的通用型操作都是以内置函数或表达式的形式出现的（比如len(X), x[0]），但类型特定的操作是
以方法调用的形式出现的（比如string.upper()）。你可以通过dir来查看对象支持的所有方法，并
使用help来查找帮助信息。

## 字符串

字符串，字符串可以通过单引号、双引号、三引号来包含，前两种形式没有太大区别但可以使得这两
种类型互相包含，而三引号则可以包含多行字符串。字符串的使用场景非常多，所以Python提供了强
大的字符串支持。

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

## 元组

元组与字符串、列表同属于序列类型，即按照顺序排列的一组值，支持索引和切片。

元组的特点：

- 不可变，杜绝了无意修改元组的可能，有助于防范错误。--> 提供了一种完整性的约束。
- 即便对元组进行细微修改，必须复制元组再创建新元组。
- 支持 `x in s`来检查元素是否在序列中。

元组的定义：

```
pets = ()                        # 创建空元组。
pets = ('dog',)                  # 创建单个元素的元组，逗号不可省略。
pets = ('dog', 'cat', 'bird',)   # 创建包含3个元素的元组，最后一个逗号可以省略。
```

常见方法：

- a in tuple
- a not in tuple
- min(tuple)
- max(tuple)
- sorted(tuple)
- tuple.count(e)
- tuple.index(e)
- len(tuple)

## 列表

list是一种可以将多个数值组合在一起的复合数据类型，这些数值可以是不同的数据类型。当然list
也可以内嵌包含。相比元组，列表可以在不复制的情况下添加、删除或修改元素。

- len()获取长度。
- 使用方括号来定义，支持索引和切片。对列表进行分片时往往返回一个新的列表。
- 定义包含单个元素的列表不需要逗号结尾。
- list.sort()和list.reverse()会就地修改列表，不会制作拷贝。
- list.extend(anotherlist)类似于 list.append(element)，在末尾添加元素，但前者添加整
个列表。

列表解析(list comprehensions)是创建列表的特殊方法，它是一种通过对序列中的每一项运行一个表达式来创建一个新列表的方法，每次一个，从左到右，它编写起来更加精简，且比手动的for循环语句运行得更快（往往会快1倍），因为迭代在解析器内部是以C语言的速度执行的。当考虑在每项上执行一个操作时，都可以考虑使用列表解析。

```
# 空列表
l = []

# example 1:
[n*n for n in rang(1,11)] # 这种方式可以变形为 l = [n for n in range(1,11)]

# example 2:
numbers = [-1, 0, 6, -4, -2, 3]
res = [n for n in numbers if n > 0]

# example 3: 如何生成多个相同元素的列表？
res = [9] * 8 # 生成8个包含9的列表

# 创建 1000000 个符合均值1.5方差2的伪随机数。
a = [gauss(1.5, 2) for i in range(1000000)]

# 移除字母p开头的行末尾的换行符
lines = [line.rstrip() for line in open('script1.py') if line[0] == 'p']
```

3) 增删操作

列表的扩展可以通过"+"操作来完成（列表+列表，添加单一元素使用`append()`方法），而删除操
作需要使用`del()`指定对应列表元素集合。

*`;`用来在一行代码里面分割不同的代码指令。*

4) 列表拷贝

直接通过“=”来拷贝列表那么拷贝变量和被拷贝变量都指向相同的对象，

```
# areas, areas_copy都指向相同的对象。
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = areas

# 通过list()进行复制拷贝，areas, areas_copy都指向各自不同的对象。
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas)

```

5) 遍历操作（Excursion）

使用`for`语句来遍历列表，Python提供了一种极具扩展性的遍历方式使得你可以不用去管被遍历的
list中元素的数据类型。

6) 常见方法

  - len(list) 获取列表的长度。比如计算平均值 sum(list) / len(list),sum()属于内建函数。
  - min(list)
  - max(list)
  - list.sort() 默认升序的排序操作，可以通过`reverse=True`转换为降序，`key`来指定排序方法。

7）查询操作

```
if 3 in l:
  pass
else:
  pass
```

`list`也是一个可变的序列。常见方法：

- list.append(elem)
- list.pop(index)，默认移除最后一个元素
- list.extend(new_list)，合并另一个列表
- list.insert(index, elem)
- list.remove(elem)
- list.clear()
- list.sort()，排序，会修改原字符串
- list.reverse()
- list.count(elem)
- list.index(elem)
- a in list
- a not in list
- min(list)
- max(list)
- sorted(list)，排序，不会修改原字符串

## 切片

无论是可变序列（list, bytearray）还是不可变序列（tuple, string, bytes）都支持切片操作。

首先对于这些序列的元素都能够按照索引进行访问，索引从前往后从0开始，从后往前自-1开始，以list为例：

```
[a, b, c, d, e, f, g]
 0  1  2  3  4  5  6
-7 -6 -5 -4 -3 -2 -1
```

序列的切片遵循前闭后开的原则：[start, end)，同时也支持省略：省略start默认从第一个元素开始，省略end，默认最后一个元素+1。三种切片形式：

```
list[0:2]
list[0:]
list[:2]
list[0:2:1] 指定切片间隔/步长
```



## 常见问题

1. 如何查找列表中某个元素的下标？



参考：

- [Finding the index of an item in a list](https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list)
