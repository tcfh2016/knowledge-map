## 硬体、核心与Shell

在开始作者对于Shell内容通俗的讲解下，自己突然对linux kernel有些兴趣，无他，就想看看kernel对于多个指令的处理是否是通过不断循环进行多进程创建的方式，或者是进程池的方式，这俨然就是一个典型服务器服务架构嘛。 

上面的是第一个问题，那么第二个问题则是：有时候多个指令可能存在对某些硬件的共享操作，那么这个时候的同步操作是如何进行的呢？是硬体对于要访问的进程主动进行同步，还是各个进程与共享资源紧密结合呢？ 

PS：作者对Shell这个概念讲得非常通俗，所以很自然的让人想到kernel的这两个问题。 

作者在对Shell的Tips当中介绍到，其实常见的GUI应用程序也是一种Shell，其基本原理也是通过GUI来触发对于系统的相关调用，只不过它不是文字界面而已。如此这般，那么在平时称呼各种文字界面的时候更准确的应该是称呼具体的名称，比如Bash Shell, BSH Shell等等。而直接称呼Shell，一是不明其具体指代; 二是其实最初的表意是有些模糊的。 


## 为何要学文字界面的shell?

相比GUI而言，文字界面的shell更为难学，而因为如下的3个方面的优势使其有必要去学习： 

- 大家都一样
- 速度更快
- 在系统管理方面更有优势

## 系统的合法shell与etc/shells功能

通常一套linux发行版本可以支持多个shell，这可以在/etc/shells下面可以查看当前系统支持哪些shell。虽然各家的shell功能差不多，但是在某些语法上面有不同之处，比如Bill Joy设计的BSD Unix系统当中的C Shell的语法就类似C语言。 

对于当前Linux下面默认的shell全称为Bourne Again Shell，它的前身是Steven Bourne开发的称之为sh的Bourne shell。在这里提到了“默认”，这可以在/etc/passwd里面查看到。 

## Bash shell的功能

bash是GNU计划中重要的工具软体之一，也是Linux distributions的标准shell。bash主要相容于sh，并且依据一些使用者需求而加强的shell版本。Linux为何要将其作为预设的shell呢？看看下面它的几个功能： 

1. history 
在～/.bash_history里面记录了之前登录的历史命令，当前的命令记录在记忆体当中，登出之后会写入bash_history。 

2. 命令与档案的补全功能 

3. alias 
可以通过alias查看当前已有的命令别名，也可以直接下达命令来设定别名（如alias lm='ls -al'）。 

4. job控制，前后台操作 

5. shell scripts 
shell scripts可以将日常管理系统经常下达的连续指令写成一个档案，档案可以透过对谈互动式的方式来进行主机的侦测工作，也可以藉由shell提供的环境变数及相关指令来进行设计。 

6. Wildcard 
这个就是所谓的“通配符”，可以用来帮助使用者查询指令。 

## Bash shell的内建命令：type

之前对于“内建命令”一直没有弄清楚，后来就把整个bash shell抽象到程序执行上面，想象着内建命令其实就是bash shell里面直接支持的一些命令，而不用调用系统当中其他的功能。 

使用type可以用来检查一个命令是否为内建指令。因为type 会在 执行档案当中进行搜索，所以它也可以用来作为类似which指令的用途。 

指令的下达
这里提到了如果一行命令太长了，那么可以使用反斜线（\）来完成转义操作的功能。 

## Shell的变数功能

在通过bash下达指令的时候，该指令对应的一些设置通常就存放在一些默认的配置档案中。 

什么是变数？变数其实与一般程序设计语言当中的变量差不多，它的灵活与可变性非常方便，特别是在设计一些Shell Script的时候。bash当中的环境变数就类似于Windows下面的环境变量。看下作者对其的定义： 

> 变数就是以一组文字或符号等，来取代一些设定或者是一串保留的资料！

变数的取用与设定：echo，变量设定规则, unset

使用echo来取用变数，比如echo $PATH/${PATH}。不过这里为什么会有大扩号‘{}’这种用法呢？ 

下面是变数的设定规则，非常重要： 

- 变数与变数内容以一个等号=连接，且等号左右两边无空格（这点尤其注意）
- 变数名称只能是英文字母与数字，开头字元不能为数字
- 变数内容有空白字元可以使用双引号”“或者单引号，区别为双引号支持变数引用，单引号为纯文本
- 使用跳脱字元\可将特殊字符如Enter, $, \, 空白字元,' 等变成一般字元
- 在一串指令中，使用`指令`或者$(指令)来直接调用其他指令
- 为变数扩增内容时，可以使用PATH=”$PATH“:/home/bin来累加内容
- 如果一个变数需要在其他子程序当中执行，那么用export将变数变成环境变数
- 取消变数的方法为使用unset

