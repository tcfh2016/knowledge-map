STL库里面的部分函数会同时在algorithm与container中有实现，比如如remove(), swap()：

<algorithm>
```
// std::remove
template <class ForwardIterator, class T>
  ForwardIterator remove (ForwardIterator first, ForwardIterator last, const T& val);

// std::swap
template <class T> void swap (T& a, T& b);
```

<list>
```
// std::list::remove
void remove (const value_type& val);

// std::list::swap
void swap (list& x);
```

这是STL在设计上的特性所决定的：一方面STL的泛型编程范式需要算法具有一定的通用性，即对所有
的容器均支持。另一方面，每种容器本身的数据组织形式是不一样的，这也就决定了同一种算法在不
同容器上的表现不同。通常，容器的自身提供的操作函数拥有更好效率，往往也更“易用”。

如下代码是用来解释“易用性”的一个例子:

```
std::list<int> coll;

for (int i=0; i < 6; ++i)
{
  coll.push_front(i);
  coll.push_back(i);
}

```

当前向list中添加了10个元素：5 4 3 2 1 0 0 1 2 3 4 5，假如我们要使用algorithm中的remove
函数删除其中的3，我们需要这样做：

```
coll.erase(remove(coll.begin(), coll.end(), 3), coll.end());
```

之所以这样做是因为使用std::remove()来进行操作的时候，它使用内部算法删除了其中的3，但不会
对容器做过多的操作，比如list中的元素个数依然与删除之前一样。所以才使得一个简单的删除操作
需要通过两次函数调用来完成。然而，如果使用容器本身提供的函数，只需要调用一次：

```
coll.remove(4);
```
