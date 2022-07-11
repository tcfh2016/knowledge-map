# -*- coding: utf-8 -*-

class Person(object):
    # __intit__ 函数是用于初始化对象值的标准函数，它在创建Person对象时自动创建。
    def __init__(self, name='', age=0):
        self.__name = name
        self.__age = age

    # 在类中定义的函数称为方法，方法的第一个参数必须是self。
    # Python 自动给每个对象添加特殊变量 self，这个变量指向对象本身，让类中的函数能够明
    # 确地引用对象的数据和函数。

    def display(self):
        print (str(self))

    # 用于生成对象的字符串表示的特殊方法。这个方法是在我们需要将对象输出字符串形式的时候
    # 被调用，就像如下链接里面解释的：
    # __str__ is only called when a string representation is required of an object.
    # For example str(uno), print "%s" % uno or print uno
    #https://stackoverflow.com/questions/12448175/confused-about-str-in-python
    def __str__(self):
        return ("Person('%s', %d)" % (self.__name, self.__age))

    #通过特性装饰器设置设置、取值函数之后，可以通过直接访问变量的形式来进行设置、取值操
    #作。

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        print "set age to %d" % age,

        if 0 < age <=150:
            self.__age = age
            print ("success.")
        else:
            print ("did not work.")

    def get(self):
        return self.__age

def main():
    p     = Person('lianbche', 30)
    print (p.age)
    p.age = 28
    print (p.age)

    p.age = 0
    print (p.age)

main()
