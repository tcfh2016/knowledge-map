## 条件包含预处理宏

常见的条件包含预处理宏有`#if`, `#ifdef`, `#ifndef`, `#else`, `#elif`, `#endif`，最基本的表达式为。它们各自的语法如下：

- #if: `#if constant-expression newline`
- #ifdef: `#ifdef identifier newline`
- #ifndef: `#ifndef identifier newline`
- #else: `#else newline`
- #elif: `#elif constant-expression newline`
- #endif: `#endif newline`

我们使用#define好的宏来的时候会看到如下用法：

```
#ifdef DEBUG
...
#else
...
#endif
```

但恰如上面介绍的用法，实际上这些条件宏并不一定针对定义的宏，也支持常量表达式：

```
#if true  
.          
#elif true
.          
#endif     
```

那如果我们要对条件宏使用条件表达式呢，这个时候就需要用到`defined运算符`，它用来判断宏是否已经定义。有了它我们就可以简化一些表达：*注：不能使用`#ifndef defined(INTERNATIONAL) || defined(DEBUG)`因为语法规定#ifndef后面只能跟identifier，即定义的宏，不能跟表达式。*

```
#if !defined(INTERNATIONAL) && !defined(DEBUG)
    // neither defined - setup Crittercism
#else
    // one or both defined
#endif
```

或者：

```
#if defined(INTERNATIONAL) || defined(DEBUG)
    // one or both defined
#else
    // neither defined - setup Crittercism
#endif
```

参考：

- [Conditional Compilation](https://www.cs.auckland.ac.nz/references/unix/digital/AQTLTBTE/DOCU_078.HTM)
- [how to use #ifdef with an OR condition?](https://stackoverflow.com/questions/9682593/how-to-use-ifdef-with-an-or-condition)
- [Conditional compilation with ifndef and || doesn't catch second case](https://stackoverflow.com/questions/18535706/conditional-compilation-with-ifndef-and-doesnt-catch-second-case)
