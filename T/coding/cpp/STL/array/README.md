array容器最先在TR1中引入，它基于C语言数组语义之上提供了STL容器的接口，因此相比C数组它更安全，也更易用。由于array是一个具有固定大小的容器，因此你无法增加或者删除元素并改变容器的大小，而是只能够通过“替换”操作来抹去某个元素的值。

如果你需要一个用来存储元素并拥有固定大小的序列，array<>是一个不错的选择因为其在效率上不逊的表现：

- 内存分配在栈上（通常情况下）。
- reallocation不会发生。
- 支持随机存取。

在进行随机存取时，操作元素的索引必须由调用者予以保证，当然你也可以直接使用at()接口：

```
template <typename C>
void foo(C& coll)
{
  if (coll.size() > 5)
  {
    coll[5] = ...;
  }

  coll.at(5) = ...;
}
```

array的异常处理支持有限，仅仅在使用at()时提供元素索引检查时可能抛出`out_of_range`异常。

## std::array的常见用法

1）初始化


2）填充

- `c.fill(val)` 将c里面所有的元素填写为val


## std::array如何与C-style的操作连用

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
