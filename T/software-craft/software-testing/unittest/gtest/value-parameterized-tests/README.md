# Value-Parameterized Tests

基于值参数化测试可以通过不同的参数来测试同一块代码。要使用这种功能，需要定义一个继承自`testing::Test`和`testing::WithParamInterface<T>`的混合类。

```
class FooTest :
    public testing::TestWithParam<const char*> {
  // You can implement all the usual fixture class members here.
  // To access the test parameter, call GetParam() from class
  // TestWithParam<T>.
};

// Or, when you want to add parameters to a pre-existing fixture class:
class BaseTest : public testing::Test {
  ...
};
class BarTest : public BaseTest,
                public testing::WithParamInterface<const char*> {
  ...
};
```

之后，通过`TEST_P`宏了定义针对这个混合类的测试用例，在其中可以使用`GetParam()`来访问传入的不同参数：

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

最后，需要使用`INSTANTIATE_TEST_SUITE_P`来实例化测试集，这一步会对所有参数都实例化对应的测试:

```
INSTANTIATE_TEST_SUITE_P(InstantiationName,
                         FooTest,
                         testing::Values("meeny", "miny", "moe"));
```

参考：

- [Value-Parameterized Tests](https://github.com/google/googletest/blob/master/googletest/docs/advanced.md#value-parameterized-tests)

# 问题

`std::tr1::get`和`std::get`的区别？
