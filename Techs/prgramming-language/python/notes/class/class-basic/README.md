## class的定义

类（class）是一种抽象的数据类型，是一种设计蓝图，用来创建特定类型的对象。类在定义的时候指定了一簇数据和函数，因此它创建出来的对象实际上也就是一组数据和操作它们的函数。类可以继承、定制或扩展超类中已有的代码。

概括地讲，类就是一些函数的包，这些函数大量使用并处理内置对象类型。不过，类的设计是为了创建和管理新的对象，并且也支持继承（这是一种代码定制和复用机制）。

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
- `__str__`  用于生成对象的字符串表示的特殊方法。这个方法是在我们需要将对象输出字符串形式的时候被调用，比如使用`str(p)`。
- 在类中定义的函数称为方法，方法的第一个参数必须是 self, self使得类中的函数能够明确地引用对象对象的数据和函数。


## 类的属性

就像简单变量一样，类和实例的属性并没有事先声明，而是在首次赋值时才会存在。如果类想确保变量名一定会在实例创建时存在，那么需要在构造时填好这个属性。

在变量前面添加两个下划线`__`将其更改为私有变量。


## 类的方法

类通过函数为实例提供行为，这些函数会在类中对变量名进行赋值。它们通常称为方法，而且会自动接收第一个特殊参数（self）。

### 1.设置和取值函数

如下的设置/取值函数支持：

- 使用`p.age`来获得成员`_age`的值，不使用特性装饰器我们需要执行`p.age()`来获取。使用`@property`修饰器可以让访问方法让访问属性那样简单。
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

### 2.类方法

使用装饰器（@classmethod）可以定义类方法，这样的方法可以使用类和对象来调用：

```
class C(object):  
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
```

另一种方法是对定义的函数进行转换：

```    
    def fun(cls, arg1, arg2, ...):
       ....
    fun = classmethod(fun)
```

### 3.静态方法

使用装饰器(@staticmethod)来定义静态方法：

```
class MyClass(object):
    # 方式一
    @staticmethod
    def the_static_method(x):
        print x

    # 方式二
    def the_static_method2(x):
        print x
    the_static_method2 = staticmethod(the_static_method2)

MyClass.the_static_method(2) # outputs 2
```

## 运算符重载

作为一名类的设计者，你可以选择使用或不使用运算符重载。你的抉择取决于有多想让对象的用法和外观看起来更像内置类型。

Python通过重载预期的内置类型接口来实现重载。以下是重载运算符的主要概念：

- 以双下划线命名的方法（__x__）是特殊钩子。Python语言替每种运算和特殊命名的方法之间，定义了固定不变的映射关系。
- 当实例进行内置运算时，这类方法会自动调用。比如，实例对象继承了__add__方法，那么对象出现在+表达式内时，该方法就会调用。
- 类可覆盖多数内置类型运算。


如果要比较两个对象值的大小，可以通过重载`__eq__`方法来实现：

```
class Staff(object):
    def __init__(self,id,name):
        self.id=id
        self.name=name        

    def __eq__(self,other):
        return self.id==other.id
```
