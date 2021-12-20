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


3.1 描述如何只用一个数组来实现三个栈。
3.2 请设计一个栈，除pop与push方法，还支持min方法，可返回栈元素中的最小值。push, pop和min三个方法的时间复杂度必须为O(1)。
3.3 设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。请实现数据结构SetOfStacks，模拟这种行为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。此外，SetOfStacks.push()和SetOfStacks.pop()应该与普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。

进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。
