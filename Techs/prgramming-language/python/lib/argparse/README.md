`argparse`是python标准库内置的命令行解析模块，类似模块功能的还有`getopt`和`optparse`，`argparse`基于`optparse`。

## 基本概念

命令行参数可以细分为两类：

- positional argument : 位置参数，参数的含义与其参数的位置有关。
- optional argument   : 可选参数。

比如使用`cp src dest`命令时，第一个参数`src`表示要拷贝的源文件，`dest`表示拷贝的目的文件。而 `ls -l`命令中的`-l`表示可选参数。

## 简单用法

使用`argparse`最简单的用法是单纯将其应用在代码中：

```
import  argparse
parser = argparse.ArgumentParser()
parser.parse_args()
```

上面3句代码提供了最简单的命令行解析功能：仅仅支持对`-h`, `--help`的解析。其他的均会报错。

执行`python bin2text.py -h`：

```
>
>usage: bin2text.py [-h]
>
>optional arguments:
>
>  -h, --help  show this help message and exit
>
```

执行`python bin2text.py foo`：

```
>usage: bin2text.py [-h]
>
>bin2text.py: error: unrecognized arguments: foo
```

## 位置参数

位置参数是必须要指定的参数，通过 `add_argument`来添加位置参数，并且可以指定帮助信息，以及类型（默认为字符串）。如下的示例是添加一个名为`echo`参数，并且在解析时将其当做`int`类型来处理（argparse默认将解析的参数内容都当成字符串类型）。

```
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here.", type=int)
```

位置参数是必须要输入的参数，并且argparse会根据参数的位置去解析它，如果在解析命令的时候没有得到对应的参数内容，那么会提示错误。

## 可选参数

可选参数的添加需要在参数名称前面添加“-”，该参数后面可以跟上参数值，也可以不跟。同样可以指定参数的type, action。

1.默认形式：argparse会解析可选参数后面的参数值。

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print "verbosity turned on"
```

2.简单形式：argparse不解析可选参数后面的参数值，只根据是否指定了可选参数得到True/False。

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
   print "verbosity turned on"
```

*190610 注：位置参数是通过参数的顺序去推算对应的参数值，而可选参数是显示指定参数值。*

## 同时使用位置参数和可选参数

总结下参数使用过程中的几个要点：

- 通过`type`指定类型，默认为字符串。
- 通过`choices`指定可选值。
- 通过`default`设置默认值，如果`argparse`没有解析到某个参数，那么默认值为None。

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")                    
```

## 使用`add_mutually_exclusive_group()`

有些时候一些命令具有互斥关系，即指定了`-v`就不能指定`-q`，这个时候就需要使用专门的方法。

```
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y
```

## 为一个参数传递多个值

有两种方式：使用`nargs`和`append`action。

```
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
# Use like:
# python arg.py -l 1234 2345 3456 4567

parser.add_argument('-l','--list', action='append', help='<Required> Set flag', required=True)
# Use like:
# python arg.py -l 1234 -l 2345 -l 3456 -l 4567
```

## 参考

- [argparse](https://docs.python.org/2/howto/argparse.html)
- [argparse option for passing a list as option](https://stackoverflow.com/questions/15753701/argparse-option-for-passing-a-list-as-option)
