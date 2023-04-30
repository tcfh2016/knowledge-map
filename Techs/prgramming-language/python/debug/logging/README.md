## logging

logging相比print打印有不少优势，首先，print语句提供的信息是有限的，通常供临时使用，而logging可以提供时间戳、打印日志的模块以及代码行号。其次，print只能够打印到终端，而logging可以输出到指定的文件。再次，logging还能够进行日志分级控制。

logging打印的日志分5个层级：

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

参考：

- [](https://www.pylenin.com/blogs/python-logging-guide/)


## 基本用法 / ValueError: Unrecognised argument(s): encoding

使用logging功能需要包含`logging`模块，默认的级别是WARNING，默认输出到终端，但可以指向到文件：

```
import logging

# 打印到终端
logging.warning('Watch out!')

# 配置输出文件，和打印级别
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
```

如果使用上面的代码配置会碰到“ValueError: Unrecognised argument(s): encoding”这样的错误，参考[Logging error on run](https://github.com/xZaR3y4p/Img_link_to_local_markdown/issues/2)，这是因为logging.basicConfig()里面的encoding参数是在python 3.9的时候添加的，如果执行的Python版本较低会有这个错误。

workaround方案：

```
logging.basicConfig(filename='Img_To_Local_Python.log', encoding='utf-8', filemode="w", level=logging.DEBUG)

替换为：

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('Img_To_Local_Python.log', 'w', 'utf-8')
root_logger.addHandler(handler)

或者：

logging.basicConfig(
    handlers=[
                logging.FileHandler(filename="./log_records.txt", encoding='utf-8', mode='a+')
             ],
    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
    datefmt="%F %A %T",
    level=logging.DEBUG)
```


## 配置输出信息

使用`format`参数，可以在输出时提供更多额外的信息，比如时间戳、日志级别、用户名、代码源文件名、行号以及具体的日志信息：

```
log_format = "%(asctime)s::%(levelname)s::%(name)s::%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(level='DEBUG', format=log_format)
```

当然，对于时间戳，可以用`datefmt`来设置展示方式：

```
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
```

参考：

- [Print timestamp for logging in Python](https://stackoverflow.com/questions/28330317/print-timestamp-for-logging-in-python)
- [Python Logging Basic Configurations](https://www.studytonight.com/python/python-logging-configuration)


## 输出到文件

日志默认输出到终端，但使用`filename`参数可以将其输出到指定的文件中，每次执行程序时日志会不断附加到日志文件中：

```
log_format = "%(asctime)s::%(levelname)s::%(name)s::"\
             "%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(filename='mylogs.log', level='DEBUG', format=log_format)
```

*疑问：怎么配置日志不能无限制增长？*

首先，可以使用在配置里面添加`filemode='w'`来进行覆盖原有旧文件。


## 多模块记录

模块调用模块是程序中最常见的设计，比如模块A, B里面都需要记录日志，这个时候记录日志该怎么配置呢？

首先需要明确的一点是，如果在模块A，B里面都使用`logging.basicConfig`配置了日志输出的参数，那么默认以第一次配置生效的为准。这样不管层级有多少，输出的日志里面默认都是“root logger”（表示最高的层级），为了便于区分可以配置“main logger”，当然还需要配置其他的：

```
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__name__)

logger.setLevel('DEBUG')

file_handler = logging.FileHandler("mylogs.log")
formatter = logging.Formatter(log_format)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info("I am a log from project")
```



## 参考

- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Python Logging Tutorial](http://www.patricksoftwareblog.com/python-logging-tutorial/)
