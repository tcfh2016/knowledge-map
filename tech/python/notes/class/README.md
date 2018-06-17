
# class的定义

类（class）是一种抽象的数据类型，是一种设计蓝图，用来创建特定类型的对象。类在定义的时候
指定了一簇数据和函数，因此它创建出来的对象实际上也就是一组数据和操作它们的函数。

```
class Person(object):    
    def __init__(self, name='', age=0):
        self._name = name
        self._age = age    

    def display(self):
        print (str(self))

    def __str__(self):
        return ("Person('%s', %d)" % (self.__name, self.__age))

```

- `__init__` 函数是用于初始化对象值的标准函数，它在创建Person对象时自动创建。
- `__str__`  用于生成对象的字符串表示的特殊方法。这个方法是在我们需要将对象输出字符串形式
的时候被调用，比如使用`str(p)`。
- 在类中定义的函数称为方法，方法的第一个参数必须是 self, self使得类中的函数能够明确地引
用对象对象的数据和函数。

# 设置和取值函数

如下的设置/取值函数支持：

- 使用`p.age`来获得成员`_age`的值，不使用特性装饰器我们需要执行`p.age()`来获取。
- 使用`p.age = 55`来修改`_age`的值，不使用特性装饰器我们需要执行类似 `p.setage()`的调
用。

```
@property
def age(self):
    return self._age

@age.setter
def age(self, age):
    print "set age to %d" % age,

    if 0 < age <=150:
        self._age = age
        print ("success.")
    else:
        print ("did not work.")
```

# 私有变量

在变量前面添加两个下划线`__`将其更改为私有变量。

# inheritance （继承）

继承（inheritance）是 OOP里的一项重要功能，它可以让新类继承已有的类。妥善使用继承可以很
好的实现代码重用。如下代码是让`Human`继承`Player`，如果你要简单打印出当前类的信息需要重
写`__repr__(self)`来更正显示信息，否则它会直接调用父类里面的这个方法。

```
class Human(Player):
  pass
```

# polymorphism （多态）

python里面的多态比较简单，它会直接根据当前实际的对象去调用对应的方法，比如：

```
class Player(object):
  pass

class Human(Player):
  def play(self):
    print "Human plays."

class Computer(Player):
  def play(self):
    print "Computer plays."

map(lambda x:x.play(), [Human(), Computer()])
```
