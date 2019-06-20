# class的定义

类（class）是一种抽象的数据类型，是一种设计蓝图，用来创建特定类型的对象。类在定义的时候
指定了一簇数据和函数，因此它创建出来的对象实际上也就是一组数据和操作它们的函数。类可以继
承、定制或扩展超类中已有的代码。

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

# 类的方法

类通过函数为实例提供行为，这些函数会在类中对变量名进行赋值。它们通常称为方法，而且会自动
接收第一个特殊参数（self）。

# 类的属性

就像简单变量一样，类和实例的属性并没有事先声明，而是在首次赋值时才会存在。如果类想确保变
量名一定会在实例创建时存在，那么需要在构造时填好这个属性。

## 1.私有变量

在变量前面添加两个下划线`__`将其更改为私有变量。


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

# 静态方法

使用装饰器(@staticmethod)来定义静态方法：

```
class MyClass(object):
    @staticmethod
    def the_static_method(x):
        print x

MyClass.the_static_method(2) # outputs 2
```

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

# 运算符重载

作为一名类的设计者，你可以选择使用或不使用运算符重载。你的抉择取决于有多想让对象的用法和
外观看起来更像内置类型。

Python通过重载预期的内置类型接口来实现重载。以下是重载运算符的主要概念：

- 以双下划线命名的方法（__x__）是特殊钩子。Python语言替每种运算和特殊命名的方法之间，定
义了固定不变的映射关系。
- 当实例进行内置运算时，这类方法会自动调用。比如，实例对象继承了__add__方法，那么对象出
现在+表达式内时，该方法就会调用。
- 类可覆盖多数内置类型运算。

## 1.比较大小

如果要比较两个对象值的大小，可以通过重载`__eq__`方法来实现：

```
class Staff(object):
    def __init__(self,id,name):
        self.id=id
        self.name=name        

    def __eq__(self,other):
        return self.id==other.id
```

# 对象持久化

Python的对象持久化功能通过3个标准的库模块来实现：pickle, dbm和shelve。

pickle模块是一种非常通用的对象格式化和解格式化工具：对于内存中几乎任何的Python对象，它
都能聪明地把对象转换为字节串，这个字节串可以随后用来在内存中重新构建最初的对象。pickle
模块几乎可以处理我们所能够创建的任何对象。

shelve模块提供了一个额外的层结构，允许按照键来存储pickle处理后的对象。Shelve使用pickle
把一个对象转换为其pickle化的字符串，并将其存储在一个dbm文件中的键之下，随后载入的时候，
shelve通过建获取pickle化的字符串，并用pickle在内存中重新创建最初的对象。

# 参考阅读

- (Static methods in Python?)[https://stackoverflow.com/questions/735975/static-methods-in-python]
- 《Python学习手册》
