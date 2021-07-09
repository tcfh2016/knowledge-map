## std::pair

C++98的时候为pair定义了专门的类。TR1引入tuple的类型用来存放多个不同类型的元素，但此时元素个数限制在10个以内。C++11的时候tuple的元素个数不再是限制。

pair的类型是将两个不同的元素作为基本的操作单元，在map容器中使用pair来管理元素，pair的定义如下：

```
template <typename T1, typename T2>
struct pair {
  T1 first;
  T2 second;
  ...
}
```

### 常见用法

- `pair<T1, T2> p`: 创建一个pair元素，分别调用T1, T2的默认构造器进行初始化
- `pair<T1, T2> p(val1, val2)`: 创建一个pair元素，用val1, val2来初始化
- `pair<T1, T2> p(p2)`: 基于p2拷贝构造一个副本
- `pair<T1, T2> p(rv)`: 移动构造器，将rv内容移动给p
