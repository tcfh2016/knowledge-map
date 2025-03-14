## [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库,它能够通过你喜欢的转换器实现惯用的文档导航、查找、修改文档的方式。BS支出如下四种解析器：

- Python标准库：`BeautifulSoup(markup, "html.parser")`
- lxml HTML 解析器：`BeautifulSoup(markup, "lxml")`
- lxml XML 解析器：`BeautifulSoup(markup, ["lxml-xml"])`/`BeautifulSoup(markup, "xml")`
- html5lib：`BeautifulSoup(markup, "html5lib")`

在[BeautifulSoup Parser](https://lxml.de/elementsoup.html)提到默认使用Python标准库中的`html.parser`。


## 使用方法

将一段文档传给 BeautifulSoup 的构造方法，便得到了一个文档对象，也可以传入字符串或者文件句柄。文档会首先被转换成Unicode再选择合适的解析器进行解释。

```
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html")) # 传入文档
soup = BeautifulSoup("<html>data</html>") # 传入字符串
```

之后就是使用bs4提供的特别的方法去获取、查找其中的内容。如果仅仅想获取某个tag的文本，那么使用[get_text()](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#get-text)即可：

```
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)

soup.get_text()
u'\nI linked to example.com\n'
soup.i.get_text()
u'example.com'
```

如果要将获取到的soup对象保存到文件里面，需要使用到[格式化输出](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id48)

```
print(soup.prettify())
```

## 解析器

```
BeautifulSoup(markup, "lxml")
BeautifulSoup(markup, "xml")
```

参考：

-[Installing a parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser)


## 常见问题

- `ModuleNotFoundError: No module named 'beautifulsoup4'`错误

在碰到“ModuleNotFoundError: No module named 'beautifulsoup4'”的提示时，需要使用`pip install beautifulsoup4`来安装。如果需要代理使用``pip3 --proxy ip:port install pandas`安装。


-  `'geckodriver' executable needs to be in PATH`错误

尽管已经使用`sys.path.append()`来添加了geckodriver所在的path，但是依然不行，使用`export PATH=target_path:${PATH}`之后就可以。

参考：

- [Selenium using Python - Geckodriver executable needs to be in PATH](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path)