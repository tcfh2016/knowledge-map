## 如何使用

最简单的用法：

```
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"))
```

如果要将获取到的soup对象保存到文件里面，需要使用到[格式化输出](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id48)

```
print(soup.a.prettify()) # 以及直接保存
```

如果仅仅想获取某个tag的文本，那么使用[get_text()](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#get-text)即可：

```
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)

soup.get_text()
u'\nI linked to example.com\n'
soup.i.get_text()
u'example.com'
```
