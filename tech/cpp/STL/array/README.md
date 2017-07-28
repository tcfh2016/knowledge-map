array容器最先在TR1中引入，它基于C语言数组语义之上提供了STL容器的接口，因此相比C数组它更
安全，也更易用。如果你需要一个用来存储元素并拥有固定大小的序列，array<>很有潜力：

- 内存可能分配在栈上。
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
