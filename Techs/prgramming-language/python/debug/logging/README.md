## logging

logging相比print打印有不少优势，首先，print语句供临时使用，在调试的时候添加，调试之后需要删除。其次，print只能够打印到终端，而logging可以输出到指定的文件。再次，logging还能够进行日志分级控制。

logging打印的日志分5个层级：

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

## 基本用法

使用logging功能需要包含`logging`模块，默认的级别是WARNING，默认输出到终端，但可以指向到文件：

```
import logging

# 打印到终端
logging.warning('Watch out!')

# 配置输出文件，和打印级别
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
```


## Q&A

- ValueError: Unrecognised argument(s): encoding

参考[Logging error on run](https://github.com/xZaR3y4p/Img_link_to_local_markdown/issues/2)，这是因为logging.basicConfig()里面的encoding参数是在python 3.9的时候添加的，如果执行的Python版本较低会有这个错误。

workaround方案：

```
logging.basicConfig(filename='Img_To_Local_Python.log', encoding='utf-8', filemode="w", level=logging.DEBUG)

替换为：

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('Img_To_Local_Python.log', 'w', 'utf-8')
root_logger.addHandler(handler)

或者：

logging.basicConfig(handlers=[logging.FileHandler(filename="./log_records.txt", encoding='utf-8', mode='a+')],
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.DEBUG)
```

## 参考

- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Python Logging Tutorial](http://www.patricksoftwareblog.com/python-logging-tutorial/)
