# 第8章 防御式编程 / Defensive Programming

防御式编程的主要思想是：子程序应该不因传入错误数据而被破坏，哪怕是由其他子程序产生的错
误数据。

## 8.1 保护程序免遭非法输入数据的破坏 / Protecting Your Program from Invalid Inputs

- 用使用迭代设计、编码前先写伪码、写代码前先写测试用例、低层设计检查等活动，都有助于防止
引入错误。

## 8.2 断言 / Assert

- 用错误处理代码来处理预期会发生的状况，用断言来处理绝不应该发生的状况。错误处理通常用来
检查有害的输入数据，而断言是用于检查代码中的bug。

## 8.4 异常 / Exceptions

- 了解所用函数库可能抛出的异常。未能捕获由函数库抛出的异常将会导致程序崩溃，就如同未能捕
获未能由自己代码抛出的异常一样。
- 自始自终考虑各种各样的错误处理机制：在局部处理错误、使用错误码来传递错误、在日志文件中
记录调试信息、关闭系统或其他的一些方式。仅仅因为编程语言提供了异常处理机制而使用异常，是
典型的“为用而用”。
