## [Selenium](https://selenium-python.readthedocs.io/)

Selenium使用对应浏览器的驱动来和浏览器进行交互，比如Firefox使用geckodriver, Chrome使用chromedriver，其他浏览器都可以在Selenium说明文档[1.5. Drivers](https://selenium-python.readthedocs.io/installation.html#drivers)找到。

使用浏览器主要涉及打开并和页面进行交互的过程，这里面的步骤大致包括下面几步：

- step 1：打开页面
- step 2：定位到页面的某个/某些元素
- step 3：操作元素
- step 4：关闭页面


## 如何开始使用selenium ？

首先需要安装`selenium`，然后需要安装对应浏览器的驱动，比如Firefox的`geckodriver`，这个驱动的安装只需要把对应的exe（Windows系统下）下载下来并将其目录添加到系统PATH中即可。之后便是熟悉库里面各种变量和函数的使用。

## 隐藏模式执行


如果执行时不想打开浏览器，那么可以设置`headless`参数：

```
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)

```

参考：

- [How to hide Firefox window (Selenium WebDriver)?](https://www.tutorialspoint.com/how-to-hide-firefox-window-selenium-webdriver)


## 如何处理"NoSuchElementException"

首先，需要import异常模块；其次，使用try except来捕获异常。

参考：

- [](https://stackoverflow.com/questions/38022658/selenium-python-handling-no-such-element-exception)


## 'geckodriver' executable needs to be in PATH

在执行的时候需要geckodriver驱动，通常需要将它添加到系统变量里面，否则会提示找不到的错误：

```
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
```

通过在调用`webdriver.Firefox()`的时候使用`executable_path`参数来解决。


## “ModuleNotFoundError: No module named 'selenium'”

为什么安装了`selenium`但是import的时候一九提示“ModuleNotFoundError: No module named 'selenium'”

第一步执行`pip3 show selenium`查看`selenium`是否安装成功。

```
> pip3 show selenium
Name: selenium
Version: 3.141.0
Summary: Python bindings for Selenium
Home-page: https://github.com/SeleniumHQ/selenium/
Author: UNKNOWN
Author-email: UNKNOWN
License: Apache 2.0
Location: c:\users\lianbche\appdata\local\programs\python\python39\lib\site-packages
Requires: urllib3
Required-by:
```

在发现上面安装成功，并且重启编辑器尝试问题依然存在的时候，我们需要确认是否是因为电脑中安装了多个版本的Python，然后在Python A版本里安装`selenium`了，但是在运行程序的时候使用了Python B版本。那么如何确认呢？

首先在Windows下面搜索找到Python解析器打开，然后执行`import selenium`发现可以正常执行。现在命令行里面执行脚本发现不对那么基本肯定就是因为版本不匹配的问题。

通过`python -c "import os, sys; print(os.path.dirname(sys.executable))"`命令可以找到当前python调用的是`C:\msys64\mingw64\bin`下面的python。这也难怪通过`python -c "import sys; print(sys.path)"`的命令将系统的path打印出来，查看执行的Python里面是否包含了安装的`selenium`路径。

```
> python -c "import os, sys; print(os.path.dirname(sys.executable))"
C:\msys64\mingw64\bin

> python -c "import sys; print(sys.path)"
['', 'C:\\msys64\\mingw64\\lib\\python39.zip', 'C:\\msys64\\mingw64\\lib\\python3.9', 'C:\\msys64\\mingw64\\lib\\python3.9\\lib-dynload', 'C:\\N-xddks\\lianbche\\Downloads\\selenium-3.141.0', 'C:\\
msys64\\mingw64\\lib\\python3.9\\site-packages']
```

而如果搜索`selenium`发现安装在`C:\Users\lianbche\AppData\Local\Programs\Python\Python39\Lib\site-packages`，这样就确认了之所以运行python提示找不到模块的错误是因为模块的安装和当前程序的执行使用了不同的Python版本。

那么怎么解决这个问题？

在Linux上可以使用`alias`分别给不同版本的Python取别名并指向不同路径的Python版本。在Windows上最简单的方法就是把倾向版本的Path添加到系统变量的前面。可以看到这样调整之后一些相关的变量都会更新：

```
> python -c "import os, sys; print(os.path.dirname(sys.executable))"
C:\Users\lianbche\AppData\Local\Programs\Python\Python39

> python -c "import sys; print(sys.path)"
['', 'C:\\Users\\lianbche\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\lianbche\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\lianbche\\AppData\\Local\\Programs\\Py
thon\\Python39\\lib', 'C:\\Users\\lianbche\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\lianbche\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages']
```


参考：

- [ImportError: No module named 'selenium'](https://stackoverflow.com/questions/31147660/importerror-no-module-named-selenium)
- [How can I find where Python is installed on Windows?](https://stackoverflow.com/questions/647515/how-can-i-find-where-python-is-installed-on-windows)


## InvalidArgumentException: Message: unexpected end of hex escape

获取gerrit数据的时候出现的异常，其他的没有问题，但偶尔一个会抛出这种问题。

```
InvalidArgumentException: Message: unexpected end of hex escape at line 1 column 813928
```

这个问题没有找到答案，网络上提到不同的浏览器的结果不同，FireFox有问题但是Chrome有问题，可能和一些cache之类的有关。

参考：

- [Python Selenuim - InvalidArgumentExpression: unexpected end of hex escape](https://stackoverflow.com/questions/65729386/python-selenuim-invalidargumentexpression-unexpected-end-of-hex-escape)
- [Selenium driver.page_source InvalidArgumentException](https://stackoverflow.com/questions/73606180/selenium-driver-page-source-invalidargumentexception)


##  invalid argument: can't kill an exited process

在命令行上执行脚本时提示：

```
 raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: invalid argument: can't kill an exited process
```

原因在于我是在没有GUI的命令行上面执行脚本，但是脚本里面并没有使用`headless`模式：

```
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
```

参考：

- [WebDriverException: Message: invalid argument: can't kill ...](https://stackoverflow.com/questions/52534658/webdriverexception-message-invalid-argument-cant-kill-an-exited-process-with)