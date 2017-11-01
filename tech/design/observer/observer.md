
2017年10月23日16:35:07

## 观察者模式雏形——一个双向耦合版本

先仿照示例写了一个交叉引用的观察者原型（`参考coupled_version.cpp`)，却碰到交叉引用造就的编译问题：

```
[lianbche@hzlinb17 observer]$ g++ coupled_version.cpp -o coupled_version
coupled_version.cpp:24: error: field ‘_secretary’ has incomplete type
coupled_version.cpp: In constructor ‘StockObserver::StockObserver(std::string, Secretary)’:
coupled_version.cpp:10: error: ‘secretary’ has incomplete type
coupled_version.cpp:5: error: forward declaration of ‘struct Secretary’
coupled_version.cpp:13: error: ‘_secretary’ was not declared in this scope
coupled_version.cpp: In member function ‘void StockObserver::update()’:
coupled_version.cpp:19: error: ‘_secretary’ was not declared in this scope
[lianbche@hzlinb17 observer]$
```

尝试着使用前置声明来解决该问题，但没有办法办到：因为每个类的成员方法中均相互调用它所交叉
引用的类，这是前置声明无法办到的事。而弥补的方法在于将前一个版本分离（`参考forward_declaration_version`）。
*注：前向声明的作用类型是不完全类型，它只能以有限方式使用：① 不能定义该类型的对象，仅用于
定义指向该类型的指针及引用；②用于声明(而不是定义)使用该类型作为形参类型或返回类型的函数。*

新的一个版本的代码在耦合关系上依然是双向耦合，只不过这个解决了第一个版本的编译问题，可以
正常的编译、执行。

## 解耦实践

耦合引起的最主要问题是对于变化的不友好，牵一发而动全身。所以我们首先尝试使用依赖倒置，让
依赖对象基于抽象来解决。

当前考虑将“`Secretary`对于`StockObserver`的依赖”更新为“`Secretary`对于`StockObserver
抽象`的依赖。如此，对于之后的`StockObserver`还是`NbaObserver`,或者其他类型的observer，
`Secretary`都不需要进行其他的修改。（`参考decouple_version`）

调试代码的过程中遇到一个问题：如何在派生类中访问基类的私有数据成员？找寻答案以及自己调试
过程中两个基本结论：

- 使用域运算符::来访问基类的成员仅限定于public成员，对于private成员无帮助。
- 可以将`private`数据成员修改为`protected`以便在派生类中访问。
- 在积累中提供访问`private`数据成员的public方法，并在派生类中调用。

https://www.quora.com/How-do-I-access-private-members-of-a-base-class
>You can't. Private means it can't be accessed outside of that class, including in subclasses. Only protected or public members can be accessed in a subclass. Or you can add a public (or protected) method to return the member, like you suggested.


让具体的观察者在得到通知事件之后可以完成多样化的工作。


讨论C++前向声明的一个问答：
https://www.zhihu.com/question/63201378
