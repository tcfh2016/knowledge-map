# 第7章 高质量的子程序 / High-Quality Routines

子程序（routine）是为实现一个特定的目的而编写的一个可被调用的方法（method）或过程（procedure），
例如C++中的函数(function)，Java中的方法（method），或Microsoft Visual Basic中的函数
过程（function procedure）或子过程（Sub procedure）。

## 7.1 创建子程序的正当理由 / Valid Reasons to Create a Routine

- 如果没有子程序的抽象能力，我们的智力将根本无法管理复杂的程序。

## 7.2 在子程序层上设计 / Design at the Routine Level

- 内聚性（cohesion）的概念是由 Wayne Stevens, Glenford Myers 和 Larry Constantine在
1974年发表的一篇论文中提出来的。其他一些更为现代的概念，如抽象和封装等，通常在类这一层次
的设计中更为适用，但内聚性的概念仍然存在，而且在单个子程序这一层次上，仍是设计时常用的启
发式方法。
- 功能的内聚性（functional cohesion）是最强也是最好的一种内聚性，也就是说让一个子程序仅
执行一项操作。

## 7.3 好的子程序名字 / Good Routine Names

- 子程序的名字应当描述其所有的输出结果以及副作用。
- 研究表明，变量名的最佳长度是9到15个字符，而子程序名的长短要视该名字是否清晰易懂而定。
- 给过程起名时使用语气强烈的动词加宾语的形式，在面向语言中，你不用在过程名中加入对象的名
词（宾语），因为对象本身已经包含在调用语句中了。

## 7.5 如何使用子程序参数 / How to Use Routine Parameters

- 把子程序的参数个数限制在大约7个以内。心理学研究发现，通常人类很难同时记住超过7个单位的
信息。

## 7.6 使用函数时要特别考虑的问题 / Special Considerations in the Use of Functions

- 函数是指有返回值的子程序；过程是指没有返回值的子程序。在C++中，通常把所有子程序都称为
函数，然而，那些返回值类型为void的函数在语义上其实就是过程。
- 如果一个子程序的主要用途就是返回由其名字所指明的返回值，那么就应该使用函数，否则就应该
使用过程。

## 7.7 宏子程序和内联子程序 / Macro Routines and Inline Routines

- 节制使用inline子程序：
  - inline子程序违反了封装原则，因为C++要求其实现在头文件里，将实现细节暴露给使用者；
  - 会增加整体代码的长度；
  - 为性能原因使用inline需要通过剖测（profile）代码衡量性能上的改进看是否值得。
