# Typed Tests

如果对于某个接口/函数具有多重实现，此时测试你需要对不同的类型进行相同步骤的验证，一种方法是使用`TEST`/`TEST_F`为每种类型都定义测试用例，如果要多n种类型测试m个用例，那么你必须要写n*m次用例的定义。

`Typed Test`可以对多种类型重复相同的测试逻辑，你仅仅需要写作一次测试过程：

```
template <typename T>
class FooTest : public ::testing::Test {
 public:
  ...
  typedef std::list<T> List;
  static T shared_;
  T value_;
};
```

下一步，使用`TYPED_TEST_SUITE`来声明对多个类型的测试集：

```
using MyTypes = ::testing::Types<char, int, unsigned int>;
TYPED_TEST_SUITE(FooTest, MyTypes);
```

*注：之前是使用`TYPED_TEST_CASE`，现在更新为`TYPED_TEST_SUITE`。*

最后，使用`TYPED_TEST`(不再是`TEST_F()`)来定义测试用例：

```
TYPED_TEST(FooTest, DoesBlah) {
  // Inside a test, refer to the special name TypeParam to get the type
  // parameter.  Since we are inside a derived class template, C++ requires
  // us to visit the members of FooTest via 'this'.
  TypeParam n = this->value_;

  // To visit static members of the fixture, add the 'TestFixture::'
  // prefix.
  n += TestFixture::shared_;

  // To refer to typedefs in the fixture, add the 'typename TestFixture::'
  // prefix.  The 'typename' is required to satisfy the compiler.
  typename TestFixture::List values;

  values.push_back(n);
  ...
}

TYPED_TEST(FooTest, HasPropertyA) { ... }
```

参考：

- [Typed Tests](https://github.com/google/googletest/blob/master/googletest/docs/advanced.md#typed-tests)
- [TYPED_TEST_CASE is deprecated, please use TYPED_TEST_SUITE](https://github.com/vdksoft/signals/issues/6)

# Type-Parameterized Tests

类型参数化测试类似于类型测试，但它不需要你事先指定要测试的多种类型（像前面的`TYPED_TEST_SUITE(FooTest, MyTypes)`语句），而是在之后实例化。



延伸阅读：

- [Google Test(GTest)使用方法和源码解析——模板类测试技术分析和应用](https://cloud.tencent.com/developer/article/1383728)
