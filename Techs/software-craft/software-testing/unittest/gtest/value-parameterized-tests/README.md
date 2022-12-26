## Value-Parameterized Tests

“基于参数化值的测试”指的是使用相同参数但是多组不同的值来测试同一块代码，这样可以避免你写作重复的代码来测试不同的值。

要使用这种功能，需要定义一个继承自`testing::Test`和`testing::WithParamInterface<T>`的固件类，gtest里面已经定义了这样的固件类：`testing::TestWithParam<T>`，其中的T就是参数的类型。

```
class FooTest :
    public testing::TestWithParam<T> {
  // You can implement all the usual fixture class members here.
  // To access the test parameter, call GetParam() from class
  // TestWithParam<T>.
};

```

之后，通过`TEST_P`宏来定义测试用例，这里的“P”指代“Parameterized”或者“Pattern”，其中可以使用`GetParam()`来访问传入的不同参数：

```
TEST_P(FooTest, DoesBlah) {
  // Inside a test, access the test parameter with the GetParam() method
  // of the TestWithParam<T> class:
  EXPECT_TRUE(foo.Blah(GetParam()));
  ...
}

TEST_P(FooTest, HasBlahBlah) {
  ...
}
```

最后，需要使用`INSTANTIATE_TEST_SUITE_P`来实例化测试集，这一步会对所有参数都实例化对应的测试。下面是针对T为“char *”初始化了三个不同的值"meeny", "miny", "moe"，它带来的效果是上面的两个测试用例`DoesBlah`和`HasBlahBlah`都会分别执行这三个不同的值。

```
INSTANTIATE_TEST_SUITE_P(InstantiationName,
                         FooTest,
                         testing::Values("meeny", "miny", "moe"));
```


## 添加参数

当然，有时候你需要在固件类当中添加新的参数，那么这个时候就不需要直接使用`testing::TestWithParam<T>`，而是可以直接定义：

```
// Or, when you want to add parameters to a pre-existing fixture class:
class BaseTest : public testing::Test {
  ...
};
class BarTest : public BaseTest,
                public testing::WithParamInterface<const char*> {
  ...
};
```


## 参考

- [Value-Parameterized Tests](https://github.com/google/googletest/blob/master/googletest/docs/advanced.md#value-parameterized-tests)