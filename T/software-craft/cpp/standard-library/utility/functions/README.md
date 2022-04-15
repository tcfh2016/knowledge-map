## [std::swap](https://en.cppreference.com/w/cpp/algorithm/swap)

`std::swap`在C++11之前是定义在algorithem库中的，之后则放到了utility库中，并且还新增了数组的操作。它的功能是用来将两个值进行互换操作。

```
int a = 5, b = 3;
std::swap(a,b);
```

## [std::move](https://en.cppreference.com/w/cpp/utility/move)

`std::move`是C++11之后引入的，和`std::swap`一样存放在utility库里面。它指示了传入的参数会被移动到新的对象里，这往往是为了更加高效的进行内存资源的转移。

```
std::string str = "Hello";
std::vector<std::string> v;

// 创建临时string对象拷贝str，再从临时string里面复制到vector里
v.push_back(str);

// 不需要创建临时string对象，而是直接将str内容移动到vector里，str变空。
v.push_back(std::move(str));
```

## std::next/ std::advance

Std::next and std::advance have same purpose which can be used to advance the iterator by a certain position:

```
template
void advance( InputIt& it, Distance n );

ForwardIterator next (ForwardIterator it,
       typename iterator_traits::difference_type n = 1);
```

The differences includes:

- std::next will advance by one by default, whereas std::advance() requires a distance.
- std::next returns an iterator after advancing n positions from the given base position, whereas std::advance does not return anything.
- std::next returns a new iterator to the desired position, whereas std::advance modifies its argument pointing to the desired position.


参考：

- [std::next vs std::advance in C++](https://www.geeksforgeeks.org/stdnext-vs-stdadvance-in-cpp/)
- [What's the difference between std::advance and std::next?](https://stackoverflow.com/questions/15017065/whats-the-difference-between-stdadvance-and-stdnext)
