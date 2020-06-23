# 映射

主要有字典，支持通过键进行索引。其中的列表和字典是可变的，而数字、字符串、元组是不可变的。

字典类似小型数据库，使用健高效地存储和检索数据。字典中的每个键都被转换为一个数字，即散列值，字典的值存储在底层列表中，散列值被用做它们的索引。访问值时，把提供的键转换为散列值，再跳到列表的对应位置。

- 字典中的键必须唯一。
- 键是不可变的。
- 在访问键值时如果不确定键是否存在可以先用`key in d`进行检查。
- 函数keys(), items(), values()可以创建视图。

## 字典的创建

键的创建方式有多种：

- 使用常量的方式
- 声明一个空字典，然后每次以一个键来填充它

```
color = {'red':1, 'blue':2, 'green':3}

key_list = [1, 2, 3]
value_list = ['simon', 'john', 'juye']
mapping = zip(key_list, value_list)
d = dict(mapping)

color = {}
color = dict()
```

## 字典的访问

1. if测试

我们能够通过给新的键赋值来扩展字典，但是获取一个不存在的键值仍然是一个错误。避免该错误的
一个技巧就是使用in关系表达式进行测试。

```
'f' in D

if not 'f' in D:
  print('missing')
```

2. 遍历

可以分别遍历key和value:

```
for key in d:
  pass

for value in d:
  pass
```

同时遍历key和value:

```
for key,value in d.items():
  pass

for kv in d.items():
  pass
```

## 键的排序

相比list, dict是无序而且也无法排序。如果我们确实需要强调某种顺序的时候，一个常用的解决办
法就是通过字典的keys方法收集一个键的列表，使用列表的sort方法进行排序，然后使用Python的
for循环逐个进行显示结果：

```
ks = list(D.keys())
ks.sort()
for key in ks:
  print(key, '=>', D[key])

for key in sorted(D):
  print(key, '=>', D[key])
```

## 常见方法

- a = b.copy()
- a.clear()
- key_list = a.keys()
- value_list = a.values()
- key in dict
- key not in dict
