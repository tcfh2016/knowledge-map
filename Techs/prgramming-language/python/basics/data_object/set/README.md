## 集合

集合是一系列不重复的且不可修改的元素，类似于字典，但只包含键没有值，它的顺序是不确定的。

常见操作：

- alpha.union(beta) #等同于 alpha | beta
- alpha.intersection(beta) #等同于 alpha & beta
- alpha.difference(beta) #等同于 alpha - beta
- alpha.symmetric_difference(beta) #等同于 alpha ^ beta
- epsilon.isdisjoint(delta) #判断两个集合是否包含相同的元素
- epsilon.issubset(delta) #判断epsilon是不是delta的子集
- a.issuperset(b)
- a.add(e) #添加单个元素
- a.update(e) #添加多个元素，和列表的extend类似
- a.remove(e) #移除单个元素，元素不存在报错
- a.discard(e) #移除单个元素，元素不存在不会报错
- a.pop()
- b = a.copy()
- a.clear()

## 创建集合

空集合必须使用`set()`来创建，因为Python中`{}`是一个空的字典。

所以使用`s = {1}`可以直接识别为`set`类型，但如果使用`s = {}`会识别为`dict`，如果调用`s.add(1)`添加时会出错。

```
s = set()
s = {1, 2, 3}

l = [1, 2, 1, 3, 2, 4, 5]
s = set(l)
```

## 操作集合

集合可以求取交集、并集和差集：

```
(set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除
>>> x & y         # 交集
set(['o'])
>>> x | y         # 并集
set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
>>> x - y         # 差集
set(['r', 'b', 'u', 'n'])
```

## 过滤重复项
集合（set）可以用来把重复项从其他集合（collection）中过滤掉，直接把collection转换为set然后再转换回来即可。

```
l = [1, 2, 1, 3, 2, 4, 5]
l = list(set(l))
```
