# gtest


## 常见问题

### 1."Uninteresting mock function call"错误

据网络上查找到的资料，这个信息的出现是因为“你已经定义了mock函数”，但是没有“为它指定expectation”所以在调用到这个mock函数的时候就进行默认处理，但是这个信息会打印出来。

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


参考：

- [I got a warning “Uninteresting function call encountered - default action taken..” Should I panic?](https://cuhkszlib-xiaoxing.readthedocs.io/en/master/external/gtest/googlemock/docs/v1_6/FrequentlyAskedQuestions.html?highlight=google#i-got-a-warning-uninteresting-function-call-encountered-default-action-taken-should-i-panic)
- [Gmock test fails(should pass?)](https://github.com/google/googlemock/issues/209)
