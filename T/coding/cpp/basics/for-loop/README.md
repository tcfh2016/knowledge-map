## for循环

C++17之前是不支持在for循环初始化时使用多种类型的数据，但是C++17就可以：

```
for (auto [i, rnti, floatWeight] = std::tuple{0, 1000, 9.1}; i < maxNumOfUes; ++i, ++rnti, floatWeight+=0.1)
```

参考：

- [Is it possible to declare two variables of different types in a for loop?](https://stackoverflow.com/questions/2687392/is-it-possible-to-declare-two-variables-of-different-types-in-a-for-loop)
