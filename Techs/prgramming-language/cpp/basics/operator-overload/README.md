## 操作符重载

## Q&A

1. `explicit operator`是什么意思？

在代码里面看到一个重载，但是与常规重载不同，那到底该如何使用？

```
class T
{
public:
    explicit operator int() const { return lower; }

private:
    int lower;
    int upper;
};
```

在使用的时候必须要显示指定确定的类型，如下所示：

```
T t(100, 200);

auto a(t); // compiling error
int a(t); // ok

auto d = static_cast<long>(t); // compiling error
auto c = static_cast<int>(t); // ok
```

参考：

- [When can I use explicit operator bool without a cast?](https://stackoverflow.com/questions/39995573/when-can-i-use-explicit-operator-bool-without-a-cast)
