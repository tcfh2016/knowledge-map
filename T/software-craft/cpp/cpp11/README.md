
### 常规

- 初始化列表。
- auto关键字，完成类型推导。
- range-based for循环。

###　迭代器
- cbegin()/cend()。

# 常见问题

## 编译提示` error: ‘move’ is not a member of ‘std’`

在编译一个c++11的例子的时候提示出错，只有查找是编译c++11时需要在编译选项中指定对应的编译
选项：

```
g++ move_semantics_test.cpp -std=c++11 -o move_semantics_test
```

参考：

- [C++ linux : error: ‘move’ is not a member of ‘std’ how to get around it?](https://stackoverflow.com/questions/7251251/c-linux-error-move-is-not-a-member-of-std-how-to-get-around-it)
- [What is std::move(), and when should it be used?](https://stackoverflow.com/questions/3413470/what-is-stdmove-and-when-should-it-be-used)
