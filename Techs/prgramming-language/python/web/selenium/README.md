## [Selenium](https://selenium-python.readthedocs.io/)

Selenium使用对应浏览器的驱动来和浏览器进行交互，比如Firefox使用geckodriver, Chrome使用chromedriver，其他浏览器都可以在Selenium说明文档[1.5. Drivers](https://selenium-python.readthedocs.io/installation.html#drivers)找到。

使用浏览器主要涉及打开并和页面进行交互的过程，这里面的步骤大致包括下面几步：

- step 1：打开页面
- step 2：定位到页面的某个/某些元素
- step 3：操作元素
- step 4：关闭页面

## Q&A

### 如何处理"NoSuchElementException"

首先，需要import异常模块；其次，使用try except来捕获异常。

参考：

- [](https://stackoverflow.com/questions/38022658/selenium-python-handling-no-such-element-exception)

### 'geckodriver' executable needs to be in PATH

在执行的时候需要geckodriver驱动，通常需要将它添加到系统变量里面，否则会提示找不到的错误：

```
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
```

通过在调用`webdriver.Firefox()`的时候使用`executable_path`参数来解决。


### 如何开始使用selenium ？

首先需要安装`selenium`，然后需要安装对应浏览器的驱动，比如Firefox的`geckodriver`，这个驱动的安装只需要把对应的exe（Windows系统下）下载下来并将其目录添加到系统PATH中即可。之后便是熟悉库里面各种变量和函数的使用。
