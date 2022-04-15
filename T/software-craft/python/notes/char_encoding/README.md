# 字符编码方法

## 字符集

根据字符所属的字符集，计算机内存中存储它们的方式有所不同。这些方法对应了不同的标准，比如
ASCII、Latin-1、UTF-8等。

ASCII标准在美国创建，定义了大多数美国程序员使用的文本字符串表示法。它定义了从0到127的字
符代码，允许每个字符存储在一个8位的字节中（真实用到其中的7位）。例如，把字符'a'映射为整
数值97，Python提供了多个函数来观察ASCII编码的对应关系：

```
ord('a') # 打印字符'a'对应的整数值
chr(97)  # 打印整数97对应的字符
```

由于ASCII只能表示128个字符，为了容纳更多字符，一些标准启用了ASCII标准中未曾使用的那一位，
即用0到255来表示字符，0到127兼容ASCII字符，值128到255分配给特殊字符。这样的一个标准是
Latin-1，广泛用于西欧地区。

然而，一些国家的字母表定义了更多的字符，超过了256个，以至于无法把每一个字符都表示为一个
字节，此时Unicode应运而生，它定义了一个字符集用来表示世界上的所有字符，每个字符对应一个
值（也称作码位）。

## 编码标准

Unicode是字符集，由于它定义的字符很多都超过了一个字节，因此需要对应的编/解码方式来完成
字符与字节之间的转换工作：

- 编码：将一个字符翻译为字节形式
- 解码：将字节翻译为字符形式

广泛使用的支持Unicode字符集的编码标准是UTF-8，它采用可变的字节数来编码字符。UTF-8兼容之
前提到的ASCII，Latin-1。

参考：

- [Unicode 和 UTF-8 有什么区别？](https://www.zhihu.com/question/23374078)

# 文件处理

## 文件读写

Python2.6中，文本文件和二进制文件之间没有主要区别，都是接受并返回作为str字符串的内容。
唯一的主要区别是，Windows下文本文件自动把\n行末字符和\r\n相互映射，而二进制文件不这么做。

Python3.0中对于文本文件和二进制文件进行了独立的区分：

1.当一个文件以文本模式打开的时候，读取其数据会自动将其内容解码（使用默认的或者指定的编解
码标准）再返回一个str。写入时则是在传输到文件之前进行编码。

2.当一个文件以二进制方式打开的时候，其内容不会进行解码，而是直接返回内容对应的bytes对象，
写入时也不做任何编码。

因此，以何种模式打开一个文件将决定Python使用哪种类型的对象来表示其内容。对于图像文件，其
他程序创建的必须解压的打包数据，或者一些设备数据流，使用bytes类型和二进制模式文件处理更
合适。对于文本内容，如程序输出、HTML、国际化文本或CSV或XML文件，使用str和文本模式更合适。

文本模式文件也处理在某种编码方案下可能出现在文件开始处的字节顺序标记（byte order marker,
BOM)序列。例如，在UTF-16和UTF-32编码中，BOM指定大尾还是小尾格式或声明编码类型。一般来说，
一个UTF-8的文本文件也包含了一个BOM来声明它是UTF-8，但并不保证这样。这也是之前碰到的为什
么EXCEL打开csv文件时显示乱码的原因：Windows系统下读取文件需要BOM信息，而其他平台则没这
个要求。

## 源文件字符集

对于在脚本文件中编码的字符串，Python默认地使用UTF-8编码，但是，它允许我们通过包含一个注
释来指明想要的编码，从而将默认值修改为支持任意的字符集。这个注释必须拥有如下的形式，并且
在Python 2.6或Python 3.0中必须作为脚本的第一行或第二行出现：

`# -*- coding: latin-1 -*-`

参考：  

- [「带 BOM 的 UTF-8」和「无 BOM 的 UTF-8」有什么区别？网页代码一般使用哪个？](https://www.zhihu.com/question/20167122)

# 常见问题

## 1.如何在Python脚本里面确定要处理文件的字符编码标准？

之前决定应该有什么功能来确定要处理文件的编码标准，可以使用`chardet`函数库来完成，先读取
文件内容，再判断其编码标准。

参考：

- [How to determine the encoding of text?](https://stackoverflow.com/questions/436220/how-to-determine-the-encoding-of-text)
- [How to convert a file to utf-8 in Python?](https://stackoverflow.com/questions/191359/how-to-convert-a-file-to-utf-8-in-python)

## 2.格式转换

将某种格式的文件转换为另一种格式：

```
f= open(path1, 'r', encoding=coding1)
content= f.read()
f.close()
f= open(path2, 'w', encoding=coding2)
f.write(content)
f.close()
```

参考：

- [Python: Convert File Encoding](http://xahlee.info/python/charset_encoding.html)

## 3. 将格式保存为UTF-8-BOM格式，以便Windows系统下面的office软件能够正常显示中文

在保存为UTF-8的时候指定的字符集参数为`utf-8`，但是对于带BOM的并不是`utf-8-bom`，而是在[Python中如何将文件保存为utf-8（带BOM）的格式](https://segmentfault.com/q/1010000002493464)里面提示的'utf_8_sig'。


## 参考

- 《Python学习手册》
