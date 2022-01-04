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
