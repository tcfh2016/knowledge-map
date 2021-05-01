## std::vector

vector实现了动态数组，它是一种提供随机访存的序列容器。我们在末端添加和删除元素是高效的，如果添加或删除中间元素效率则会大大降低（*注意也会让该元素后面的指针、引用或者迭代器失效。*）。

由于vector需要满足元素的动态增长的要求，它在添加元素的过程中可能进行内存的重新分配。这一点非常重要，因为内存重新分配之后之前指向该区域的所有指针、引用或者迭代器通通都会失效。vector提供了`capacity()`来反馈它当前内存能够存放的最大元素个数，超出则会进行内存再分配。在效率为重要考虑因素的场景下，为了避免内存有两种方式可以参考：

- `v.reserve(80)`：直接reserve最大的元素空间。
- `std::vector<T> v(5)`：初始化最大的元素空间。

上面第二种没有前一种好因为它会对每个元素执行初始化，也耗费一些时间。当然，如果上面两种都没有使用那么在首次压入元素时分配的capacity()是与实现相关的，有可能会占用比较多的内存。

## 常见用法

### *初始化*

C++11之前的初始化通常是首先创建空的vector，或者利用拷贝或者赋值构造基于其他vector来创建。C++11支持更加便捷的初始化方式，比如支持move构造器和初始化列表。

```
vector<E> c; // 空的vector
vector<E> c(c2); // 基于copy构造器创建
vector<E> c = c2; // 基于copy构造器创建
vector<E> c(n, elem); // 创建n个相同的elem
vector<E> c(begin, end); // 基于迭代器创建

vector<E> c(rv); // 基于move构造器创建（C++11）
vector<E> c = rv; // 基于move构造器创建（C++11）

vector<int> deck({ 0, 1, 2, 3, 4, 5 }); //基于初始化列表创建（C++11）
vector<int> deck = { 0, 1, 2, 3, 4, 5 }; //基于初始化列表创建（C++11）
```


### *读取*

- c.empty()
- c.size() 当前元素个数
- c.max_size() 最大可能的元素个数
- c.capacity() 不进行内存重分配下最大的元素个数
- c[idx]/c.at(idx) 后者提供范围检查，超出时抛出`out_of_range`异常
- c.front()/c.back() 第一个/最后一个元素


### *修改*

- c = c2/rv/initlist 赋值，调用构造器
- c.reserve() 预留容量
- c.resize(num) 改变当前元素个数，如果新增了元素那么调用默认构造器进行初始化
- c.assign(n, elem)/c.assign(beg, end)/c.assign(initlist) 赋值，调用构造器
- c.push_back(elem)/c.emplace_back(args...) 后面是C++11新接口，不需要进行elem拷贝所以更高效


### vector<bool>

`vector<bool>`尝试着从节省内存空间的角度来实现bool类型的vector，它为每位bool使用1个bit，而不像常规的1个byte。不过，由于C++最小的寻址单位是1个byte，所以这种实现在操作引用和迭代器上会有着种种限制。

如果你仅仅需要使用固定大小的bit位，那么使用`bitset`就够了。

## Q&A

1. 如何像array.fill()那样将所有元素赋值为相同的值？

std::vector并没有std::array自带的`fill()`函数，但是我们可以直接使用算法中的`std::fill()`来进行填充。原型如下：

```
template< class ForwardIt, class T >
void fill( ForwardIt first, ForwardIt last, const T& value );
```

2. 将vector当作C风格数组一样使用

一个比较重要的一点是用`v.data()`来替代vector的首地址。
