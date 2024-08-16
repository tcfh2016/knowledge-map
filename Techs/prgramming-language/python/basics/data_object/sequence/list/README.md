## 列表

list是一种可以将多个数值组合在一起的复合数据类型，这些数值可以是不同的数据类型。当然list也可以内嵌包含。相比元组，列表可以在不复制的情况下添加、删除或修改元素。 `list`也是一个可变的序列。

## 方法

- a in list
- a not in list
- list.count(elem)
- list.index(elem)
- min(list)
- max(list)
- len(list) 获取列表的长度

- list.append(6) # 在末尾添加1个元素
- list.extend([7, 8]) # 在末尾添加多个元素
- list_a + list_b # 将两个列表进行合并
- list.remove(elem) # 将最开始找到的元素删除，*按值匹配，找不到报错*
- list.pop(index) # 删除对应索引位置的元素，并返回该元素的值，`del l[index]`删除对应位置的元素
- list.clear() # 清除所有元素
- list.sort() 默认升序的排序操作，可以通过`reverse=True`转换为降序，`key`来指定排序方法。
- list.sort()和list.reverse()会就地修改列表，不会制作拷贝。
- sorted(list)，排序，不会修改原字符串
- list.insert(index, elem)
- list.reverse()，反转，在原来的list反转，*并不会有返回值*


## 创建

使用方括号来定义，支持索引和切片。对列表进行分片时往往返回一个新的列表。

```
# 空列表
l = []
```

列表解析(list comprehensions)是创建列表的特殊方法，它是一种通过对序列中的每一项运行一个表达式来创建一个新列表的方法，每次一个，从左到右，它编写起来更加精简，且比手动的for循环语句运行得更快（往往会快1倍），因为迭代在解析器内部是以C语言的速度执行的。当考虑在每项上执行一个操作时，都可以考虑使用列表解析。

```
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

## 查找

用`in`和`not in`来测试某个元素是否在列表中。

用`index`查找某个元素在列表中的位置，没有找到会报`ValueError`错。


## 拷贝

直接通过“=”来拷贝列表那么拷贝变量和被拷贝变量都指向相同的对象，

```
# areas, areas_copy都指向相同的对象。
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = areas

# 通过list()进行复制拷贝，areas, areas_copy都指向各自不同的对象。
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas)
```


## 遍历（Excursion）

使用`for`语句来遍历列表，Python提供了一种极具扩展性的遍历方式使得你可以不用去管被遍历的list中元素的数据类型。遍历的方式有三种：

```
# 方式一：仅关心列表内容
for elem in list:
    #...

# 方式二：关心列表索引
for idx in range(len(list)):
    #...

# 方式三：仅关心列表索引和内容
for idx, text in enumerate(labels):
    #...
```

逆序遍历：

```
list(reversed(xs))
xs.reverse() # 修改之前列表
xs[::-1]
```

参考：

- [](https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards)

## 删除

有没有直接通过“+”或“-”来进行列表的删除操作？

答：很遗憾，亲自尝试，并没有。不过在[Python list subtraction operation](https://stackoverflow.com/questions/3428536/python-list-subtraction-operation)给出了两个思路：使用set（支持“-”操作和“|”操作），或者使用列表解析式（`[item for item in x if item not in y]`）。


## 求均值

sum(l) / len(l)
