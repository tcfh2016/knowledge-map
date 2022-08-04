## 列表

list是一种可以将多个数值组合在一起的复合数据类型，这些数值可以是不同的数据类型。当然list也可以内嵌包含。相比元组，列表可以在不复制的情况下添加、删除或修改元素。

- len()获取长度。
- 使用方括号来定义，支持索引和切片。对列表进行分片时往往返回一个新的列表。
- 定义包含单个元素的列表不需要逗号结尾。
- list.sort()和list.reverse()会就地修改列表，不会制作拷贝。
- list.extend(anotherlist)类似于 list.append(element)，在末尾添加元素，但前者添加整个列表。

## 创建

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

列表的扩展可以通过"+"操作来完成（列表+列表，添加单一元素使用`append()`方法），而删除操作需要使用`del()`指定对应列表元素集合。

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

使用`for`语句来遍历列表，Python提供了一种极具扩展性的遍历方式使得你可以不用去管被遍历的list中元素的数据类型。

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
