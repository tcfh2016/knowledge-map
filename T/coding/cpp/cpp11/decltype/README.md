## decltype

c++11使用了新的关键字`decltype`用来让编译器在编译的阶段求得一个表达式的类型。它的使用场景主要有三个：1）定义返回值类型；2）在metaprogramming中使用；3）传递一个lambda的类型。


### 使用场景之一：定义返回值类型

```
template <typename T1, typename T2>
auto add(T1 x, T2 y) -> decltype(x+y);     
```

### 使用场景之二：在metaprogramming中使用

比如对于`std::common_type`的实现：

```
template <typename T1, typename T2>
struct common_type<T1, T2> {
  typedef decltype(true ? declval<T1>() : declval<T2>()) type;
}
```

### 使用场景之三：传递一个lambda的类型

```
class Person {
  ...
};

auto hash = [](const Person& p) {
  ...
};

auto eq = [](const Person& p1, Person& p2) {
  ...
};

unordered_set<Person, decltype(hash), decltype(eq)> pset(10, hash, eq);
```
