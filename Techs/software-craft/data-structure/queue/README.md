## 队列

队列也是一种线性的数据结构，有着先进先出操作顺序。它与栈的不同之处在于删除元素时的选择，栈是删除最近添加进来的元素，队列是删除最初添加进来的元素。队列一般使用在不需要立即处理事件，并且需要依照先进先出的顺序进行处理的场景中，常见于磁盘、CPU资源调度。

## 常用函数

```
begin() / end()
front() / back()
```