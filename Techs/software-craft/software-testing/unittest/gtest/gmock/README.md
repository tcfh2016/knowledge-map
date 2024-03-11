## [gMock Cookbook](http://google.github.io/googletest/gmock_cook_book.html)


## Mock Classes

Mock类的作用就是用来打桩的，也就是说如果你当前在测试类A，该类依赖于类B，那么你通常需要给类B创建对应的Mock类，来更好的测试类A。

创建Mock类和普通类一样，在定义该类的成员方法时需要使用宏`MOCK_METHOD`来产生对应的Mock方法。

```
class MyMock {
 public:
  MOCK_METHOD(ReturnType, MethodName, (Args...));
  MOCK_METHOD(ReturnType, MethodName, (Args...), (Specs...));
};
```

`MOCK_METHOD`是在2018年新引入的宏，在这之前使用的是`MOCK_METHODn`系列宏。这个系列有专门针对`const`方法，类模板等等不同的宏，比如`MOCK_CONST_METHOD1`, `MOCK_METHOD1_T`, `MOCK_CONST_METHOD1_T`, `MOCK_METHOD1_WITH_CALLTYPE`等等，但新的宏`MOCK_METHOD`可以满足所有这些需求。


## EXPECT_CALL

`EXPECT_CALL`是一种预期被调用到的声明，如果你已经定义了mock函数，但是没有为它声明被调用到的预期，一旦该mock函数被调用那么就成了“uninteresting call”。

比如，下面的代码会打印出“Uninteresting mock function call - returning default value”的信息：

```
class MyClass{
public:
virtual int retValue() { return 100; }
virtual ~MyClass(){}
};

class MockMyClass : public MyClass
{
public:
MOCK_METHOD0( retValue, int() );
};

TEST(TestForMyClass, TestRetVal)
{
MockMyClass obj3;
EXPECT_EQ(obj3.retValue(), 100); // 调用mock过的函数
}
```

要修正这个打印，那么需要添加expectation设置：

```
TEST(TestForMyClass, TestRetVal)
{
  MockMyClass obj3;
  EXPECT_CALL(obj3, retValue()).WillOnce(Return(100)); // 设定expectation
  EXPECT_EQ(obj3.retValue(), 3);
}
```

如果想屏蔽这些警告信息，可以使用`NiceMock<MockFoo>`，而如果使用`StrictMock<MockFoo>`那么任何“uninteresting call”会导致用例失败。


参考：

- [I got a warning “Uninteresting function call encountered - default action taken..” Should I panic?](https://cuhkszlib-xiaoxing.readthedocs.io/en/master/external/gtest/googlemock/docs/v1_6/FrequentlyAskedQuestions.html?highlight=google#i-got-a-warning-uninteresting-function-call-encountered-default-action-taken-should-i-panic)
- [Gmock test fails(should pass?)](https://github.com/google/googlemock/issues/209)
