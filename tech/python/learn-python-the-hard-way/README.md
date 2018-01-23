
## The Hard Way Is Easier
2016年12月27日16:08:41

序言中作者在讲述“Attention to Detail”时，里面提到的细节的重要性：

 > The one skill that separates bad programmers from good programmers is attention to detail. In fact, it's what separates the good from the bad in any profession. You must pay attention to the tiniest details of your work or you will miss important elements of what you create. In programming, this is how you end up with bugs and difficult-to-use systems.

从亚历山大的摸不着头脑到耐心的对问题进行分析和剥离，这个过程一般难以逃避。回过头去看毕业四年走过的路，转变无非就是碰到问题只能尝试静下心来仔细梳理细节。

## Exercise 1: A Good First Program
2016年12月28日13:05:39

1.一段引用：

> If you did it right then you should see the same output as I in the What You Should See section of this exercise. If not, you have done something wrong. No, the computer is not wrong.

这可以算作一条编程时的纪律：遇到编程错误的时候先从自己身上找原因，大多时候康普特只听命于你，不会乱来。

2.ASCII编码

文中有针对ASCII编码的提示：

> If you are from another country, and you get errors about ASCII encodings, then put this at the top of your Python scripts:
> # -*- coding: utf-8 -*-
> It will fix them so that you can use Unicode UTF-8 in your scripts without a problem.

对于字符编码这部分不是很熟悉,就这个练习来说，当前的理解是如果想在python里面使用print语句输出字符串的时候，字符串恰好在当前的文本编辑器里面不支持，通过如上的 ·# -*- coding: utf-8 -*-· 来设置文本编辑器的编码。这样理解对吗？到底是设置文本编辑器的编码方式还是针对python print的编码语系？


*生词：*

- cryptic 神秘的；含义模糊的。
- drill 训练；钻孔。
- chill out 冷静下来。
- octothorp “#”号。

## Exercise 2: Comments and Pound Characters
2016年12月28日14:38:31

注释，在#号之后加上一个空格看起来更清晰一些。

1.前面提到的格式问题“·# -*- coding: utf-8 -*-·”，这一节的“Common Student Questions”里面提到：Python并不会将它视为有效的代码，参考2中提到这种特定的格式主要用来为文本编辑器提供编码信息，是这样吗？

2.字符串当中的特殊字符并不会被解析，#如是。

3.Read Code Backward
哈哈，软件世界里面总是会碰到让人惊奇的东西，逆序阅读代码，下来试试看。


*生词：*

- pound 英镑；重击；敲打。这里也称#号为"pound"。
- arrogance 傲慢；气焰嚣张。

