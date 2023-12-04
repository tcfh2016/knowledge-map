## 集合

集合是一系列不重复的且不可修改的元素，类似于字典，但只包含键没有值，它的顺序是不确定的。由于它的使用场景较少，暂不详述。

集合（set）可以用来把重复项从其他集合（collection）中过滤掉，直接把collection转换为set然后再转换回来即可：

```
l = {1, 2, 3}

l = [1, 2, 1, 3, 2, 4, 5]
l = list(set(l))
```

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

常见操作：

- alpha.union(beta) 等同于 alpha | beta
- alpha.intersection(beta) 等同于 alpha & beta
- alpha.difference(beta) 等同于 alpha - beta
- alpha.symmetric_difference(beta) 等同于 alpha ^ beta
- epsilon.isdisjoint(delta) 判断两个集合是否包含相同的元素
- epsilon.issubset(delta)
- a.issuperset(b)
- a.add(e)
- a.discard(e)
- a.remove(e)
- a.pop()
- b = a.copy()
- a.clear()

## 声明

使用`s = {1}`可以直接识别为`set`类型，但如果使用`s = {}`会识别为`dict`，如果调用`s.add(1)`添加时会出错。

可以使用`s = set()`来声明。

