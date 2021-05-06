## 操作符重载

## Q&A

1. `explicit operator`是什么意思？

在代码里面看到一个重载，但是与常规重载不同，那到底该如何使用？

```
struct T {
    explicit operator bool() const { return true; }
};
```

参考：

- [When can I use explicit operator bool without a cast?](https://stackoverflow.com/questions/39995573/when-can-i-use-explicit-operator-bool-without-a-cast)