*参考：*
- [1](http://stackoverflow.com/questions/4872007/where-does-this-come-from-coding-utf-8)
- [2](http://stackoverflow.com/questions/6289474/working-with-utf-8-encoding-in-python-source)

## Exercise 3: Numbers and Math
2016年12月28日15:36:59

1.学习几个运算符的单词
	+ plus
	- minus
	/ slash
	* asterisk
	% percent
	< less-than
	> greater-than
	<= less-than-equal
	>= greater-than-equal

2.运算符

在这里例子当中运算符的优先级 {+, -, /, *, %} 大于 {<, >, <=, >=}，在“Common Student Questions”提到python默认的优先级遵从PEMDAS：Parentheses Exponents Multiplication Division Addition Subtraction。

运算默认以整数进行，如果需要进行floating point运算，只需要将参与运算的数字以小数点的形式表示。

*生词：*

- hen 母鸡；雌性。
- Roosters 公鸡；狂妄自负的人。
- acronym 首字母缩略词。


## Exercise 4: Variables And Names
2016年12月28日17:47:13

1.使用“下划线”来命名变量。

这是例子里面提到的命名方式。

2.在运算符的两边添加空格来保证更好的可读性。

3.占位输出。

使用%s来进行占位，比如：

	>>> variable = 100
	>>> print "YES. You have %s millions!" %variable
	YES. You have 100 millions!
	>>>

*生词：*

- lousy　讨厌的；极坏的。
- get stuck 受骗；遇到困难。

## Exercise 5: More Variables and Printing
2016年12月28日18:17:27

1.单引号与双引号

它们的区别是什么呢？

2.格式化输出

在文档里面查询到有多重输出格式:

	d	Signed integer decimal.
	i	Signed integer decimal.
	o	Unsigned octal.	(1)
	u	Unsigned decimal.
	x	Unsigned hexadecimal (lowercase).	(2)
	X	Unsigned hexadecimal (uppercase).	(2)
	e	Floating point exponential format (lowercase).
	E	Floating point exponential format (uppercase).
	f	Floating point decimal format.
	F	Floating point decimal format.
	g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
	G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
	c	Single character (accepts integer or single character string).
	r	String (converts any python object using repr()).	(3)
	s	String (converts any python object using str()).	(4)
	%	No argument is converted, results in a "%" character in the result.

详细参见参考链接。


*生词：*

- handy　便利的；容易取得的。

*参考：*
- [String Formatting Operations](https://docs.python.org/2.4/lib/typesseq-strings.html)


## Exercise 6: Strings and Text

例子里提到 %r 与 %s 的区别，作者虽然提及了 %r 用来表示变量的raw data，常用来调试。但对于raw data的概念自己并不是很清晰。	在segment fault中的一种解释稍微通俗一点：%s将打印string对象q，%r打印被repr处理后的string对象（非q）

*参考：*

- [segment fault](https://segmentfault.com/q/1010000000163896)


## Exercise 7: More Printing

1.输出行合并

这一节里的例子里面得知可以使用逗号“,” 来将两行的打印连接在一行。比如：

	# Test the comma usage.
	print "you",
	print "are"

	print "you"
	print "are"

输出：
	you are
	you
	are

2.注释相关

在“Common Student Questions”里面作者提到尽管在“Study Drill”里面提到给代码添加注释，但并不是要求严格为每行代码均如此做：

> Is it normal to write an English comment for every line of code like you say to do in Study Drill 1?

> No, you write comments only to explain difficult to understand code or why you did something. Why is usually much more important, and then you try to write the code so that it explains how something is being done on its own. However, sometimes you have to write such nasty code to solve a problem that it does need a comment on every line. In this case it's strictly for you to practice translating code to English.

并且，作者提到当你发现每行代码都需要注释时，就需要“写好”代码了。

3.单引号与双引号

单引号与双引号在python里没有明显的区别，习惯用法上给比较短的字符串上使用单引号。

*生词：*

- chops　排骨。
- fleece 羊毛。
- magicians 魔术师。


## Exercise 8: Printing, Printing
2016年12月28日22:24:30

好吧，感觉做了好多道print的题目了，快晕掉了。

理解 %r与%s 的区别更近了一步。比如例子中的如下代码，

	formatter = "%r %r %r %r"

	print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
	)

其输出为：

	'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'

输出结果的第3句为双引号，同时其他三句为单引号。可见为什么作者多次提到%r一般在调试时候使用，用来输出程序员编写代码时候的变量值。这个时候如果仍旧使用单引号，那么就没有办法将输出区分出来了，所以python做了一次输出格式调整。

那如果问：为什么输出要添加单、双引号呢？这个，我觉得应该是为了与%s相区分吧...

## Exercise 9: Printing, Printing, Printing
2016年12月29日07:18:40

一大清早的起来，看到这一课还是print，讶异至极。

1.print 格式小结

刚在敲击print的时候看到在末尾输出变量的用法时末尾的逗号“,”，一时想起逗号的作用，同时发现格式化输出的时候并没有逗号，这里一并记录它们：

- 在末尾输出单个变量，末尾跟上逗号：print "Here are the days: ", days
- 逗号的另外一个用法：连接两行的print输出
- 格式化输出的时候并不需要逗号来分隔字符串区与参数列表区：y = "Those who know %s and those who %s." % (binary, do_not)

运行完该节的例子之后留意到它新增了两种print知识点：

- 在字符串当中使用 \n 等特别字符来调整输出格式。
- 使用 """ 符号来定义一个跨行的字符串。

2.%r与%s的区别到底是什么？

不得不说看完“Common Student Questions”里的第一个问题之后，自己觉得已然明了它们之间的区别。所谓%r输出的"raw data"即是在程序员眼中它的本来样子，而%s则是python将其处理之后的样子，看完下面这段代码就能很好的理解它：

	months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
	print "Here are the format: %r " % months
	print "Here are the format: %s " % months

输出为：

	Here are the format: 'Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug'
	Here are the format: Jan
	Feb
	Mar
	Apr
	May
	Jun
	Jul
	Aug

不错不错的，这是今早早起的一个让人兴奋的礼物:)

## Exercise 10: What Was That?

转义字符的使用，在字符串中使用"\"来达到一些不可告人的目的，是的，不可告人，因为是告诉给康普特嘛~

从“Common Student Questions”最后一问中学习到字符串的四种样子：

- 'string.'
- "string."
- '''string.'''
- """string."""

*生词：*

- toes　脚趾。

## Exercise 11: Asking Questions
2016年12月29日11:07:34

1.再看%r

在前面中的例子里面有使用%r的时候如果字符串里面有“ ' ”符号，那么输出里面为了输出这个单引号便会将这个字符串使用双引号括起来。但如果字符串里面即有单引号又有双引号，会发生什么情况呢？见下面这个例子：

	# Change ' to " because ' exist in string.
	print "%r %r" % ("But it didn't sing.",	"So I said goodnight.")

	# Keep ' unchange because both ' and " exist in string.
	print "%r %r" % ("But it didn't sing \"LOVE\".",	"So I said goodnight.")

输出为：

	"But it didn't sing." 'So I said goodnight.'
	'But it didn\'t sing "LOVE".' 'So I said goodnight.'

很显然，%r的输出会根据输出字符串做些格式上的微调，以保证显示效果。

*生词：*

- fairly　相当地；公平地。

## Exercise 12: Prompting People
2016年12月29日11:34:26

两个知识点：

1.输入提示

使用类似 age = raw_input("How old are you?") 的语法在命令行给出提示的同时从命令行获取输入。

2.pydoc使用

pydoc是python的参考文档，一般分布在网络上和本地。Windows上面使用"python -m pydoc open"来查阅对应的函数的方式即是查看本地的文档。

## Exercise 13: Parameters, Unpacking, Variables
2016年12月29日13:10:59

参数变量：Argument Variable，这些变量是在执行python脚本的同时传递给程序本身的。如果考虑程序的输入，现在在我脑子里面大概有下面几种类型：

- 程序执行过程当中提示用户输入。这种方式即是前面最初接触的输入部分。
- 使用参数变量。也就是这一节里面学习到的这种方式。
- 读取文件。来自其他如C/C++的学习经验。
- 进程间数据共享（共享内存、消息机制等。来自其他如C/C++的学习经验。

很显然，前面两种方式有些欠缺灵活。

需要注意的是，参数变量都是以字符串的形式写入，如果你需要整数类型的参数就需要动用int()的大斧头进行强制转换了。

*生词：*

- jargon　行话；术语。
- replicate 复制；重复。
- slap 拍击；掌击；直接地。

## Exercise 14: Prompting and Passing
2016年12月29日18:23:55

*生词：*

- slightly　轻微地；稍稍。
- figure out 解决；想出。

## Exercise 15: Reading Files
2016年12月29日18:43:59

Hard coding的解释：

> "Hard coding" means putting some bit of information that should come from the user as a string directly in our source code.

编码的时候时常听说魔术字，它们之间的细微关系是怎样的？

在“Common Student Questions”作者解释第一个问题的时候将open(filename)返回的文件对象类比为DVD播放器，这种类比觉得非常形象。

*生词：*

- fancy　幻想；想象的；奇特的。

## Exercise 16: Reading and Writing Files
2016年12月29日20:24:02

与文件操作的几个操作：

- close 文件关闭操作。
- read 读取文件内容。
- readline 读取文件的一行.
- truncate 清空文件。
- write('stuff') 将"stuff" 写入文件.


*生词：*

- truncate　截断的；把...截短。
- square away 迎风扬帆；摆好姿势；把一切弄整齐。

## Exercise 17: More Files
2016年12月29日20:57:43

例子中的文件拷贝是一行一行的进行拷贝，这让我想起大二学习C语言的时候，觉得文件操作太神奇了，心中颇有点自惭形秽，以至于都懒得动手去练习。

其实对于编程自己一直以来兴趣并不大（其实其他事情亦然），这或许才是我没有动手去练习的根本原因。如今八年过去，兴趣依然不是很大，然而，身在软件行业却知道程序设计语言作为一种工具的重要性。几年下来，也明白了很多事情在安静下来去琢磨一阵子之后便可显现出其实际、可把握的一面。

虽小道，必有可观者焉。

*生词：*

- blast　爆炸；冲击波。

## Exercise 18: Names, Variables, Code, Functions
2017年1月3日13:55:12

1.当前感受
目前学习到函数，对比写C++，python即不需要末尾的标点，也不需要为每个变量指定类型，觉得自在了不少。

刚测试例子代码的时候自己写错了，刚好在标点符号上：python里面的函数定义需要加上冒号。总结一下，python当中函数的写作需要注意：

- 使用关键字“def”来定义函数。
- 函数体统一缩进四个空格。
- 如果需要使用参数列表，用关键字“*args”表示。一般不建议在函数中如此使用。

2.函数写作
看来仅仅这样还不够，在“Study Drills”当中作者整理了一个checklist，专门用于在编写函数时候进行检查。

2.1定义函数时的checklist

- 在函数定义的开头使用 def。
- 保证函数名称仅仅包含字符和下划线。
- 在函数名称之后要加上括号，并且使用逗号来分隔括号里面的参数。
- 参数名称必须唯一。
- 函数体必须采用4个空格的缩进格式。
- 函数以顶格的行结束。

*（注：变量名称仅允许 数字、字母和下划线 三种字符组成，这里不建议在函数名称中使用数字。）*

2.1使用函数时的checklist

- 通过指定“函数名称+括号”来调用一个函数。
- 在函数调用时将参数填写在括号中并用逗号分隔开。

*生词：*

- monotonous　单调的。


## Exercise 19: Functions and Variables
2017年1月6日14:40:51

1.变量
通过“=” 来创造一个变量。作者这里提到了"make"，不像C/C++里面的"define"/"declare"，准一下子就把新人搞晕掉。看来“人生苦短，Python当歌”还是有些道理呀。

>In a way, the arguments to a function are kind of like our = character when we make a variable. In fact, if you can use = to name something, you can usually pass it to a function as an argument.

2.代码风格
末尾“Common Student Questions”当中的讲解提到了与代码风格相关的两点：

- 在同一代码文件当中尽量避免使用相同名称的变量，比如不要让全局变量与函数内部的局部变量相同。
- 函数的参数尽量不要超过5个，以免代码太难看。

*生词：*

- mind-blowing　使兴奋得；引起幻觉的。
- reinforce 加强；求援。

## Exercise 20: Functions and Files
2017年1月6日16:02:31

1.单变量操作的缩写式

	current_line = current_line + 1
	current_line +=  1

如上两者等价，正如"it is"缩写为“it's”。

2.使用逗号

在《Exercise 7: More Printing》提到使用逗号来将两行的打印连接在一行。在阅读“Common Student Questions”最后一问之后觉得这样说或许不正确，在print时使用逗号的真正目的是“不在末尾打印换行符‘\n’”。


*生词：*

- rewind　倒回；重绕。

## Exercise 21: Functions Can Return Something
2017年1月6日16:55:55

依旧是函数，但是可以使用return语句来给函数调用者返回一个值。

*生词：*

- whack 重击；猛击。

## Exercise 22: What Do You Know So Far?
2017年1月6日18:07:14

Yeah! 这一课不用敲代码哟~

想一想，就这样直接回忆一下学过的知识，不过这里按照作者的提议，以word为线索。

- print
首当其冲是print，当时学了好多课，有天白天学习好几课的print，结果第二天早上起来仍旧是print。所以，印象深刻。与print相关的有逗号（","）、占位符（"%r", "%s", "%d"等等）、百分号（"%"）

- raw_input
上面是输出，所谓“上吐下泻”，上下缺一不可：软件之运转需要输入。这个关键字是用来在命令行之下问用户要取输入的，并且刚毅到不到黄河心不死的地步。

- from sys import argv
输入，与楼上不同，这个输入是从在一开始执行python脚本就必须指定的参数，又称“命令行参数”。

- open-close-read-write
文件操作。

- def-return
函数定义，定义函数。

想到这里觉得自己有编程基础，所以可以随便乱写。对于没有编程基础的学习人员，一开始可能会比较痛苦。但学习理论在阳师那里，热爱学习、坚持进步之下百分之九十的困难都是纸老虎，一起加油吧。

*生词：*

- nail down 确定；明确。

## Exercise 23: Read Some Code
2017年1月6日18:34:47

一篇好的文章，或者一本好书，除了是诚心之作之外，通常会有不少附加福利：即有很多可供拓展学习的知识点。这一章的内容起码有两个可供学习：

1.代码集中营

作者提到的几个网站，定是国外，或者说是程序界共同认同的有代表性的站点。真有心，是可以全力深耕于此的。

2.学习方式

访问站点-->搜索"python"-->选择项目-->开读-->记录自己所想-->查阅解惑。非常直接的学习方式，当前跟随开智学堂学习，里有同侪互助，是不是努力之下可以收获更多呢？

*生词：*

- daunting 令人生畏的；令人气馁的。
- anthropologist 人类学家。
- trucking 货车运输；交易。
- jungle 丛林；密林。

*站点:*

- bitbucket.org
- github.com
- gitorious.org
- launchpad.net
- sourceforge.net
- freecode.com

## New Start
2018年1月10日21:17:42

刚对照着代码看了之前的学习笔记和代码，举得有个地方可以改进：在代码当中贴上程序调试的输出，
方便之后阅读之后进行脑中验证。

至于在第23课作者建议的阅读代码，我可以去阅读另外一款工具的代码，并且打算这本书阅读完之后
将其重写一遍。

2018年1月15日11:00:52
不妨将工具代码的阅读笔记作为这一课的作业。

#### emil-decoder:script: lte-decoder.py

1.`if __name__ == "__main__":`代表什么意思？

查阅 StackOverFlow，得知`__name__`是每个源代码文件在执行时均有的隐式变量，当它被当做程
序执行时，该变量设置为`__main__`，当它被当做模块引入其他文件中时该变量设置为`模块名称`。

https://stackoverflow.com/questions/419163/what-does-if-name-main-do

2.参数解析模块`argparse`

2018年1月16日10:19:49

`argparse`是Python标准库中用于命令行参数解析的模块，它提供的功能包括：

- 从sys.argv解析出对应的参数内容
- 提供usage提示 （*提示用户输入指引。*）
- 提供error提示 （*用户输入错误的参数。*）

参考链接：
- https://docs.python.org/3/howto/argparse.html#id1
- https://docs.python.org/3/library/argparse.html#module-argparse
- https://pymotw.com/2/argparse/

#### emil-decoder:src: config.py

1.`class`的组成形式

如其他支持OOP的编程语言一样，Python中的对象也是对一组数据以及操作这些数据的封装。我们同
样使用关键字`class`来定义一个类，并由类来完成对象创建的工作。通常一个类包括：

- __init__(self) 函数，在对象创建时调用完成初始化。
- 对象方法，即class里面定义的函数，按照约定所有的函数的第一个参数是`self`。
- 数据成员。


Python里面有一些特殊方法，比如 `__str__`和`__repr__`，前者用来生成对象的字符串表示，后
者用来生成对象的官方表示，通常情况下后者与前者的实现相同（因为后者不太实用。《Python编程
入门》P158）。

https://stackoverflow.com/questions/12448175/confused-about-str-in-python

创建类时，推荐同时编写`__str__`和`__repr__`，它们对于显示对象内容，对于调试非常有帮助。


class中的私有变量需要在字符前加上`__`前缀，这样设置之后只能在类的方法里面访问它们，类外
不能直接访问（访问需要通过 `p._Person.__age`这种方式）。编程时一条实用的方式是先将所有
对象变量都设置为私有变量，在有充分理由的情况下将其修改为公有的。

class中的设置函数（setter）和获取函数（getter）可以通过特性装饰器来完成。在代码调试了半
天发现必须使用新的语法才能够让装饰器生效：`class Person(object):`。

https://stackoverflow.com/questions/16502133/python-property-decorator-not-working-why

2.读写文件

文件是一个命名的比特集合，存储在硬盘、U盘、闪存等辅助存储设备中。文件可以分为文本文件和
二进制文件两类。

文本文件通常比等价的二进制文件大。需要通过网络发送大型文本文件时通常对其进行压缩来提高传
输速度和节省磁盘空间。


- `os.getcwd()` 返回当前工作目录的名称
- `os.listdir(p)` 返回一个字符串列表，包含路径p指定的文件夹中所有文件/文件夹的名称。
- `os.chdir(p)` 将当前工作目录设置为路径p。
- `os.stat(fname)` 返回有关fname的信息，比如大小、最后一次修改的时间等。
- `os.path.isfile(p)` 当路径p指向的是一个文件时，返回True，否则返回False。
- `os.path.isdir(p)` 当路径p指向的是一个文件夹时，返回True，否则返回False。
- `os.path.join(path, *paths)`  进行路径拼接。


2.`os.path`的使用

- `os.path.isdir`
- `os.path.isfile`
- `os.path.dirname`
- `os.path.join`
