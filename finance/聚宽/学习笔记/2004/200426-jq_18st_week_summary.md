# 聚宽学习周记十八：详解@东南有大树的“指数估值自动报表系统”（下）

这周工作上有点忙，经常加班，所以没有多少时间放在聚宽的学习上，这周的周记就只能划水划过去了。五一这两天找了点时间把上周测试得差不多的改写自@东南有大树的指数估值策略发布到模拟交易，接下来一周看看效果。这周的周记只能简单写写将研究文件发布到模拟策略过程中的一些事了。

## 从“策略研究”模块到“模拟交易”模块的切换

把研究内容发布到实盘策略并不是看起来的那么简单，因为策略环境与研究环境是不一样的，我之前以为无非就是将研究环境里面的代码拷贝成单独的`.py`文件做成python库，然后在策略直接引用即可，结果花了四、五个小时才搞成功。如下是碰到的几个主要问题。

### 1：从策略里面引用的自定义库只能放在‘研究环境’根目录

之前在'研究环境'里面进行测试的时候，新建了一个`repotool`文件夹，在里面存放了自定义的函数库，同时也新建了`/pic`和`/database`目录用来存放图片和数据，然后在ipynb研究文件里面进行测试。

然而，当我在策略里面通过`from repotool.mailservice import *`来引用repotool文件夹下面mailservice.py里面定义的函数时，就没有办法完成预想的功能了。因为当前不支持这么做，会碰到下面这样的错误：

```
File "/tmp/strategy/user_code.py", line 1, in <module>
  from repotool.valuationlib import *
File "/tmp/jqcore/jqboson/jqboson/plugin/web.py", line 62, in import_
  raise ImportError('您是否想导入研究中的自定义库? 自定义库暂时不支持文件夹, 请把库文件放在研究根目录: {}'.format(name))
ImportError: 您是否想导入研究中的自定义库? 自定义库暂时不支持文件夹, 请把库文件放在研究根目录: repotool.valuationlib
```

因此只能把自定义的函数库放在研究环境的根目录。

### 2：研究环境和策略环境是不同的

需要留意研究环境和策略环境在运行时的上下文是不一样的，特别是有些库默认在研究环境下导入了，但是策略环境下面并没有导入。

比如，在自定义的函数库里面我们需要执行`plt.savefig(picture_path + picture_name)`来调用matplotlib.pyplot来把图片保存下来。这在研究环境下面是不需要显式的导入，但是当这个函数库需要在策略里面导入时，必须要显式在其中到入，即加上`import matplotlib.pyplot as plt`。

### 3.策略环境中读写研究环境中的文件必须要使用聚宽提供的特定接口

由于部署一直不成功，我花了很长的时间对比大树兄的代码，最终找到关键点在头文件`from kuanke.user_space_api import *`,以及两个读写函数`read_file()`和`write_file()`，之后跑去聚宽API文档上面一看，才恍然大悟，这两个函数是用来在策略/模拟环境中读写研究环境中文件的方法，它们原来早在[其他函数](https://www.joinquant.com/help/api/help?name=api#%E5%85%B6%E4%BB%96%E5%87%BD%E6%95%B0)就写明了。而`from kuanke.user_space_api import *`是导入自定义的python库必须要添加的语句，也在API文档里面有写明。

饶了一大圈发现自己还是没有完整阅读聚宽API文档，闷着头摸索花费了好多时间！


参考：

- [Python文件读写、StringIO和BytesIO](https://www.jianshu.com/p/b74a83e0f9fc)
- [Difference between `open` and `io.BytesIO` in binary streams](https://stackoverflow.com/questions/42800250/difference-between-open-and-io-bytesio-in-binary-streams/42800629)


## 二、上周计划任务

### 1. 继续完善[指数估值自动报表系统——源代码](https://www.joinquant.com/view/community/detail/20497)里自动报表系统的改写，功能完成之后看是否能够在布局上做得更美观一点。

没时间搞啊兄弟！

### 2. 在理解函数`send_message()`的时候发现聚宽本身定义了这个函数用来发送微信消息，当前自己在进行ETF定投，都是使用聚源数据提供的指数估值来进行决策，受这篇文章的启发其实可以尝试手动计算当前指数的估值，这样每天就可以实时掌握指数的估值状态了。

没时间搞啊兄弟！

## 三、本周新学内容

真木有。

## 四、下周学习任务

### 1. 尝试完成上周布置的两个任务。

### 2. 另外一个想法是扩大指数估值的统计范围，从当前支持的20只指数扩展到所有指数，然后去前50位。
