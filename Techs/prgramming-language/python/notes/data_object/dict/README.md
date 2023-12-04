## 字典

字典类似小型数据库，使用健高效地存储和检索数据。字典中的每个键都被转换为一个数字，即散列值，字典的值存储在底层列表中，散列值被用做它们的索引。访问值时，把提供的键转换为散列值，再跳到列表的对应位置。

- 字典中的键必须唯一。
- 键是不可变的。
- 在访问键值时如果不确定键是否存在可以先用`key in d`进行检查。
- 函数keys(), items(), values()可以创建视图。

常见方法：

- a.update(b) # 将b中的键值去更新a，不存在则存入，存在则刷新
- len(dict) #获取size
- d.pop('a') # 删除键'a'对应的记录，并返回值
- del d['a'] # 删除键'a'对应的记录
- a = b.copy()
- a.clear()
- key_list = a.keys()
- value_list = a.values()
- key in dict
- key not in dict


## 创建

常见的创建方式有两种：1）声明一个空字典，然后以键值来填充它。2）使用已有的数据进行创建，即通过在大括号（`{}`）中使用冒号（`:`）将键和值隔开进行创建。

```
# 空的字典
color = {}
color = dict()

# 初始化的字典
color = {'red':1, 'blue':2, 'green':3}

# 
key_list = [1, 2, 3]
value_list = ['simon', 'john', 'juye']
mapping = zip(key_list, value_list)
d = dict(mapping)
```

那如何创建一个空的列表作为值的空字典呢？查找了一些资料，似乎无法完成一个空的字典，确定值的类型为空的列表。也就是必须要首先确定`键值`。

```
data = {k: [] for k in range(2)}

dictLists = {key: [] for key in ["xcg", "bsd", ...]}
dictLists = dict((key, []) for key in ["xcg", "bsd", ...]) #python2.x
```

参考：

- [How to initialize a dictionary of empty lists in Python?](https://thewebdev.info/2021/11/01/how-to-initialize-a-dictionary-of-empty-lists-in-python/)
- [Most efficient way to create a dictionary of empty lists in Python?](https://stackoverflow.com/questions/10852345/most-efficient-way-to-create-a-dictionary-of-empty-lists-in-python)


## 字典的访问

访问字典的时候可以在1）在方括号（[]）中指定键，或者2）使用get方法指定键对值进行引用。前者获取一个不存在的键值会反馈`KeyError`错误，后者返回`None`但是没有错误。

我们能够通过给新的键赋值来扩展字典。避免该错误的一个技巧就是使用in关系表达式进行测试。

```
'f' in D

if not 'f' in D:
  print('missing')
```

在遍历字典时，可以可以分别遍历key和value，也可以同时遍历key和value:

```
for key in d:
  pass

for value in d:
  pass

for key,value in d.items():
  pass

for kv in d.items():
  pass
```

## 字典的修改

在使用`=`对字典进行修改时，如果键存在于字典中，就会对相应的值进行修改，否则，新的键和值就会被添加到字典中。


## 键的排序

相比list, dict是无序而且也无法排序。如果我们确实需要强调某种顺序的时候，一个常用的解决办法就是通过字典的keys方法收集一个键的列表，使用列表的sort方法进行排序，然后使用Python的for循环逐个进行显示结果：

```
ks = list(D.keys())
ks.sort()
for key in ks:
  print(key, '=>', D[key])

for key in sorted(D):
  print(key, '=>', D[key])
```

## 如何获取第一个键值

```
ks = list(D.keys())
ks[0]
```

## 如何判断字典是空的

if dict:
  print("NOT EMPTY")

