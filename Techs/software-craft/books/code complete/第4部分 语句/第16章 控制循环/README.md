## 第16章 控制循环

循环是一个非正式术语，用来指代任意一种迭代控制结果。使用循环是编程中最复杂的方面之一；知道如何以及何时使用每一种循环是创建高质量软件的一个决定性因素。

### 16.1 选择循环的种类

1）什么时候使用while循环

while循环是一种灵活的循环选择。如果你预先并不知道循环要迭代多少次，那么就使用while循环。有关while循环最主要事项就是决定在循环开始处还是结尾处做检测。

2）什么时候使用for循环

如果你需要一个执行次数固定的循环，那么for循环就是一个很好的选择。如果存在一个必须使执行从循环中跳出的条件，那么就应该改用while循环。

类似地，不要在for循环里通过直接修改下标值的方式迫使它终止，这种情况应该使用while循环。for循环就是为了简单的用途，更复杂的循环最好用while循环去处理。

3）什么时候使用foreach循环

foreach循环或等价物很适用于对数组或者其他容器的各种元素执行操作。它的优势在于消除了循环内务处理算术，从而也就消除了任何由循环控制算术导致出错的可能性。

### 16.2 循环控制

循环错误可以归结到下面问题之一：忽略或错误地对循环执行初始化、忽略了对累加变量或其他与循环有关的变量执行初始化、不正确的嵌套、不正确的循环终止、忽略或者错误地增加了循环变量的值，以及用不正确的循环下标访问数组元素等。

在适当的情况下多使用for循环，因为for循环把循环的控制代码集中在一起从而有助于写成可读性强的循环。但在while循环更适用的时候不要使用for循环。

在嵌套循环中使用有意义的变量名来提高可读性、避免下标串话。循环尽可能短，长循环的内容移到子程序里，嵌套应控制在3层以内。

### 16.3 轻松创建循环——由内而外

如果你在编写复杂循环的时候遇上麻烦，可以使用一种简单的技巧来让它从一开始就是正确的。首先用字面量（literal）来编写代码，然后缩进它，在外面加上一个循环，然后用循环下标或计算表达式替换那些字面量。如果需要，在它的外面再套上一个循环，然后再替换掉一些字面变量。根据你的需要持续这一过程。等你做完以后，再加上所有需要的初始化。由于你是从简单的情况开始并且由内而外生成代码的，因此你可以把这一过程看做是由内而外的编码。

这里的要点在于从具体事件入手，在同一时间只考虑一件事，以及从简单的部分开始创建循环。在开发更通用、更复杂循环的过程中，你迈的步子要小，并且每一步的目的要容易理解。这样一来，你就可以减少在同一时间需要关注的代码量，从而减少出错的可能。

### 16.4 循环和数组的关系

循环和数组之间有着密切的联系。在许多情况下，循环就是用来操纵数组的。不过值得一提的是，循环结构和数组并不是天生就相互关联的，有些语言，特别是APL和Fortran 90提供了强大的数组操作功能。这说明了一点，那就是你通过编程来解决问题，而有的时候这种解决方案是特定于语言的。你所用的语言将在相当大的程度上影响到你的解决方案。
