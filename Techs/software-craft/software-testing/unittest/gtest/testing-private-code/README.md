## 私有成员测试

基于黑盒测试原则，你通常只需要针对类的公有接口进行测试。所以，当你想要去测试类的内部实现的时候就需要考虑当前类的设计是否可以进一步提升。这种情况通常都是因为类有些过于复杂的缘故，此时应该将一些功能单独抽离到新的类，单独进行测试。

测试非公共接口之外的对象通常包括两类：

1. static函数，定义在未命名空间里面的变量
2. private/protected类成员


## 参考

- [Testing Private Code](http://google.github.io/googletest/advanced.html#testing-private-code)

