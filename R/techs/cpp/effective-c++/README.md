## 条款32：确定你的public继承塑模出is-a关系

- public inheritance意味着“is-a”的关系。适用于base classes的每一件事情一定也适用于derived classes。
  - 如果`class D`以public形式继承`class B`那么每一个类型为D的对象同时也是一个类型为B的对象。
  - Liskov Substitution Principle（里氏替换原则） ：B对象可派上用场的地方，D对象一样可以派上用场。
  - 编译器在必要时刻（为了让函数调用成功）将derived class对象暗自转换为base class对象。

## 条款33：避免遮掩继承而来的名称

- 当编译器处于函数的作用域并遭遇名称`x`时，它在local作用域内查找是否有什么东西带有这个名称。如果找不到就再找其他作用域。
  - 》 someFunc内的`double x`可以遮掩global作用域内的`int x`。
- 继承时，drived class作用域嵌套在base class作用域内，位于drived class作用域内的名称`x`的查找顺序为：
  - 查找local作用域。
  - 查找drived class作用域。
  - 查找base class作用域。
  - 查找base class所在的namespace作用域。
  - 查找global作用域。
  - 》 Drived 内的函数`fm()`可以遮掩Base 内的`fm(int)`，尽管参数类型不同。
  - 》 解决方法是在Drived内使用 `using`声明那些可能被遮掩的名称。
  - 》 或者使用forwarding functions。

## 条款34：区分接口继承和实现继承

- 成员函数的接口总是会被继承。public继承意味着`is-a`，所以对base class为真的任何事情一定也对其derived classes为真。因此如果某个函数可施行于某class身上，一定也可施行于其derived classes身上。
- 声明一个pure virtual函数的目的是为了让derived classes只继承函数接口。
  - 包含pure virtual函数的base class无法为函数提供合理的缺省实现。它提醒derived classes设计者“必须提供函数实现。”
- 声明一个impure virtual函数的目的，是让derived classes继承该函数的接口和缺省实现。
  - base class提供该函数的缺省行为，它告诉derived class设计者“你必须支持这个函数，如果你不想自己写一个，可以使用base class中的默认版本。”
  - 如果某个derived class过于轻率的使用这种方式，可能造成危险（本身行为与默认行为违背）。
- 声明non-virtual函数的目的是为了令derived classes继承函数的接口及一份强制性实现。
  - 任何derived class都不应该尝试改变其行为，所以它绝不该在derived class中被重新定义。

## 条款39：明智而审慎地使用private继承

- 如果class之间的继承关系是private，编译器不会自动将一个derived class对象转换为一个base class对象。
- 由private base class继承而来的所有成员，在derived class中都会变成private属性，纵使它们在base class中是protected或public属性。
- private继承意味着 implementated-in-terms-of（根据某物实现出），只有实现部分被继承，接口部分应略去。如果D以private形式继承B，意思是D对象根据B对象实现而得，再没有其他涵义了。
- 复合和private继承都意味 is-implemented-in-terms-of，但复合比较容易理解，所以无论什么时候，只要可以应该选择复合。
- 当你面对“并不存在is-a关系”的两个classes，其中一个需要访问另一个protected成员，或需要重新定义其一或多个virtual函数，private继承极有可能成为正统涉及策略。