在练习例子里面似乎为如上为什么变数的引用要写为${NAME}这种有大括号的形式找到一种理由：能够更好的区分出变数，比如想在变数name的后面跟上一个yes，那么这样写 name=$nameyes显然是不对的，但是下面两种方式就没有问题：

name=${name}yes  # 很明确的宣告name当前是一个变量
name="$name"yes   # 与上面的意思完全不一样。

注：读到后面，也即array的时候，发现使用${arr[i]}也显得更为合适，比$arr[i]好吧。

在这里也提到了子程序的概念，也就是在当前的bash shell下面再次启动一个bash shell，这种操作上次在培训C++ STL的时候看到培训讲师使用过，那时候还摸索了一阵他切换过去之后是如何切换回来的，后来知道是使用“exit”返回到当前bash的。

这里的另外一个重要的概念：使用`uname -a`或者$(uname -a)来直接调用bash shell的指令。 

同时，可以使用变量来制定一些经常切换的目录。并且可以将变量写入到bash的设定档案中，这样每次启动bash shell的时候就可以直接cd $work 来进入对应目录了（如何操作？） 


## 环境变数的功能

Bash Shell当前相关的变数基本上可以分做环境变数， Bash操作界面相关的变数，与自定义的变数三类。使用env和export可以显示当前所有的环境变数，而set可以查看所有的变数。 

挺好，在这里总算读到自己这几天一直纠结的“提示字元设定”了，当前为的新系统显示是如下这样： 
    peter87@peter87-ThinkPad-T400:~$ 
    PS1='\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\w\$ ' 

为很想把它改变得短一些。那么这个时候需要知道两件事情： 

1. 这个提示字元是如何定义的？
2. 它定义在哪里？也就是解决了如上“如何定义”的问题之后去哪里修改呢？

对于1，\[\e]0;不知道表示的是什么，\u是目前的账户名，\h是主机名称，\w是工作目录名称，\a不知道，\$是提示字符。我尝试着在当前目录下直接通过PS1=‘\u\$’修改了PS1的设置，立即生效，但是重启之后并没有生效。当前知道可以使用export来将一个变数变为环境变数，使得下一个子程序可以使用（当前不行哟，看来只能修改对应档案啦），同时可用declare将一个环境变数还原为自定变量。

在set当中也能够查看到$与?这两个符号，前者是shell的PID，而后者是上一次指令的执行结果。

需要注意的是，当前所谓的环境变数与bash shell的操作环境不一样。自己认为可以这样理解：环境变数仅仅指的当前可以继承到其他子shell里面使用的变量，有些变量可以在非环境变量与环境变量之间进行变换，而bash shell的操作环境会取用某些默认设定档案当中的内容，是固定的。对吗？

影响显示结果的语系变数（locale）

使用locale -a可以查询到当前的distribution版本支持多少语言编码，而locale指令可以查看当前主机内保有的语系档案（存放在/usr/lib/locale中）。当然，这里比较特别的是在终端tty1 ~ tty6上面是无法支持中文这样比较复杂的文字，所以一般需要使用一些中文花界面的软体。

`read, array, declare`

read用来读取用户的输入，有两个参数-pt，p用来输出提示，t用来指定等待时间。

declare/typeset的用意为“宣告变数的类型”，如果declare不跟任何参数，效果与set一样。declare支持四个参数-aixr，a的意思为将后面的变量定义为array，i为将后面变量定义为整形，x为将后面变量变成环境参数，r为将变量设定为readonly类型。

需要注意的是，因为bash默认对于变数有两个基本约定：其一，变数默认为字符串; 其二，变数的数值运算，最多支持整形运算。

array的设置，目前看起来只能通过var[index] = content的一个一个写作啦。

## 与档案系统及程序的限制关系：ulimit

这个东东前几天还用到过啦，在调试core的时候需要设定呢。其实其功能远不止于此，可以设定创建档案大小啦，开启档案的数量啦，可以通过ulimit -a来查看哟。

一个问题：鸟个提到ulimit -a时对于core size如果显示为0那么也就是没有限制，但是为之前在Linsee上面通过ulimit -c查看为0就默认不输出呢？这个今天要确认下。