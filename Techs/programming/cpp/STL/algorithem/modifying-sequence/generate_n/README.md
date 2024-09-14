## [generate_n](https://en.cppreference.com/w/cpp/algorithm/generate_n)

函数原型为`generate_n( OutputIt first, Size count, Generator g )`（这里为了简单省略了返回值的类型，因为c++11, c++17, c++20均对返回值做了变动），该函数的作用为调用生成器g生成counter个元素然后赋值给first指向的元素。

比如下面是一种可能的实现，从中可以更加清晰的理解该函数的意图：

```
template< class OutputIt, class Size, class Generator >
OutputIt generate_n( OutputIt first, Size count, Generator g )
{
    for( Size i = 0; i < count; ++i ) {
        *first++ = g();
    }
    return first;
}
```
