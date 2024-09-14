## 用户定义的类

类定义了新的对象类型，扩展了核心类型。

目录：

- [基础](./class-basic/READM.md)
- [继承](./inheritance/README.md)
- [多态](./polymorphism/README.md)


## 对象持久化

Python的对象持久化功能通过3个标准的库模块来实现：pickle, dbm和shelve。

pickle模块是一种非常通用的对象格式化和解格式化工具：对于内存中几乎任何的Python对象，它都能聪明地把对象转换为字节串，这个字节串可以随后用来在内存中重新构建最初的对象。pickle模块几乎可以处理我们所能够创建的任何对象。

shelve模块提供了一个额外的层结构，允许按照键来存储pickle处理后的对象。Shelve使用pickle把一个对象转换为其pickle化的字符串，并将其存储在一个dbm文件中的键之下，随后载入的时候，shelve通过建获取pickle化的字符串，并用pickle在内存中重新创建最初的对象。

## 参考阅读

- (Static methods in Python?)[https://stackoverflow.com/questions/735975/static-methods-in-python]
- 《Python学习手册》
