## [gtest](http://google.github.io/googletest/)


## 常见问题

测试特定的值：

```
EXPECT_CALL(
        *ptr,
        function(::testing::An<msg&>(), 20));
```

