## 列表

列表通常采用双向链表进行实现，所以它拥有着和array, vector, dequeue不同的特征：

- list不提供随记访问，所以如果要访问第几个元素，必须要逐个遍历，因此效率较低。如果访问首尾元素则不同。
- 增删某个元素，在位置已知的情况下/首尾元素会很快。


## 常用函数

```
front()
push_front()
pop_front

back()
push_back()
pop_back()

remove(val) // 移除所有值为val的元素
erase(pos) // 移除pos位置的元素
```

## Q&A

`erase()`有着比`remove()`更好的性能。
