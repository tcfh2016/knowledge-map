## Selenium

Selenium使用对应浏览器的驱动来和浏览器进行交互，比如Firefox使用geckodriver, Chrome使用chromedriver，其他浏览器都可以在Selenium说明文档[1.5. Drivers](https://selenium-python.readthedocs.io/installation.html#drivers)找到。

使用浏览器主要涉及打开并和页面进行交互的过程，这里面的步骤大致包括下面几步：

- step 1：打开页面
- step 2：定位到页面的某个/某些元素
- step 3：操作元素
- step 4：关闭页面


### [打开浏览器]()

最简单的方式就是通过get()函数来打开页面：

```
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.google.com")
```


### [定位页面元素](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements)

定位到页面元素的手段比较多，常见是就是下面这些方法：

```
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
```

举个例子，对于下面的输入框元素我们可以通过多种方法来找到它。

```
<input type="text" name="passwd" id="passwd-id" />

element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
element = driver.find_element_by_css_selector("input#passwd-id")
```


### [操作页面元素](https://selenium-python.readthedocs.io/navigating.html)

操作定位到的元素主要包括输入、点击等。

1）对于文本框的操作

```
# 输入内容
element.clear()
element.send_keys("some text")
```

2）对于可选元素的操作

```
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)

# 取消选择
select = Select(driver.find_element_by_id('id'))
select.deselect_all()

# 获取选择项
select = Select(driver.find_element_by_xpath("//select[@name='name']"))
all_selected_options = select.all_selected_options
```

3）对于点击类型的按钮

```
# Assume the button has the ID "submit" :)
driver.find_element_by_id("submit").click()

# WebDriver 为每个element都提供了简便的submit函数来实现点击
element.submit()

# 点击
element.send_keys(" and some", Keys.ARROW_DOWN)
```

4）在Window和Frame之间移动

```
# 切换到某个window
driver.switch_to_window("windowName")

# 遍历每个打开的window
for handle in driver.window_handles:
    driver.switch_to_window(handle)

# 切换到某个frame
driver.switch_to_frame("frameName")

# 访问某个sub-frame
driver.switch_to_frame("frameName.0.child")
```

5）弹出的对话框

通过`alert = driver.switch_to.alert`可以访问弹出的alert对象，该接口也能够很好的访问confirm, prompt对象。


### [关闭页面]()


## Q&A

1）如何开始使用selenium ？

首先需要安装`selenium`，然后需要安装对应浏览器的驱动，比如Firefox的`geckodriver`，这个驱动的安装只需要把对应的exe（Windows系统下）下载下来并将其目录添加到系统PATH中即可。之后便是熟悉库里面各种变量和函数的使用。
