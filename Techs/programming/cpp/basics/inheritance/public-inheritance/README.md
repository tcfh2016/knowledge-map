2017年10月19日07:58:24
使用public继承实现“is-a”的关系并不是看起来那么简单，如下以一个实例来讨论public继承时可
能遇到的问题以及解决办法。

《Effective C++》条款32 中有一个很好的例子可以应用在这里：“企鹅是一种鸟”，很显然这里确
实复合“is-a”的设计模型，于是让“企鹅”类以public继承“鸟”类看起来没有问题：

```
class Bird
{
public:
  virtual void fly();
  // ...
};

class Penguin : public Bird
{
  // ...
};
```

但是我们忘记了，企鹅本身并不会飞，这是在采用继承设计时可能碰到的问题：现实语义与软件建模
的不同。怎么解决？下面是三种不同的方式。

- 方式一：重新设计继承体系

怎么解决？既然在鸟里面还区分为“会飞的鸟”和“不会飞的鸟”，那么可以将Bird再细分：

```
class Bird
{
public:  
  // ...
};

class FlyingBird : public Bird
{
public:
  virtual void fly();
  // ...
};

class Penguin : public Bird
{
  // ...
};
```

在软件开发中，我们大多时间不会遇到如此刁钻喜人的问题，也就不需要一开始将继承体系细分细致
非凡，一切根据需求进行定夺。

- 方式二：派生类中裁剪

派生类中可以重写基类的成员方法，所以另一种方式是让派生类中的方法“什么也不做”：

```
class Bird
{
public:
  virtual void fly();
  // ...
};

class Penguin : public Bird
{
  void fly() {}
  // ...
};
```

这样做的不足之处在《HEAD FIRST》中提到过：派生类与基类的强耦合，当基类当中增添另外一个
类似的成员方法时，派生类必须为之进行适配；或者，当整个继承体系中增添了一个类似的派生类
时同样需要覆盖fly()方法。

- 方式三：使用策略模式

策略模式的定义如下：

  策略模式定义了算法族，分别封装起来，让它们之间可以互相替换，此模式让算法的变化独立于使
  用算法的客户。

相对于继承，策略模式使用组合的方式，将一些父类当中“容易随着需求改变而变化的部分”独立出来
再组合到子类中去，如此使得需求变更局限在这部分独立出来的类，屏蔽了对原有继承体系的影响。

```
// 原有继承体系。
class Bird
{
public:
  FlyBehavior *flyBehavior;
  // ...
};

class Penguin : public Bird
{
  Penguin()
  {
    flyBehavior = new FlyNoWay();
  }
  // ...
};

// 独立而出算法簇，其中变化部分，即fly()不同的实现不再耦合于原有继承体系。
class FlyBehavior
{
  virtual void fly() = 0;
}

class FlyWithWings : public FlyBehavior
{
  void fly ()
  {
    // ...
  }
}

class FlyNoWay : public FlyBehavior
{
  void fly () {}
}

```

可见，第三种方式代码量看起来最多，但它可以更换来更整洁的代码，以及具有弹性整体架构，这对
于后期的维护，以及需求变更有不小的助益。

其他问题：
- public继承与private继承的意义？
