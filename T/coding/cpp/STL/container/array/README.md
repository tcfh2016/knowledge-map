## std::array

array容器最先在TR1中引入，它基于C语言数组语义之上提供了STL容器的接口，因此相比C数组它更安全，也更易用。由于array是一个具有固定大小的容器，因此你无法增加或者删除元素并改变容器的大小，而是只能够通过“替换”操作来抹去某个元素的值。

如果你需要一个用来存储元素并拥有固定大小的序列，array<>是一个不错的选择因为其在效率上不逊的表现：

- 内存分配在栈上（通常情况下）。
- reallocation不会发生。
- 支持随机存取。

array的异常处理支持有限，仅仅在使用at()时提供元素索引检查时可能抛出`out_of_range`异常。


## 常见用法

### *初始化*

通过显示调用空的构造器（`T()`或者`T{}`for c++11）来将参数初始化为0的这种方式称为"zero initialized"，另一种不管不问的方式为"default initialized"。容器通常都需要进行显示初始化，但是`array<>`是唯一一个不指定初始化值时会保持"default initialized"方式的容器，这意味着对于`std::array<int, 2> x`这样的array里面的值将是随机的。

`array<>`的实现并没有提供支持初始化列表的构造器，所以你可以在创建它的时候使用初始化列表直接初始化元素的值。

```
std::array<int, 2> x = {} // 所有元素初始化为0
std::array<int, 2> x = {1, 2} // 元素依次初始化为1，2
std::array<int, 2> x = {1} // 初始化第1个元素为1，第2个元素初始化为0
std::array<int, 2> x ({1, 2}) // ERROR: 不支持构造器
```

`array<>`提供了`swap()`，不过它可以交换array容器的元素值，但是并不会交换容器内部的迭代器或者引用，也就是swap之后原先容器的迭代器指向的内容也已经改变了（并不会保持不变）。

### *读取*

- c.empty()
- c.size()
- c.at(idx) 在进行随机存取时，操作元素的索引必须由调用者予以保证，当然你也可以直接使用at()接口：
- c[idx]

### *修改*

- c.fill(val) 将c里面所有的元素填写为val
- c = c2
- c = rv


## Q&A

1）std::array如何与C-style的操作连用

比如下面的代码，会报`error: do not use array subscript when the index is not an integer constant expression; use gsl::at() instead [cppcoreguidelines-pro-bounds-constant-array-index,-warnings-as-errors]`的错误：

```
std::array<char, 20> printBuffer = {};
...
position += snprintf(&printBuffer[position], 20 - position, str);
```

需要将其更换为：

```
std::array<char, 20> printBuffer = {};
...
position += snprintf(printBuffer.data() + position, 20 - position, str);
```

参考：

- [Is the std::array bit compatible with the old C array?](https://stackoverflow.com/questions/39376813/is-the-stdarray-bit-compatible-with-the-old-c-array)
