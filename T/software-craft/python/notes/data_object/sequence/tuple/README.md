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
