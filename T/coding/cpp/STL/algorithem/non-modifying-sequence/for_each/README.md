## [std::for_each](https://en.cppreference.com/w/cpp/algorithm/for_each)

`for_each`在C++11之前是运用最多的算法之一，它用来对指定迭代区间的每个元素执行读/写的操作。不过C++11提供了更便捷的[Range-based for loop](https://en.cppreference.com/w/cpp/language/range-for)，如下：

```
// before c++11
void square(auto &elem)
{
  elem = elem * elem;
}

for_each(coll.begin(), coll.end(), square)

// after c++11
for (auto &elem : coll)
{
  elem = elem *elem
}
```
