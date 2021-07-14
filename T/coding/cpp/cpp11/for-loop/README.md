## C++11

for循环在C++11的时候引入了可以遍历给定区间、数组或者容器所有元素的新形式，基本语法如下：

```
for (decl : coll) {
  statement
}
```

如上格式中的`decl`可以是值，也可以是引用，区别在于如果是引用就不需要对每个元素调用构造器和析构器来创建临时的副本，而是直接基于原始元素来操作。


## C++17

C++17之前是不支持在for循环初始化时使用多种类型的数据，但是C++17就可以：

```
for (auto [i, rnti, floatWeight] = std::tuple{0, 1000, 9.1}; i < maxNumOfUes; ++i, ++rnti, floatWeight+=0.1)
```

参考：

- [Is it possible to declare two variables of different types in a for loop?](https://stackoverflow.com/questions/2687392/is-it-possible-to-declare-two-variables-of-different-types-in-a-for-loop)
