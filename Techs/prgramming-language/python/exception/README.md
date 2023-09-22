## 异常

异常，是改变程序中控制流程的事件。每当在程序运行时检测到错误时，就会引发异常。通常而言，Python默认的异常处理就是我们想要的，尤其对顶层脚本文件中的代码，错误通常应该立刻终止程序。就许多程序而言，没有必要再更加明确代码中的错误。但是，有些场景下你并不想异常造成程序终止，而是想捕捉错误并从中恢复，比如网络服务器。

```
try:
  ...
except Exception as e:
  logger.error('failed with: '+ str(e))
```

## 捕获异常

对于异常的处理可以简单分为两类：

- 忽略错误，那么将激活Python的默认异常处理行为，通常是停止程序并打印出错消息。
- 使用异常处理器try进行捕获，程序在try进行处理之后会重新执行。

比如如下的示例是访问不存在的元素，程序会停止执行并且打印出“IndexError: string index out of range”的错误。

```
def fetcher(obj, index):
    return obj[index]

x = 'spam'
fetcher(x, 4)
```

但只要编写我们自己的异常处理流程，那么就可以正常的对异常进行处理，即便异常产生也不会中断程序：

```
def fetcher(obj, index):
    try:
        return obj[index]
    except IndexError:
        print('wrong index!')

x = 'spam'
fetcher(x, 4)
```

try是复合语句如下所示，先以try作为首行，后紧跟缩进的语句代码，然后是一个或多个except分句来识别要捕获的异常，最后是一个可选的else分支。

```
try:
  <statements>
except <name1>:
  <statements>
except (name2, name3):
  <statements>
except <name4> as <data>:
  <statements>
except:
  <statements> # 捕获任何异常
else:
  <statements> # 不发生异常时执行
```

在Python 2.5及之后的版本中，可以在同一个try语句中混合finally, except以及else子句。


## try/finally

finally代码块是用来执行不管异常是否发生一定会执行的语句块，它通常在异常场景下进行资源回收的操作。和try/except不同的是，当异常发生的时候finally会执行，之后会继续将异常传递给上一层try语句或者顶层默认处理器，不会像except那样终止异常。


## with/as 环境管理器

Python 2.6和Python 3.0引入了新的异常相关的语句：with及其可选的as子句。这个语句的设计是为了和环境管理器对象一起工作。

简而言之，with/as语句的设计是作为常见try/finally用法模式的替代方案，它也是用于定义必须执行的终止或“清理”行为，无论处理步骤中是否发生异常。
