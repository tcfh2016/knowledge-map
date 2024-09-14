## initializer list

C++11引入了统一初始化的语法，即为初始化提供通用的语法，即用`{}`来提供初始化。为了支持用户自定义类型的初始化，C++11提供了类模板`std::initializer_list<>`来完成自定义类型的初始化：

```
int x4 = {7};
std::vector<int> v1 {1, 2, 3};
```

## 为什么要这么做？

C++11之前对于变量的初始化多达四种，并且四种还拥有不少的缺陷，比如没有办法初始化数组成员，不方便初始化容器以及无法初始化动态分配的POD类型。我们先来看看C++11之前初始化的例子。

1）初始化基本类型，用`=`或者`()`。

```
int n = 1;
int n(0);
void *p = null;
char c = 'A';
```

2）初始化类成员，用`initialization list`

```
class You
{
explicit You(int n, int m) : x(n), y(m){} //mem-init
private:
 int x, y;
};
You s(0,1); //object initializers enclosed in parentheses
You s2={0,1}; //compilation error
```

3）聚合类型（POD的数组和结构体）的初始化，用`{}`

```
int arr[2]={1,2};
char sz[]="message";

struct Me
{
 int a,b;
};
Me s={0,1};
```

然后，是几组无法完成初始化的例子。

```
// 无法初始化x
class C
{
int x[100];
C();
};

// 无法初始化buffer
char *buff=new char[1024];

// 无法初始化容器，只能够从空容器开始逐步增添新元素。
vector <string> vs;
vs.push_back("alpha");
```


## C++11的统一初始化方案

C++11提供的`{}`统一初始化方案用来解决上面这些问题：

```
int a{0};
string s{"hello"};
vector <string> vs{"alpha", "beta", "gamma"};
map<string, string> stars
 {{"Superman", "+1 (212) 545-7890"},
  {"Batman", "+1 (212) 545-0987"}};
double *pd= new double [3] {0.5, 1.2, 12.99};
class C
{
  int x[4];
  double d=0;
public:
  C(): x{0,1,2,3} {}
};
```


## 构造器初始化列表（`constructor's member initialization list`/`mem-init`）和类成员初始化（`class member initializer `）

传统的初始化列表是在构造器里面初始化成员变量，C++11之后开始支持在定义的时候初始化。那究竟它们的区别在什么地方呢？

- 首先，构造器初始化列表可以通过参数来初始化成员，这是成员初始化列表缺乏的灵活性。
- 其次，如果某个类具有多个构造器，那么这个时候多个构造器均需要应用初始化列表，由此带来了重复性的工作，也增加了维护成本。此时使用成员初始化列表更合适。

*对于类里面的成员初始化列表，编译器也会将其转换为构造器初始化列表。*

参考：

- [Get to Know the New C++11 Initialization Forms](informit.com/articles/article.aspx?p=1852519)
- [Has the new C++11 member initialization feature at declaration made initialization lists obsolete?](https://stackoverflow.com/questions/24149924/has-the-new-c11-member-initialization-feature-at-declaration-made-initializati)
- [C++11 member initializer list vs in-class initializer?](https://stackoverflow.com/questions/27352021/c11-member-initializer-list-vs-in-class-initializer)
