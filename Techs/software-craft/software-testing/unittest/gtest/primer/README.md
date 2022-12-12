## 入门

使用gtest来进行单元测试在测试用例的组合上从低到高依次涉及“测试用例”、“测试集”和“测试程序”。按照惯用的说法，就是一个“测试程序”里面包括一个或者多个“测试集”，而一个“测试集”包括多个“测试用例”。

“测试用例”就是最小的组织单位，它就是一个函数。在这个测试函数中会使用断言语句来判断测试是否达到了预期，断言语句可能的结果有三种：

1. 测试成功
2. 测试失败，没有crash（由`EXPECT_*`触发）
3. 测试失败，有crash（会终端当前测试函数的执行，由`ASSERT_*`触发）

可以使用`<<`给断言提供额外的打印信息：

```
ASSERT_EQ(x.size(), y.size()) << "Vectors x and y are of unequal length";

for (int i = 0; i < x.size(); ++i) {
  EXPECT_EQ(x[i], y[i]) << "Vectors x and y differ at index " << i;
}
```


## 第一个case

使用`TEST(TestSuiteName, TestName)`来定义测试用例，*需要特别说明的是这里的TestSuiteName和TestName都不能包含下划线`_`。*

```
TEST(FactorialTest, HandlesZeroInput) {
  EXPECT_EQ(Factorial(0), 1);
}
```



## 参考

- [Googletest Primer](http://google.github.io/googletest/primer.html)