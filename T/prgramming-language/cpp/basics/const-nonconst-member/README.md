## 为什么需要`const`和`non-const`两个版本同名的函数

因为对于const对象需要const版本的成员，比如如下代码：

```
class C {
public:
  void print()
  {
    std::cout <<c <<std::endl;
  }

  char c;
};
```

我们使用使用`C* c = new C()`创建一个non-const对象，然后调用`c->print()`没有问题。但是，如果使用`const C* c = new C()`创建了一个const对象，此时调用`c->print()`就会出现如下错误：

```
error: passing ‘const C’ as ‘this’ argument of ‘void C::print()’ discards qualifiers [-fpermissive]
   c->print();
```

另外const函数也只能被其他const成员函数调用。基于这两点很多时候它需要一个const版本的`print()`，因此修正上面的代码即可，如下：

```
class C {
public:
  void print() const
  {
    std::cout <<c <<std::endl;
  }

  char c;
};
```

在大多场景中我们在使用类的时候有些时候是需要改变它（需要non-conse对象），有些时候不需要改变它（会创建const对象），所以通常情况下我们会创建两个版本的函数：

```
const char & get() const
{
  // Some more logics.
  return c;
}

char & get()
{
  std::cout <<"in non-const." <<std::endl;
  return const_cast<char &>(static_cast<const C &>(*this).get());
}
```

两个版本的函数通常实现逻辑相同，如此会造成代码重复，特别对于该函数包含有多行的时候。因此才有了如上这种先定义const版本，再去掉const的做法。（反过来会出现递归的糟糕情况，不可行。）


参考：
- [Function overloading and const keyword](https://www.geeksforgeeks.org/function-overloading-and-const-functions/)
- [ [C++] non const getter in terms of const getter](https://www.gamedev.net/forums/topic/550112-c-non-const-getter-in-terms-of-const-getter/)
