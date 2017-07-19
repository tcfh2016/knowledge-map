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

这是STL在设计上的特性所决定的：

- 一方面，STL的泛型编程范式需要算法具有一定的通用性，即对所有的容器均支持。
- 另一方面，每种容器本身具有不同，一种算法在一种容器上高效，在另一种容器可能就低效。
