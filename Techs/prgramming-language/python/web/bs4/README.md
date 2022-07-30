## Beautiful Soup 4

Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库,它能够通过你喜欢的转换器实现惯用的文档导航、查找、修改文档的方式。BS支出如下四种解析器：

- Python标准库：`BeautifulSoup(markup, "html.parser")`
- lxml HTML 解析器：`BeautifulSoup(markup, "lxml")`
- lxml XML 解析器：`BeautifulSoup(markup, ["lxml-xml"])`/`BeautifulSoup(markup, "xml")`
- html5lib：`BeautifulSoup(markup, "html5lib")`


## 安装

在碰到“ModuleNotFoundError: No module named 'beautifulsoup4'”的提示时，需要使用`pip install beautifulsoup4`来安装。


## 使用方法

将一段文档传给 BeautifulSoup 的构造方法，便得到了一个文档对象，可以传入字符串或者文件句柄。文档会首先被转换成Unicode再选择合适的解析器进行解释。

```
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup("<html>data</html>")
```


## 参考

- [Beautiful Soup 4.4.0 文档](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)
