## 1 背景

这篇笔记是根据StackOverflow上面的[一个问题](http://stackoverflow.com/questions/28002/regular-cast-vs-static-cast-vs-dynamic-cast/1255015#1255015)整理而成，主要针对C++中四种类型转换操作进行举例说明。

C++中新引入`static_cast`, `dynamic_cast`, `reinterpret_cast`，和`const_cast`四种新的类型转换操作符。相较于它们，不少程序员更乐于去使用C-like的类型转换，因为它强大且编写起来又简单。C-Like类型转换操作的语法有如下的两种形式：

- (new-type) expression
- new-type (expression)

通常说来，C-Like类型转换操作符可以完全替用`static_cast`和`reinterpret_cast`，那另外两种类型又有什么不同呢？一起来看看。

## 2 static_cast vs dynamic_cast

之所以把`static_cast`与`dynamic_cast`两兄弟放在一起是因为它们两者对比起来更容易记得住。首先，从名称上面它们就有语义相对的关系，一“静”一“动”。另外，在功能上面也在一定程度上体现了这一对比的特性，如dynamic_cast的Run-time Checking，static_cast在编译时增加的类型检测。简单而言：

- static_cast： 1）完成基础数据类型，2）同一个继承体系中类型的转换
- dynamic_cast：使用多态的场景，增加了一层对真实调用对象类型的检查

### 2.1 从C-Like到static_cast

`static_cast`对于基础类型如`int`, `float`, `char`以及基础类型对应指针的处理大多情况下
恰如C-Like的转换一样，不过`static_cast`会来得更加安全。

```
char c = 10;           // 1 个字节
int *p = (int *)&c;    // 4 个字节（32bit platform）

*p = 5;                // 内存踩脏
int *q = static_cast<int *>(&c); // 使用static_cast可在编译阶段将该错误检查出来。
```

对于自定义类型的处理，相比C-Like而言，它也多了一层保护，也就是它不支持在不属于同一继承体系的类型之间进行转换。但是C-Like就可以办到，看下面这个例子：

```
#include <iostream>

class A
{
public:
  A(){}
  ~A(){}

private:
  int i, j;
};

class C
{
public:
  C(){}
  ~C(){}

  void printC()
  {
    std::cout <<"call printC() in class C" <<std::endl;
  }
private:
  char c1, c2;
};

int main()
{  
  A *ptrA = new A;
  //C *ptrC = static_cast<C *>(ptrA);
  // 编译无法通过，提示：
  // In function ‘int main()’:
  // error: invalid static_cast from type ‘A*’ to type ‘C*’

  C *ptrC = (C *)(ptrA);
  ptrC->printC();
  // 编译正常通过。
  // 尽管这个时候能够正常调用printC，但实际上这种做法的结果是“undefined”
  // 尝试过，如果添加一些数据成员的运算，这个时候将会使得运算结果无法预测
  // 所以，在运行时候该逻辑相关的行为是不清晰的。

  return 0;
}  

```

### 2.2 static_cast对于自定义类型的转换

上面这个小例子简单对比了`static_cast`与 C-Like在针对不同继承体系的类之间表现的差异性，现在先把范围缩小到同一继承体系当中的类型转换。（注：这里所说的类型一般是针对类的指针或者类的引用）

`static_cast`针对同一继承体系的类之间的转换，它既可以进行upcast也可以进行downcast。一般来说，在进行upcast时是没有问题的，毕竟子类当中一定包含有父类的相关操作集合，所以通过转换之后的指针或者引用来操作对应的对象，其行为上是可以保证没问题。这和使用`static_cast`与使用C-Like或者直接隐式转换效果一样（当然，其结果是否符合程序员本身的预期与当时的设计有关系）。

需要注意的是，使用`static_cast`进行 downcast应该避免，因为它可以顺利逃过编译器的法眼，但在运行时却会爆发未定义的问题：

```
#include <iostream>

class A
{
public:
  A():i(1), j(1){}
  ~A(){}

  void printA()
  {
    std::cout <<"call printA() in class A" <<std::endl;
  }

  void printSum()
  {
    std::cout <<"sum = " <<i+j <<std::endl;
  }

private:
  int i, j;
};

class B : public A
{
public:
  B():a(2), b(2) {}
  ~B(){}

  void printB()
  {
    std::cout <<"call printB() in class B" <<std::endl;
  }

  void printSum()
  {
    std::cout <<"sum = " <<a+b <<std::endl;
  }

  void Add()
  {
    a++;
    b++;
  }

private:
  double a, b;
};

int main()
{
  B *ptrB = new B;
  ptrB->printSum();
  //打印结果：sum = 4
  A *ptrA = static_cast<A *>(ptrB);
  ptrA->printA();
  ptrA->printSum();
  //打印结果：sum = 2
  //在进行upcast的时候，指针指向的对象的行为与指针的类型相关。

  ptrA = new A;
  ptrA->printSum();
  //打印结果：sum = 2  
  ptrB = static_cast<B *>(ptrA);
  ptrB->printB();
  ptrB->printSum();  
  //打印结果：sum = 0
  //在进行downcast的时候，其行为是“undefined”。

  //B b;
  //B &rB = b;
  //rB.printSum();
  //打印结果：sum = 4
  //A &rA = static_cast<A &>(rB);   
  //rA.printA();
  //rA.printSum();
  //打印结果：sum = 2
  //在进行upcast的时候，引用指向的对象的行为与引用的类型相关。

  //A a;
  //A &rA = a;
  //rA.printSum();
  //打印结果：sum = 4
  //B &rB = static_cast<B &>(rA);   
  //rB.printB();
  //rB.printSum();
  //打印结果：sum = 5.18629e-317  
  //在进行downcast的时候，其行为是“undefined”。

  return 0;
}
```

如上，`static_cast`在对同一继承体系的类之间进行downcast时的表现，与C-Like针对分属不同继承体系的类之间进行转换时的表现一样，将是未定义的。所以，应该尽可能避免使用`static_cast`执行downcast转换，更准确的说，应该尽可能避免对集成体系的类对应的指针或者引用进行downcast转换。

既然这样，那是不是在软件开发过程当中就不会存在 downcast的这种情况了呢？实际上不是的。一般来说，进行downcast的时候一般是在虚继承的场景当中，这个时候dynamic_cast就上场了。

### 2.3 dynamic_cast

`dynamic_cast`的使用主要在downcast的场景，它的使用需要满足两个条件：

- downcast时转换的类之间存在着“虚继承”的关系
- 转换之后的类型与其指向的实际类型要相符合

`dynamic_cast`对于upcast与`static_cast`的效果是一样的，然而因为`dynamic_cast`依赖于RTTI，所以在性能上面相比`static_cast`略低。

```
#include <iostream>
#include <exception>

class A
{
public:
  virtual void print()  
  {
    std::cout <<"Welcome to WorldA!" <<std::endl;
  }
};

class B : public A
{
public:
  B():a(0), b(0) {}
  ~B(){}
  virtual void print()  
  {
    std::cout <<"Welcome to WorldB!" <<std::endl;
  }
private:
  double a, b;
};

int main()
{
  B *ptrB = new B;
  A *ptrA = dynamic_cast<A *>(ptrB);
  ptrA->print();
  //在虚继承当中，针对指针执行upcast时dynamic_cast转换的效果与static_cast一样
  //对是否存在virtual没有要求，会实际调用所指向对象的成员。

  //A *ptrA = new A;
  //B *ptrB = dynamic_cast<B *>(ptrA);
  //ptrB->print();
  //Segmentation fault，针对指针执行downcast时转换不成功，返回NULL。

  //A a;
  //A &ra = a;
  //B &b = dynamic_cast<B &>(ra);
  //b.print();    
  //抛出St8bad_cast异常，针对引用执行downcast时转换不成功，抛出异常。

  //ptrA = new A;
  //ptrB = static_cast<B *>(ptrA);
  //ptrB->print();
  //使用static_cast进行downcast的时候，与dynamic_cast返回NULL不同，
  //这里会调用ptrB实际指向的对象的虚函数。

  //ptrA = new A;
  //ptrB = dynamic_cast<B *>(ptrA);
  //ptrB->print();
  //在进行downcast时，如果没有virtual成员，那么在编译时会提示：  
  // In function ‘int main()’:
  // cannot dynamic_cast ‘ptrA’ (of type ‘class A*’) to type ‘class B*’ (source type is not polymorphic)

  return 0;
}
```

从这个例子可以看出，在虚继承场景下，能够使用`dynamic_cast`的地方一定可以使用`static_cast`，然而dynamic_cast却有着更严格的要求，以便帮助程序员编写出更加严谨的代码。只不过，它在性能上面多了一部分开销。

## 3 reinterpret_cast

`reinterpret_cast`是最危险的一种cast，之所以说它最危险，是因为它的表现和C-Like一般强大，稍微不注意就会出现错误。它一般在一些low-level的转换或者位操作当中运用。

```
#include <iostream>

class A
{
public:
  A(){}
  ~A(){}
  void print()  
  {
    std::cout <<"Hello World!" <<std::endl;
  }
};

class B
{
public:
  B():a(0), b(0) {}
  ~B(){}

  void call()
  {
    std::cout <<"Happy for your call!" <<std::endl;
  }

private:
  double a, b;
};

int main()
{
  //A *ptrA = new A;
  //B *ptrB = reinterpret_cast<B *>(ptrA);
  //ptrB->call();
  //正常编译
  //A *ptrA = new A;
  //B *ptrB = (B *)(ptrA);
  //ptrB->call();
  //正常编译
  //A *ptrA = new A;  
  //B *ptrB = static_cast<B *>(ptrA);
  //ptrB->call();
  //编译不通过，提示：
  //In function ‘int main()’:
  //error: invalid static_cast from type ‘A*’ to type ‘B*’

  //char c;
  //char *pC = &c;
  //int *pInt = static_cast<int *>(pC);
  //编译提示错误：error: invalid static_cast from type ‘char*’ to type ‘int*’
  //int *pInt = reinterpret_cast<int *>(pC);
  //正常编译。
  //int *pInt = (int *)(pC);
  //正常编译。

  return 0;
}

```

分析了`static_cast`，`dynamic_cast`与`reinterpret_cast`之后就可以画出如下的图示对它
们之间的区别进行简单比较了。这里没有将`const_cast`纳入进来是因为它比较特殊，另外分节对
它进行介绍。

              ----------------
             /   dynamic_cast \ -->同一继承体系（virtual）的类指针或引用[更安全的downcast]
            ~~~~~~~~~~~~~~~~~~~~    
           /     static_cast    \ -->基础类型[更安全]，同一继承体系的类指针或引用
          ~~~~~~~~~~~~~~~~~~~~~~~~
         /    reinterpret_cast    \ -->与C-Like的作用一致，没有任何静态或者动态的checking机制
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       /          C-Like            \ -->基础类型，同一继承体系的类指针或引用,不同继承体系类的指针或引用
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## 4 const_cast

`const_cast`能够使用来移出或者增加一个变量的const属性，最初的时候我觉得这个`const_cast`
比较怪异，C里面一直都没有类似的东西来消除`const`属性，这里是否会多余呢？其实，我这种想法
本身就没根没据。后来想想，在C++当中一直提倡将变量声明为`const`，这样一旦变量变得多了起来，
在与其他软件组件或者第三方库进行衔接的时候就难免会碰到需要cast const属性的问题。比如：

```
const int myConst = 15;
int *nonConst = const_cast<int *>(&myConst);

void print(int *p)
{
    std::cout << *p;
}

print(&myConst); // 编译错误：error: invalid conversion from ‘const int*’ to ‘int*’
print(nonConst); // 正常

```

不过，在使用`const_cast`的时候应该要注意，如果没有必要尽量不要去修改它的值：

```
const int myConst = 15;
int *nonConst = const_cast<int *>(&myConst);

*nonConst = 10;
// 如果该变量存放在read-only内存区当中，在运行时可能会出现错误。
```

## 5 小结

在`C++`当中对于大部分数据类型而言，使用C-Like的类型转换已经完全够用了。然而，不少人一直在倡导进行显式数据类型转换的时候尽可能地使用`C++`规定的类型转换操作。我想这里面大概有两方面的原因：

- 第一种，`C++`是一门“新”的编程语言，应该学会用它本身的思想来解决编程方面的问题；
- 第二种，尽管C-Like转换操作能力强大，但如果将其任意使用，会产生不少在编译期间隐藏，却在运行时候神出鬼没。这些问题使得软件的行为极不清晰。

如此，C++ 当中引出了其他四种类型转换方式，用来更加安全的完成一些场合的类型转换操作。比如使用 `reinterpret_cast`的时候会表示你确定无疑的想使用 C-Like的类型转换；在使用 `static_cast`的时候想要确保转换的对象基本兼容，比如无法将`char *`转换为`int *`，无法在不同继承体系类的指针或引用之间进行转换；而使用`dynamic_cast`的时候是要对虚继承下的类执行downcast转换，并且已经明了当前性能已经不是主要的影响因素...

回答一下前文提到的问题。可以这么说，对于`const_cast`, `static_cast`, `reinterpret_cast`和`dynamic_cast`所能够完成的所有转换，C-Like也可以完成。但是，C-Like转换却没有`static_cast`, `dynamic_cast`分别提供的编译时类型检测和运行时类型检测。

`C++`之父Bjarne Stroustrup博士在[这里](http://www.stroustrup.com/bs_faq2.html#static-cast)也谈到了他的观点，主要有两点：其一，C-Like的 cast极具破坏性并且在代码文本上也难得花不少力
气搜索到它；其二，新式的cast使得程序员更有目的使用它们并且让编译器能够发现更多的错误；其
三，新的cast符合模板声明规范，可以让程序员编写它们自己的cast。

## 参考

- [这里](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Programming_Languages/C%2B%2B/Code/Statements/Variables/Type_Casting)
- [这里](http://www.cplusplus.com/doc/tutorial/typecasting/)
- [这里](http://www.icce.rug.nl/documents/cplusplus/cplusplus03.html#an241)
- [这里](https://msdn.microsoft.com/en-us/library/c36yw7x9%28VS.80%29.aspx)
