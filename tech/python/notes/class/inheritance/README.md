# inheritance （继承）

继承（inheritance）是 OOP里的一项重要功能，它可以让新类继承已有的类。妥善使用继承可以很
好的实现代码重用。如下代码是让`Human`继承`Player`，如果你要简单打印出当前类的信息需要重
写`__repr__(self)`来更正显示信息，否则它会直接调用父类里面的这个方法。

```
class Human(Player):
  pass
```

## 1.重载方法

在继承的类中定义一个与超类中同名的属性（数据/方法）会替代超类中的属性，这种重新定义并将
取代属性的动作称为重载:

```
class Player:
  def print():
    pass

class Human(Player):
  def print():  # 重写了Player中的print()
    pass
```

## 2.调用超类的方法

类方法总是可以在一个实例中调用（Python自动把该实例发送给self参数），或者通过类来调用（
必须手动地传递实例）。

```
class Manager(Person):
  def giveRaise(self, percent, bonus=.10):
    Person.giveRaise(self, percent + bonus)
```
